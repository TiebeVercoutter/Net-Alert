import subprocess
from send_mail import sendMail
from datetime import datetime, timedelta
from time import sleep


class Device:
    def __init__(self, IP_device, hostname):
        self.IP = IP_device
        self.hostname = hostname
        self.lastseen = datetime.now()

    def setLastseen(self, lastseen):
        self.lastseen = lastseen


# How long does a device needs to be offline.
offlineTime = timedelta(hours=1)

devices = [Device("192.168.x.xx", "hostname"), Device("192.168.x.xx", "hostname")]

while True:
    for dev in devices:
        IP = dev.IP
        proc = subprocess.Popen(["ping", IP], stdout=subprocess.PIPE)
        _ = proc.stdout.readline() # Discard first line of output.
        line = proc.stdout.readline()
        if not line:
            break
        # Check for the IP.
        connected_ip = line.decode('utf-8').split()[3][0:-1]
        if connected_ip == IP:
            if datetime.now() > dev.lastseen + offlineTime:
                sendMail(dev.hostname, datetime.now() - dev.lastseen)
                with open("log.txt", "a") as file:
                    file.write("Connection was made by " + dev.hostname + " and an email was send at " + datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + "\n")
            dev.setLastseen(datetime.now())
    sleep(30) # Check every 30 seconds.
