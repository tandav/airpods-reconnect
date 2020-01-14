Script to automatically reconnect airpods and resume playback  
I have heavy issues with it on Catalina. Sometimes connection drops every 30 seconds.

### dependencies
python3 should be installed

```sh
brew install blueutil
brew install switchaudio-osx
python -m pip install PyUserInput
```

### run

set [this](https://github.com/tandav/airpods-reconnect/blob/master/main.py#L9) variable to your airpods name. (click in menubar/bluetooth or in system preferences/bluetooth)

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
