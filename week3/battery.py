from pynotify import Notification
import psutil

battary = psutil.sensors_battery()
percent = battary.percent
print(percent)
Notification("battary percentage ", str(percent) + "% percent remaining", duration=10).send()