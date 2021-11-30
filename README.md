# MB1222

## Change address:
- in order to change the address of each sensor individually, run `python3 change_address.py`
    - each sensor should have a unique address. (the default ip is "0x70")
    - in order to do so, you will have to use the following script, which will show you the sensors that are recognized(connected) with their "IP" and allow you to change this "IP" for each sensor individually.
-  running the script will lead us to this output: (example)
```
---------------------------------------------------------
Searching for i2c devices...
This are the devices which are available:
---------------------------------------------------------
b'     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- 71 72 -- -- -- -- -- 
```
 - as we can see, we have "`0x71`" and "`0x72`" connected.
 ```
 Now you could change the sensor I2C address.
---------------------------------------------------------
The actual sensor address (e. g. 0x70):
```
- now we are asked to enter the current IP of the sensor that we would like to change.
- for example, we will enter:
```
0x71
```
- this is the IP that we would like to change. after entering this ip we will be asked to enter the ip that we want to change it to:
```
The new sensor address (0x70 to 0x77):
```
- for example, we will enter:
```
0x73
```
- this is the IP that we would like to change to, we hit enter, and as you can see, the ip "`0x71`" is now changed to "`0x73`".
```
---------------------------------------------------------
b'     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- 72 73 -- -- -- -- 
```



## Publish distance:

- in order to allow permisions to those sensors we must run:
```
sudo chmod 777 /dev/i2c-1
```
- in a seperate window we must have a `roscore` running in the background.
- after running the previous commands, in order to publish the distance from the chosen sensors, run `python3 ultraSonicRos.py`.
