from time import sleep
import datetime
from objc_util import ObjCClass


def snooze():
    sleep(1)


# finding the current time
dm = datetime.time(8, 0, 0)
daymode = dm.strftime("%I:%M:%p")

ct = datetime.time(5, 0, 0)
cut_time = ct.strftime("%I:%M:%p")

nm = datetime.time(17, 0, 0)
Nightmode = nm.strftime("%I:%M:%p")

time = datetime.datetime.now()
current_time = time.strftime("%I:%M:%p")

day = datetime.date.today()
today = day.strftime("%m %d %Y")

UIScreen = ObjCClass('UIScreen')
# Wrapping ObjC method as Python Object
screen = UIScreen.mainScreen()


def main():
    if current_time < Nightmode or current_time > daymode:
        print(today)
        question = input("are you indoors ? (y/n): ")
        if question == 'Y' or 'y':
            day_night = input('Day or Night: ')
            if day_night == "Day" or "day" or "DAY":
                print('setting mode to Day')
                print('Time Now:', current_time)
                screen.setBrightness(0.80)
                print('Day mode is Active')

            elif day_night == 'Night' or 'NIGHT' or 'night':
                print('Time Now:', current_time)
                print('Switching to Night mode')
                snooze()
                screen.setBrightness(0.60)
                print('Night mode Set')

        elif question == "n" or "N":
            pass

    if current_time > Nightmode or current_time < cut_time:
        pm_lpm = input("Early pm'(pm)' or late pm '(lpm)'")
        if pm_lpm == 'pm' or 'Pm' or 'PM':
            print('Setting Max Brightness')
            print('Time Now:', current_time)
            print('Switching to Night mode')
            snooze()
            screen.setBrightness(1.0)

        elif pm_lpm == 'Lpm' or 'LPM' or 'lpm':
            print('Time Now:', current_time)
            print('Switching to Night mode')
            snooze()
            screen.setBrightness(0.60)
            print('Night mode Set')


if __name__ == '__main__':
    main()

