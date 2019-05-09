import wx
import DeleteDepsql


class Mywin(wx.Frame):

    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(650, 600))

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)

        self.text = wx.TextCtrl(panel, style=wx.TE_MULTILINE)


        d_id ,name= DeleteDepsql.getdaat()
        if d_id == []:
            self.rror()

        x13 = []
        for i in range(len(d_id)):
            x11 = (str)(d_id[i])
            x11 = x11+","+name[i]
            x13.append(x11)
        lst = wx.ListBox(panel, size=(200, -1), choices=x13, style=wx.LB_SINGLE)
        # lst1 = wx.ListBox(panel, size=(100, -1), choices=las, style=wx.LB_SINGLE)

        box.Add(lst, 0, wx.EXPAND)
        box.Add(self.text, 1, wx.EXPAND)

        panel.SetSizer(box)
        panel.Fit()

        self.Centre()
        self.Bind(wx.EVT_LISTBOX, self.onListBox, lst)
        self.Show(True)

    def onListBox(self, event):
        self.text.AppendText("Selected id:      " + event.GetEventObject().GetStringSelection() + "\n  ")
        yesNoBox = wx.MessageDialog(None, 'Do you want Delete this is id?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()
        # print(yesNoAnswer)
        if yesNoAnswer == wx.ID_YES:
            DeleteDepsql.delete(event.GetEventObject().GetStringSelection())

            yesNoBox1 = wx.MessageDialog(None, "Successful deleted " + event.GetEventObject().GetStringSelection(),   'Notification', wx.OK)
            yesNoAnswer1 = yesNoBox1.ShowModal()
            yesNoBox1.Destroy()

            self.Destroy()
            # pass
            # print("Hella bitches")

        elif yesNoAnswer == wx.ID_NO:
            print("USE dare?")


    def rror(self):
        yesNoBox = wx.MessageDialog(None,'List is Empty','Empty', wx.OK)

        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()
        self.Destroy()





def initislise():

    ex = wx.App()
    Mywin(None, 'Delete Department')
    ex.MainLoop()

# initislise()