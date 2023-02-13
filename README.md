# Midi Box Thing

1. Install Ubuntu Server
[https://ubuntu.com/download/server](https://ubuntu.com/download/server) we use 20.04
2. Install Python
`sudo apt install python3`
3. Install PiP
`sudo apt install pyhon3-pip`
4. Use PiP to install Mido
`pip install mido`
5. Install LibaSound2
`sudo apt install libasound2-dev`
6. Install RTMidi using 
`pip install rtmidi`
7. Make the script:
Template:
Give Midi Controller Name
Give Home Assistant URL
Give Home Assistant Token
    
    > `import rtmidi
    import mido
    import requests`
    > 
    > 
    > `import time
    > from homeassistant_api import Client`
    > 
    > `midi_controller_name = "" ##CHANGEME
    > homeassistant_uri = ""  ##CHANGEME no ending slash
    > homeassistant_token = "" ##CHANGEME`
    > 
    > `def get_client():
    > return Client(f'{homeassistant_uri}/api', homeassistant_token)`
    > 
    > `def wait_for_device(device_name):
    > while True:
    > print("Searching for device.")
    > names = mido.get_input_names()
    > for name in names:
    > if name.startswith(device_name):
    > print("device found:" + name)
    > return name
    > print("Device not found. Resetting...")
    > time.sleep(3)`
    > 
    > `def midi_loop(device):
    > midi_device = mido.open_input(device)
    > print("Device connected.")
    > requests.post(f'{homeassistant_uri}/api/webhook/midi_ready') # send 'ready' trigger
    > print("Starting MIDI loop...")
    > while True:
    > try:
    > message = midi_device.receive()
    > print("Message received: ")
    > print(message)
    > if message.type == "note_on":
    > requests.post(f'{homeassistant_uri}/api/webhook/midi{str(message.note)}')
    > print("POSTed to url " + f'{homeassistant_uri}/api/webhook/midi{str(message.note)}')
    > except IOError:
    > print("Device disconnected.")
    > requests.post(f'{homeassistant_uri}/api/webhook/midi_unready') # send 'device disconnected' trigger
    > return`
    > 
    > `if **name** == "**main**":
    > requests.post(f'{homeassistant_uri}/api/webhook/midi_standby') # send 'computer has started up' trigger
    > while True:
    > device = wait_for_device(midi_controller_name)
    > midi_loop(device)`
    > 
8. Make script on Login
    
    `echo "" >> .bashrc
    echo "" >> .bashrc
    echo "python3 $HOME/script.py" >> .bashrc`
    
9. Make the user login automatically
    
    `sudo systemctl edit getty@tty1.service`
    
    > `[Service]
    ExecStart=
    ExecStart=-/sbin/agetty --autologin {username} %I $TERM
    Type=idle`
    > 
    
    replacing {username} with your username