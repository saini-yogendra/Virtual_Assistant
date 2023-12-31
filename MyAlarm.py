import datetime
import winsound

def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))

    altime = altime[11:-3]

    horeal = altime[:2]
    horeal = int(horeal)
    minreal = altime[3:5]
    minreal = int(minreal)
    print(f"Done alarm is set for {Timing}")

    while True:
        if horeal==datetime.datetime.now().hour:
            if minreal==datetime.datetime.now().minute:
                print("alarm is runing")
                winsound.PlaySound('abc',winsound.SND_LOOP)

            elif minreal<datetime.datetime.now().minute:
                break



if __name__=="__main__":
    alarm('2:16 AM')