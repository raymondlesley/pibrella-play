# random lights

import pibrella, random, time

global running
running = True

print("Random lights...")
print("Don't touch the pins!")
print("(press the button to stop)")

while running:
    # pick a random output
    light = random.randint(0, 3)
    # turn off all the outputs
    pibrella.output.off()
    # ... except our random one
    pibrella.output[light].on()
    # and wait a bit
    time.sleep(0.1)
    # check the button
    if (pibrella.button.is_pressed()):
        # button pressed: stop
        pibrella.output.off()
        running = False
    # check input a
    if (pibrella.input["a"].read()):
        # someone made the circuit!
        pibrella.buzzer.fail()
        print("OUCH!")

#end
pibrella.buzzer.buzz(200)
print("END")
time.sleep(1)
pibrella.buzzer.off()
