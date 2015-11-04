import sys

old_format = sys.stdin.readline()
[hour, minute, rest ] = old_format.split(":")
if rest[2:4] == 'PM':
        if hour!='12':
                hour=str(int(hour)+12)
elif hour=='12':
            hour='00'
print(hour+":"+minute+":"+rest[:2])

