#!/usr/bin/python
# -*- encoding: utf-8

""" A demo to illustrate event handler search and execution hierarchy. """
import sys, os
import wx

#------------------------------------------------------------------------------

class MainFrame( wx.Frame ) :

    def __init__( self, title='Event Handler Hierarchy', pos=(10, 10), size=(350, 200) ) :

        wx.Frame.__init__( self, None, id=-1, title=title, pos=pos, size=size )

        #----- Frame's controls:

        # An initial Frame panel is needed for tab-traversal
        #   and platform background color capabilities.
        # The first control instantiated in a Frame automatically expands
        #   to the extent of the Frame's client area.  This is unique to Frames.
        frm_pnl = wx.Panel( self )

        btn1 = wx.Button( frm_pnl, label='Btn1' )
        btn2 = wx.Button( frm_pnl, label='Btn2' )

        #----- Button centering:

        # Automatically center the button position as simply as possible.
        pnl_horzSizer = wx.BoxSizer( wx.HORIZONTAL )
        pnl_horzSizer.AddStretchSpacer()
        pnl_horzSizer.Add( btn1, flag=wx.ALIGN_CENTER )  # Center horizontally.
        pnl_horzSizer.Add( btn2, flag=wx.ALIGN_CENTER )  # Center horizontally.
        pnl_horzSizer.AddStretchSpacer()    # 2# StretchSpacers assure btn's vertical centering.

        frm_pnl.SetSizer( pnl_horzSizer )
        frm_pnl.Layout()

        #----- Buttons' click event handlers:

        ## Comment out or un-comment these handler bindings
        #   to see the effects of each remaining combination.

        #-----

        # Bind the button-to-Frame handler.
        # The 3rd argument specifies which button's events to handle.
        self.Bind( wx.EVT_BUTTON, self.OnButton_FrameHandler, btn1 )

        ## Bind both button's events because there is no 3rd argument.
        #self.Bind( wx.EVT_BUTTON, self.OnButton_FrameHandler )

        #-----

        # Bind the button-to-Panel handler.
        frm_pnl.Bind( wx.EVT_BUTTON, self.OnButton_PanelHandler, btn1 )

        ## Bind both button's events because there is no 3rd argument.
        #frm_pnl.Bind( wx.EVT_BUTTON, self.OnButton_PanelHandler )

        #-----

        # Bind the button's own handler. No 3rd argument is necessary because "btn1.Bind".
        btn1.Bind( wx.EVT_BUTTON, self.OnButton_ButtonHandler )

    #end __init__

    #------------------------

    def OnButton_FrameHandler( self, event ) :
        # The button that generated this event:
        btn = event.GetEventObject()
        print '\n----  OnButton_FrameHandler() for', btn.GetLabelText()

        # There is nowhere to .Skip() up to.
    #end def

    def OnButton_PanelHandler( self, event ) :
        # The button that generated this event:
        btn = event.GetEventObject()
        print '\n----  OnButton_PanelHandler() for', btn.GetLabelText()

        event.Skip()    # Search for handler upwards in the child-parent hierarchy tree.
    #end def

    def OnButton_ButtonHandler( self, event ) :
        # The button that generated this event:
        btn = event.GetEventObject()
        print '\n----  OnButton_ButtonHandler() for', btn.GetLabelText()

        event.Skip()    # Search for handler upwards in the child-parent hierarchy tree.
    #end def

#end class
if __name__ == '__main__' :
    app = wx.PySimpleApp( redirect=False )
    appFrame = MainFrame().Show()
    app.MainLoop()
#end def