import wx
import fileub

class windowClass(wx.Frame):

    def __init__(self,parent,title):
        super(windowClass,self).__init__(parent,title = title,size = (1920,1080))
        # self.Move((1080,250))
        self.Show()

app = wx.App()
windowClass(None,title = "WIndow")
app.MainLoop()
fileub.test()