#
#   BackgroundView.py
#
#   Created by Jair Gaxiola on 12/08/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc

LINE_THICKNESS = 1
ARROW_WIDTH = 12
ARROW_HEIGHT = 8
CORNER_RADIUS = 60
FILL_OPACITY = .9
_arrowX = 100

class BackgroundView (NSView):

    def init(self):
        pass

    def drawRect_(self, rect):
        #print dir(self)
        print "drawing"
        contentRect = NSInsetRect(self.bounds(), LINE_THICKNESS, LINE_THICKNESS)
        path = NSBezierPath.bezierPath()
        path.moveToPoint_(NSMakePoint(_arrowX, NSMaxY(contentRect)))
        path.lineToPoint_(NSMakePoint(_arrowX + ARROW_WIDTH / 2, NSMaxY(contentRect) - ARROW_HEIGHT))
        path.lineToPoint_(NSMakePoint(NSMaxX(contentRect) - CORNER_RADIUS, NSMaxY(contentRect) - ARROW_HEIGHT))
        
        topRightCorner = NSMakePoint(NSMaxX(contentRect), NSMaxY(contentRect) - ARROW_HEIGHT)
        path.curveToPoint_controlPoint1_controlPoint2_(NSMakePoint(NSMaxX(contentRect), NSMaxY(contentRect) - ARROW_HEIGHT - CORNER_RADIUS), topRightCorner, topRightCorner)
        path.lineToPoint_(NSMakePoint(NSMaxX(contentRect), NSMinY(contentRect) + CORNER_RADIUS))

        bottomRigthCorner = NSMakePoint(NSMaxX(contentRect), NSMinY(contentRect))
        path.curveToPoint_controlPoint1_controlPoint2_(NSMakePoint(NSMaxX(contentRect) - CORNER_RADIUS, NSMinY(contentRect)), bottomRigthCorner, bottomRigthCorner)
        path.lineToPoint_(NSMakePoint(NSMinX(contentRect) + CORNER_RADIUS, NSMinY(contentRect)))
        path.curveToPoint_controlPoint1_controlPoint2_(NSMakePoint(NSMinX(contentRect), NSMinY(contentRect) + CORNER_RADIUS), contentRect.origin, contentRect.origin)
        path.lineToPoint_(NSMakePoint(NSMinX(contentRect), NSMaxY(contentRect) - ARROW_HEIGHT - CORNER_RADIUS))

        topLeftCorner = NSMakePoint(NSMinX(contentRect), NSMaxY(contentRect) - ARROW_HEIGHT)
        path.curveToPoint_controlPoint1_controlPoint2_(NSMakePoint(NSMinX(contentRect) + CORNER_RADIUS, NSMaxY(contentRect) - ARROW_HEIGHT), topLeftCorner, topLeftCorner)
        path.lineToPoint_(NSMakePoint(_arrowX - ARROW_WIDTH / 2, NSMaxY(contentRect) - ARROW_HEIGHT))
        path.closePath()

        NSColor.colorWithDeviceWhite_alpha_(1, FILL_OPACITY).setFill()
        path.fill()
