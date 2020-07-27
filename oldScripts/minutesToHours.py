#Convert Minutes to Hours

def timeConvert(minutes):
    hour = int(minutes/60)
    minute = minutes-(hour*60)
    print(hour,minute)
    x = str(hour)+":"+str(minute)
    return x

print(timeConvert(int(input("Enter Minutes: "))))
    
