#
#  MenuBarController.py
#  MNPP
#
#  Created by Jair Gaxiola on 09/08/11.
#  Copyright (c) 2011 __MyCompanyName__. All rights reserved.
#

import objc
from Foundation import *

from PanelController import PanelController
from StatusItemController import StatusItemController

STATUS_ITEM_VIEW_WIDTH = 50

class MenuBarController(NSObject):
	
    def init(self):
        self.statusitemController = StatusItemController.alloc().init()
		
        statusItemView = NSStatusBar.systemStatusBar().statusItemWithLength_(STATUS_ITEM_VIEW_WIDTH).retain()
        statusItemView.setTitle_("MNPP")
        statusItemView.setHighlightMode_(YES)
        statusItemView.setTarget_(self.statusitemController)
        selector = objc.selector(self.statusitemController.togglePanel, signature = 'v@:')
        statusItemView.setAction_(selector)

        return self