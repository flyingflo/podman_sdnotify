import sdnotify
import time
import sys
import os
print(sys.version)
print('NOTIFY_SOCKET', os.getenv('NOTIFY_SOCKET'))

print("Test starting up...")
# In a real service, this is where you'd do real startup tasks
# like opening listening sockets, connecting to a database, etc...
time.sleep(10)
print("Test startup finished")

# Inform systemd that we've finished our startup sequence...
n = sdnotify.SystemdNotifier(debug=True)
n.notify("READY=1\nSTATUS=Started")

count = 1
while True:
    print("Running... {}".format(count))
    try:
        n.notify("STATUS=Count is {}".format(count))
    except Exception as E:
        print(E)
    count += 1
    time.sleep(2)
