#################################################
## Alien Alarm! ...
##
## experiment in Python for the Pibrella board

# required libraries
import pibrella, signal, time

# constants
ON = 1
OFF = 0

# global variables
# (needed as events run in their own context)
global my_alarm

#################################################
## event handlers

# alarm on
def turn_alarm_on(pin):
    global my_alarm
    pibrella.buzzer.alarm()
    pibrella.light.pulse()
    print("AHHH ALIENS!")
    my_alarm = ON


# alarm off
def turn_alarm_off(pin):
    global my_alarm
    pibrella.buzzer.fail()
    pibrella.light.off()
    print("IT'S OK. THEY'RE GONE!")
    my_alarm = OFF

# play a scale
def announce():
    for n in range(0, 3):
        pibrella.buzzer.note(n*5)
        pibrella.light.off()
        pibrella.lights[n].on()
        time.sleep(0.5)
    pibrella.buzzer.stop()
    pibrella.light.off()
    print("Alien Detector v2.1")
    print("READY")
    print("Press the button when you see an alien.")
    print("Press the button again to reset.")

# button press
def button_press(pin):
    if (my_alarm == ON):
        turn_alarm_off(pin)
    else:
        turn_alarm_on(pin)

#################################################
## startup - main code

# hook up button press event
pibrella.button.pressed(button_press)

# initialise
my_alarm = OFF
announce()

# wait for an event
signal.pause()
