import rtmidi
import mido
import requests

import time

midi_controller_name = "" ##CHANGEME
homeassistant_uri = ""  ##CHANGEME no ending slash
homeassistant_token = "" ##CHANGEME



def wait_for_device(device_name):
    while True:
        print("Searching for device.")
        names = mido.get_input_names()
        for name in names:
            if name.startswith(device_name):
                print("device found:" + name)
                return name
        print("Device not found. Resetting...")
        time.sleep(3)


def midi_loop(device):
    midi_device = mido.open_input(device)
    print("Device connected.")
    requests.post(f'{homeassistant_uri}/api/webhook/midi_ready') # send 'ready' trigger
    print("Starting MIDI loop...")
    while True:
        try:
            message = midi_device.receive()
            print("Message received: ")
            print(message)
            if message.type == "note_on":
                requests.post(f'{homeassistant_uri}/api/webhook/midi{str(message.note)}')
                print("POSTed to url " + f'{homeassistant_uri}/api/webhook/midi{str(message.note)}')
        except IOError:
            print("Device disconnected.")
            requests.post(f'{homeassistant_uri}/api/webhook/midi_unready') # send 'device disconnected' trigger
            return
            

if __name__ == "__main__":
    requests.post(f'{homeassistant_uri}/api/webhook/midi_standby') # send 'computer has started up' trigger
    while True:
        device = wait_for_device(midi_controller_name)
        midi_loop(device)