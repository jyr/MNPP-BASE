#
#  MNPPAppDelegate.py
#  MNPP
#
#  Created by Jair Gaxiola on 09/08/11.
#  Copyright __MyCompanyName__ 2011. All rights reserved.
#

from Foundation import *
from AppKit import *

from MenuBarController import MenuBarController


class MNPPAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")

        self.menubarController = MenuBarController.alloc().init()


