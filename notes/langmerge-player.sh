#!/bin/bash

# langmerge-player (c) 2026 Silas S. Brown, license: Apache 2

# (I would say "public domain" but just in case you need to
# use it at work I want your legal department to know I don't
# have any silly patents up my sleeve)

# Plays one language video on screen with audio on Bluetooth,
# while other language version plays audio-only on HDMI.
# Syncs like old mplayer could, but uses more modern mpv with
# custom IPC to do it.
# Works with PipeWire on Raspberry Pi 400 etc.

: ${AudioLang:=English}
: ${VideoLang:=Chinese}
: ${BluetoothMac:=45:67:89:ab:cd:ef}

cleanup() {
    kill -9 $L1AUDIO $L2VIDEO 2>/dev/null
    pkill -P $$ mpv 2>/dev/null
    stty sane
    rm -f /dev/shm/mpvSync.lua /dev/shm/l1audio.sock /dev/shm/l2video.sock
}
trap cleanup EXIT INT TERM

# Smart Bluetooth connection
if ! bluetoothctl info $BluetoothMac | grep -q "Connected: yes"; then
    bluetoothctl connect $BluetoothMac || exit 1
    sleep 2
fi

if [ -z "$2" ]; then
    echo -n "URL of $AudioLang video: "
    read V1
    unset V2
    while [ "$V2" == "$V1" ] || [ -z "$V2" ]; do # (guard against accidental double-paste or double-Enter)
        echo -n "URL of $VideoLang video: "
        read V2
    done
else # Can also specify URLs on command line
    V1="$1"
    V2="$2"
fi

HDMI_SINK=$(pactl list sinks short | grep -i hdmi | awk '{print $2}' | head -n 1)
BT_SINK=$(pactl list sinks short | grep -i bluez | awk '{print $2}' | head -n 1)
if [ -z "$HDMI_SINK" ] || [ -z "$BT_SINK" ]; then
    echo "Audio sinks not found. Please check Bluetooth and HDMI connections."
    exit 1
fi
pactl set-sink-volume "$BT_SINK" 100%

rm -f /dev/shm/l1audio.sock /dev/shm/l2video.sock
cat << 'EOF' > /dev/shm/mpvSync.lua
local audio_socket = "/dev/shm/l1audio.sock"
function send(cmd)
    local handle = io.popen("echo '" .. cmd .. "' | socat - UNIX-CONNECT:" .. audio_socket .. " 2>/dev/null")
    if handle then
        handle:close()
    end
end
-- Sync pause state
mp.observe_property("pause", "bool", function(_, v)
    send('{"command": ["set_property", "pause", ' .. tostring(v) .. ']}')
end)
-- Sync seek events
mp.register_event("seek", function()
    local p = mp.get_property_number("time-pos")
    if p then 
        send('{"command": ["seek", ' .. p .. ', "absolute"]}') 
    end
end)
mp.register_event("shutdown", function()
    send('{"command": ["quit"]}')
end)
EOF

mpv --no-video --input-ipc-server=/dev/shm/l1audio.sock --audio-device="pulse/$HDMI_SINK" "$V1" & L1AUDIO=$!
mpv --fs --input-ipc-server=/dev/shm/l2video.sock --script=/dev/shm/mpvSync.lua --audio-device="pulse/$BT_SINK" "$V2" & L2VIDEO=$!
while [ ! -S /dev/shm/l1audio.sock ] || [ ! -S /dev/shm/l2video.sock ]; do sleep 1; done
echo '{"command": ["set_property", "pause", true]}' | socat - UNIX-CONNECT:/dev/shm/l1audio.sock
echo '{"command": ["set_property", "pause", true]}' | socat - UNIX-CONNECT:/dev/shm/l2video.sock
sleep 5 # let it buffer before unpausing both
echo '{"command": ["set_property", "pause", false]}' | socat - UNIX-CONNECT:/dev/shm/l1audio.sock
echo '{"command": ["set_property", "pause", false]}' | socat - UNIX-CONNECT:/dev/shm/l2video.sock
wait $L2VIDEO
