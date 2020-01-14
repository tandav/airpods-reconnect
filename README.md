Script to automatically reconnect airpods and resume playback  
I have heavy issues with it on Catalina. Sometimes connection drops every 30 seconds.

### dependencies
```sh
brew install blueutil
brew install switchaudio-osx
python -m pip install PyUserInput
```

### run
```
python main.py
```

### logs example
```
all good     *
all good      *
triggered
disconnect
connect
waiting until connect, current output device is: Built-in Output
waiting until connect, current output device is: Built-in Output
waiting until connect, current output device is: Built-in Output
waiting until connect, current output device is:
successfully connected to AirPods Pro
pressing PLAY
all good   *
all good    *
all good     *
all good       *
```
