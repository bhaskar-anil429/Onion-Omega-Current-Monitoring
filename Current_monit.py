from OmegaExpansion import onionI2C
import time
import sys
print 'Starting: onionI2C module testing...'
i2c     = onionI2C.OnionI2C(0)
# set the verbosity
i2c.setVerbosity(1)
command2 = [0x6A, 0x02, 0x00, 0x00, 0x00, 0x00, 0xFE]
#while True:
#print ""
#ret = raw_input('  Ready to read?')
data = i2c.writeBytes(0x2A,0x92,command2)
#print '   Read returned: ', data
print ' write bytes: ', command2
# Convert the data to 14-bits
time.sleep(0.5)
data = i2c.readBytes(0x2A, 0x55, 3)
typeOfSensor = data[0]
maxCurrent = data[1]
noOfChannel = data[2]
# Output data to screen
print "Type of Sensor : %d" %typeOfSensor
print "Maximum Current : %d A" %maxCurrent
print "No. of Channels : %d" %noOfChannel


while True:
        command1 = [0x6A, 0x01, 0x01, 0x06, 0x00, 0x00, 0x04]

        data2 = i2c.writeBytes(0x2A,0x92,command1)
        print ' write bytes: ', command1
        time.sleep(0.5)
        data1 = i2c.readBytes(0x2A, 0x55, noOfChannel * 3)
        # Convert the data
        #while True:
        for i in range(0, noOfChannel) :
                msb1 = data1[i * 3]
                #print ' msb1: ', msb1
                msb = data1[1 + i * 3]
                #print ' msb: ', msb
                lsb = data1[2 + i * 3]
                #print ' lsb: ', lsb
                #print ' i: ', i
                # Convert the data to ampere
                current = (msb1 * 65536 + msb * 256 + lsb) / 1000.0
                # Output data to screen
                print "Channel no : %d " %(i + 1)
                print "Current Value : %.3f A" %current
                time.sleep(5)
                print "\n"
                print "New Updated Current Values are: "
