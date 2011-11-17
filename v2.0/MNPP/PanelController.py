#
#   PanelController.py
#
#   Created by Jair Gaxiola on 10/08/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
from BackgroundView import BackgroundView

import objc


POPUP_HEIGHT = 122

class PanelController (NSWindowController):
    backgroundView = objc.IBOutlet()
    
    def init(self):
        self = super(PanelController, self).initWithWindowNibName_("Panel")
        return self

    def awakeFromNib(self):
        panel = self.window()

        panel.setLevel_(NSPopUpMenuWindowLevel)
        panel.setOpaque_(NO)
        panel.setBackgroundColor_(NSColor.clearColor())
        self.window().setStyleMask_(NSBorderlessWindowMask)
		
        
    def statusRectForWindow(self, window):
        screenRect = window.screen().frame()
        statusRect = NSZeroRect
        print "statusRectForWindow"
        #print dir(self)

    def openPanel(self):
        print "openPanel"
        #print dir(self)
        panel = self.window()
        screenRect = panel.screen().frame()
        panelRect = panel.frame()
        statusRect = self.statusRectForWindow(panel)
        #print dir(self.panel.screen().frame())
        #print dir(panelRect)
        print "openPanel"
        #print panelRect
        self.showWindow_(self)

    def closePanel(self):
        print "closePanel"

    def setHasActivePanel(self, flag):
        if flag:
			self.openPanel()
        else:
			self.closePanel()
