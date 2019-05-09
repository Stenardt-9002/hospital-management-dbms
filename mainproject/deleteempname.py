import wx
import deleteempnamesql


class Mywin(wx.Frame):

    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(650, 600))

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)

        self.text = wx.TextCtrl(panel, style=wx.TE_MULTILINE)


        name1, las, em_id, Gen, b_id, d_id = deleteempnamesql.getdaat()
        name = []
        print(name)
        if name1 == []:
            self.rror()
        for i in range(len(name1)):
            x = name1[i]+"," +las[i]
            name.append(x)


        lst = wx.ListBox(panel, size=(200, -1), choices=name, style=wx.LB_SINGLE)
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

            deleteempnamesql.delete(event.GetEventObject().GetStringSelection())
            yesNoBox1 = wx.MessageDialog(None, "Successful deleted "+ event.GetEventObject().GetStringSelection(), 'Notification', wx.OK)
            yesNoAnswer1 = yesNoBox1.ShowModal()
            yesNoBox1.Destroy()
            self.Destroy()
            # pass
            

        elif yesNoAnswer == wx.ID_NO:
            print("USE dare?")


    def rror(self):
        yesNoBox = wx.MessageDialog(None,'List is Empty','Empty', wx.OK)

        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()
        self.Destroy()





def initislise():

    ex = wx.App()
    Mywin(None, 'Delete Employee by Name')
    ex.MainLoop()


# initislise()