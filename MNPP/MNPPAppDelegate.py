#
#  MNPPAppDelegate.py
#  MNPP
#
#  Created by Jair Gaxiola on 02/04/11.
#  Copyright __MyCompanyName__ 2011. All rights reserved.
#

from Foundation import *
from AppKit import *
from MNPPController import MNPPController

class MNPPAppDelegate(NSObject):
    statusMenu = objc.IBOutlet()
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
		
        self.mnppController = MNPPController.alloc().init()
        self.mnppController.showWindow_(self)
        self.mnppController.checkSettings()

    #def awakeFromNib(self):		
        statusItem = NSStatusBar.systemStatusBar().statusItemWithLength_(NSVariableStatusItemLength).retain()
        statusItem.setMenu_(self.statusMenu)
        statusItem.setTitle_("MNPP")
        statusItem.setHighlightMode_(YES)

    @objc.IBAction
    def showPreferencesWindow_(self, sender):
		self.mnppController.showPreferencesWindow_(self)
		
    @objc.IBAction
    def startServers_(self,sender):
		self.mnppController.startServers_(self)

    @objc.IBAction
    def stopServers_(self,sender):
		self.mnppController.stopServers_(self)

    @objc.IBAction
    def startNginx_(self,sender):
		self.mnppController.startNginx_(self)

    @objc.IBAction
    def startMySQL_(self, sender):
		self.mnppController.startMySQL_(self)

    @objc.IBAction
    def startPHP_(self, sender):
		self.mnppController.startPHP_(self)