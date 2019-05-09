#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Thu Apr 11 19:05:45 2019
#

import wx

# begin wxGlade: dependencies
import gettext
import Departmentsql as Dsq

# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    x1 = 12987
    x2 = "name"
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_3 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_1 = wx.Button(self, wx.ID_ANY, _("button_1"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.getid, self.text_ctrl_2)
        self.Bind(wx.EVT_TEXT, self.Getname, self.text_ctrl_3)
        self.Bind(wx.EVT_BUTTON, self.Onclik, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("Department"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5.Add((0, 0), 0, 0, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, _("Dept_id"))
        sizer_6.Add(label_2, 1, 0, 0)
        sizer_6.Add(self.text_ctrl_2, 1, 0, 0)
        sizer_5.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_5.Add((0, 0), 0, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, _("Dept_name"))
        sizer_7.Add(label_3, 1, 0, 0)
        sizer_7.Add(self.text_ctrl_3, 1, 0, 0)
        sizer_5.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_5.Add(self.button_1, 0, 0, 0)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_4)
        self.Layout()
        # end wxGlade

    def getid(self, event):  # wxGlade: MyFrame.<event_handler>
        # print("Event handler 'getid' not implemented!")
        self.x1 = event.GetString()
        event.Skip()

    def Getname(self, event):  # wxGlade: MyFrame.<event_handler>
        # print("Event handler 'Getname' not implemented!")
        self.x2 = event.GetString()
        event.Skip()

    def Onclik(self, event):  # wxGlade: MyFrame.<event_handler>
        # print("Event handler 'Onclik' not implemented!")
        try:
            self.x1 = (int)(self.x1)
        except:
            self.inv_alidinput()


        if (self.x1<=0 or self.x1 == 12987) or self.x2 == "name" or (type)(self.x2)!=str:
            self.inv_alidinput()

        try:

            x12,lis_t1 = Dsq.getdaat(self.x1,self.x2)

        except:
            self.inv_alidinput()
        if x12==1:
            self.err_or(lis_t1)
        else:
            yesNoBox1 = wx.MessageDialog(None, "Added successfully", 'Question', wx.OK)
            yesNoAnswer1 = yesNoBox1.ShowModal()
            yesNoBox1.Destroy()
            self.Destroy()





        event.Skip()

    def err_or(self,lt):
        yesNoBox = wx.MessageDialog(None,
                                    'THE ID YOU ARE ENTERING IS NOT PRESENT IN BRANCH LIST ' + lt + '\nPRESS yes to try again and no to stop',
                                    'Question', wx.YES_NO)

        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()
        self.Destroy()
        initial()


    def inv_alidinput(self):
        yesNoBox = wx.MessageDialog(None, 'invalid input', 'Question', wx.OK)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()
        self.Destroy()
        initial()



# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

def initial():
    gettext.install("app") # replace with the appropriate catalog name

    app = MyApp(0)
    app.MainLoop()
initial()