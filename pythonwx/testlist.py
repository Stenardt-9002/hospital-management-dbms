import wx
import sqltest

class Mywin(wx.Frame):

    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(350, 300))

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)

        self.text = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        # languages = ['C', 'C++', 'Java', 'Python', 'Perl', 'JavaScript', 'PHP', 'VB.NET', 'C#']
        name,las,em_id,Gen,b_id,d_id = sqltest.getdaat()
        lst = wx.ListBox(panel, size=(100, -1), choices=em_id, style=wx.LB_SINGLE)
        # lst1 = wx.ListBox(panel, size=(100, -1), choices=las, style=wx.LB_SINGLE)

        box.Add(lst, 0, wx.EXPAND)
        box.Add(self.text, 1, wx.EXPAND)

        panel.SetSizer(box)
        panel.Fit()

        self.Centre()
        self.Bind(wx.EVT_LISTBOX, self.onListBox, lst)
        self.Show(True)

    def onListBox(self, event):

        self.text.AppendText("Current selection:      "+event.GetEventObject().GetStringSelection()+"\n  ")

    def onclik(self,event):
        pass



ex = wx.App()
Mywin(None, 'ListBox Demo')
ex.MainLoop()