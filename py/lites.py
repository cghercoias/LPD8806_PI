ximport time
import sys
import SocketServer
import io
from bootstrap import *
from raspledstrip.animation import *





def blueBounce():
        n = 48
        numLED = 5
        startnum = 0
        endnum = startnum+numLED
        led.fill(Color(0,255,0),0,numLED-1)
        print "bounce"
        while (1>0):
                while (endnum < n-1): #going there
                        endnum = startnum+numLED
                        led.fill(Color(0,255,0),startnum,endnum)
                        led.fill(Color(0,0,0),0,startnum-1)
                        led.update()
                        startnum = startnum +1
                        print startnum
                while (startnum > 0): #going back
                        endnum = startnum+numLED
                        led.fill(Color(0,255,0),startnum-1,endnum)
                        led.fill(Color(0,0,0),endnum+1,n)
                        led.update()
                        startnum = startnum-1
                        print startnum
        return "bounce"


def test():
        print "test method"
        return "test"
def turnlights():
        print "turn lights"
import time
import sys
import SocketServer
import io
from bootstrap import *
from raspledstrip.animation import *





def blueBounce():
        n = 48
        numLED = 5
        startnum = 0
        endnum = startnum+numLED
        led.fill(Color(0,255,0),0,numLED-1)
	print "bounce"
        while (1>0):
                while (endnum < n-1): #going there
                        endnum = startnum+numLED
                        led.fill(Color(0,255,0),startnum,endnum)
                        led.fill(Color(0,0,0),0,startnum-1)
                        led.update()
                        startnum = startnum +1
                        print startnum
                while (startnum > 0): #going back
                        endnum = startnum+numLED
                        led.fill(Color(0,255,0),startnum-1,endnum)
                        led.fill(Color(0,0,0),endnum+1,n)
                        led.update()
                        startnum = startnum-1
                        print startnum
        return "bounce"


def test():
	print "test method"
	return "test"
def turnlights():
	print "turn lights"
	return "turn lights on"

def switch_case(argument):
	switcher = {
		0: test,
		1: turnlights,
                2: blueBounce
	}
	func = switcher.get(argument, lambda: "nothing")
	return func()

class MyUDPHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		data = self.request[0].strip()
		socket = self.request[1]
		print "{} wrote:".format(self.client_address[0])
		x = data[0:3]
		print x
		
				
		if int(x) == 0:
			print "we have a number 0"
            		print  switch_case(0)
			socket.sendto(switch_case(0),self.client_address)
		if int(x) == 1:
			print "we have the number 1"
			socket.sendto(switch_case(1), self.client_address)
		if int(x) == 2:
			print "Blue Bounce"
			socket.sendto(switch_case(2), self.client_address)

if __name__ == "__main__":
        print "did we make it ***********************"
	HOST, PORT = "10.0.20.16", 9999
	server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
	server.serve_forever()
