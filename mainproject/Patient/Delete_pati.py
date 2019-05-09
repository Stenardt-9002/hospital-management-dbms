import wx
import DeletePasql


class Mywin(wx.Frame):

    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(450, 300))

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)

        self.text = wx.TextCtrl(panel, style=wx.TE_MULTILINE)


        p_id ,name = DeletePasql.getdaat()
        if p_id == []:
            print("reached")
            self.rror()

        x13 = []
        for i in range(len(p_id)):
            x11 = (str)(p_id[i])
            x11 = x11+","+name[i]
            x13.append(x11)
        lst = wx.ListBox(panel, size=(100, -1), choices=x13, style=wx.LB_SINGLE)
        # lst1 = wx.ListBox(panel, size=(100, -1), choices=las, style=wx.LB_SINGLE)

        box.Add(lst, 0, wx.EXPAND)
        box.Add(self.text, 1, wx.EXPAND)

        panel.SetSizer(box)
        panel.Fit()

        self.Centre()
        self.Bind(wx.EVT_LISTBOX, self.onListBox, lst)
        self.Show(True)

    def onListBox(self, event):
        self.text.AppendText("Selected Patient:      " + event.GetEventObject().GetStringSelection() + "\n  ")
        yesNoBox = wx.MessageDialog(None, 'Do you want Delete this is id?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()
        # print(yesNoAnswer)
        if yesNoAnswer == wx.ID_YES:

            yesNoBox1 = wx.MessageDialog(None, "Successful deleted " + event.GetEventObject().GetStringSelection(),   'Notification', wx.OK)
            yesNoAnswer1 = yesNoBox1.ShowModal()
            yesNoBox1.Destroy()
            DeletePasql.delete(event.GetEventObject().GetStringSelection())
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
    Mywin(None, 'Delete Patient ')
    ex.MainLoop()

initislise()