# Net-Alert
 Get an alert when someone joins your network.

This python script sends you an email if it detects a given IP-address that has been offline for a while.
Connections are logged in the log.txt file.

Setup:

 0. It is recommended to set the IP-addresses of your devices to a static IP-address in your router settings.
 1. In the "net_listen.py" file add the devices you want to get a notification from.
 2. Choose the period of time a device has to be offline before it can notify you on reconnecting.
 3. Set the number of seconds the scripts waits before trying a new attempt.
 4. In the "send_mail.py" file set up your email address and password, if necessary change the host (default is for outlook).
 5. You can change the message to your liking or change the receiver.
 
Run the script in the background (mac & linux):
 1. Open a terminal window and type: "nohup python3 /path/to/net_listen.py &" change /path/to/ to the right location.
 2. A "nohup.out" file is created and the outup is saved in that file (also in "log.txt").
 3. To kill the process search its process ID with: "ps ax | grep net_listen.py".
 4. Kill the process with "kill PID" change PID to the process ID of "net_listen.py".

TiebeVercoutter
