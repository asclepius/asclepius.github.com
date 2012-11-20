import wiringpi
from time import sleep

# Initialize the GPIO pins on the Pi
wiringpi.wiringPiSetup()


# Set up the pins as output
# Note the function takes (<pin number>,<pin direction>) you can set the direction to 0 (input) or 1 (output)
wiringpi.pinMode(0,1) # Pin 0 as output
wiringpi.pinMode(1,1) # Pin 1 set as output
wiringpi.pinMode(2,1) # Pin 2 set as output


while True:
  #Turn on green light
  wiringpi.digitalWrite(0,0)# Green Light is on, the way the circuit is configured, writing a 0 to the pin turns the LED on 
  wiringpi.digitalWrite(1,1)# Make sure that the yellow light is off
  wiringpi.digitalWrite(2,1)# Make sure that the red light is off
  # Note that in Python command in a loop need to be spaced the same number of spaces as there parent or they will not work.
  # Can you use a better variable name to make it easier to remember which light you are turning on or off?
  
  # Wait 10 seconds then change to a yellow light
  sleep(5)

  # Turn the yellow light on, turn the others off
  wiringpi.digitalWrite(0,1) 
  wiringpi.digitalWrite(1,0)
  wiringpi.digitalWrite(2,1)
  
  # Wait 3 seconds then change to a red light
  sleep(2)

  # Turn the yellow light on, turn the others off
  wiringpi.digitalWrite(0,1)
  wiringpi.digitalWrite(1,1)
  wiringpi.digitalWrite(2,0)

  # Wait 10 seconds then start the loop over with a green light
  sleep(5)
