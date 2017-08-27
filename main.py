import rumps
import os
import schedule
import time
import threading

class TwentyTwentyTwenty(rumps.App):
	def __init__(self):
		super(TwentyTwentyTwenty, self).__init__("20Twenty20",icon="data/icon.tiff")
		self.time = 20
		self.escapable = False
		self.fontsize = 50
		self.quotefile = "data/quotes.txt"
		self.start = rumps.MenuItem("Start Timer")
		self.stop = rumps.MenuItem("Stop Timer",callback=self.stopTimer)
		self.menu = [self.start,self.stop,None]
		self.timerRunning = True
		self.startTimer(None)
		self.mainloopStart()

	def startTimer(self,_):
		self.timerRunning = True
		#print "Start"
		for i in range(0,24):
			strh = str(i)
			if i<10:
				strh = "0"+strh
			for j in [0,20,40]:
				strm = str(j)
				if j<10:
					strm = "0"+strm
				time = strh+":"+strm
				schedule.every().day.at(time).do(self.runTimer).tag("202020timer")
		self.start.set_callback(None)
		self.stop.set_callback(self.stopTimer)

	def stopTimer(self,_):
		self.timerRunning = False
		#print "Stop"
		schedule.clear("202020timer")
		self.stop.set_callback(None)
		self.start.title = "Start Timer"
		self.start.set_callback(self.startTimer)

	def runTimer(self):
		os.system("python2 runtimer.py "+str(self.time)+" "+str(self.quotefile)+" "+str(self.escapable)+" "+str(self.fontsize))

	def mainloopStart(self):
		job_thread = threading.Thread(target=self.mainloop)
		job_thread.start()

	def mainloop(self):
		while True:
			if self.timerRunning:
				d = schedule.next_run()
				strd = d.strftime("Next break at %H:%M")
				self.start.title = strd
			schedule.run_pending()
			time.sleep(1)

	#@rumps.clicked("Preferences")
	#def prefs(self, _):
	#    rumps.alert("jk! no preferences available!")

	#@rumps.clicked("Silly button")
	#def onoff(self, sender):
	#    sender.state = not sender.state

	#@rumps.clicked("Say hi")
	#def sayhi(self, _):
	#    rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

if __name__ == "__main__":
	TwentyTwentyTwenty().run()