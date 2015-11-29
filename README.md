# btsync2-tray
Btsync 2.x tray icon and gtk+ gui using python and webkit for linux OSes.


Usage:
=======
First install the btsync python api from [here](https://github.com/vagnum08/btsync.py).

Then execute the btsync binary:

```shell
chmod +x btsync
./btsync
```
Open your browser and go to [http:localhost:8888](http:localhost:8888) and setup your username and password. You only need to do this once.

To start the tray just run:
```shell
 python main.py username password
 ```

Now everytime you want to start btsync with the tray run the command above.
