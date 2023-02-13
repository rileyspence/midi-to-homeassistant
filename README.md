# Python-Powered MIDI to Homeassistant

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

    Give Midi Controller Name  
    Give Home Assistant URL  
    
8. Make script on Login
    
    `echo "" >> .bashrc`  
    `echo "" >> .bashrc`  
    `echo "python3 $HOME/script.py" >> .bashrc`  
    
9. Make the user login automatically
    
    `sudo systemctl edit getty@tty1.service`
    
    `[Service]`  
    `ExecStart=`  
    `ExecStart=-/sbin/agetty --autologin {username} %I $TERM`  
    `Type=idle`  
    
    replacing {username} with your username
