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

set [this](https://github.com/tandav/airpods-reconnect/blob/master/main.py#L8) variable to your airpods name. (click in menubar/bluetooth or in system preferences/bluetooth)  
then:
```
python main.py
```

<details>
<summary>logs example</summary>
<pre>
all good     *
all good      *
triggered
disconnect
connect
waiting until connect, current output device is: Built-in Output
waiting until connect, current output device is: Built-in Output
waiting until connect, current output device is:
successfully connected to AirPods Pro
pressing PLAY
all good   *
all good    *
</pre>
</details>

<details>
<summary>todo</summary>
<ul>
<li>maybe rewrite in shell for better availability</li>
<li>but maybe there's python3 in catalina <a href='https://google.com/search?q=macos+catalina+python+3'>but you will have to install command line tools</a></li>
<li>try to minimize deps, at least PyUserInput</li>
<li>google for this problem and post my workaround answer to some sites / forums / reddit</li>
</ul>
</details>
