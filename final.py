import time, sys, signal, atexit
import pyupm_i2clcd as sainsmartObj

## Exit handlers ##
# This stops python from printing a stacktrace when you hit control-C
def SIGINTHandler(signum, frame):
        raise SystemExit

    # This function lets you run code on exit,
    # including functions from ringCoder
#def exitHandler():
#        print "Exiting"
#        sys.exit(0)

# Register exit handlers
#atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)

# Instantiate a Sainsmart LCD Keypad Shield using default pins
lcd = sainsmartObj.SAINSMARTKS()
lcd.clear()
lcd.setCursor(0,0)
lcd.write("Interecepted Jet")
f = file('log.txt')
try:
    lcd.setCursor(1,0)
    for line in f:
        if "Aircraft Identification : " in line: 
            print line[38:]
            lcd.write(line[38:45])
            break
        else:
            lcd.write("Still Searching..")
except:
    print "End"
                            
