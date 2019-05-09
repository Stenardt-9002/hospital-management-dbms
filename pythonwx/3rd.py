#adding menuvars
import wx
class windowClass(wx.Frame):

    def __init__(self,*args,**kwargs):
        super(windowClass,self).__init__(*args,**kwargs)
        self.basicGUI()

        # self.Move((1080,250))
    def basicGUI(self):
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        exitItem = fileButton.Append(wx.ID_EXIT,'Exit','status mesa')

        menuBar.Append(fileButton,'&File')
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU,self.Quit,exitItem)

        self.SetTitle("Epic Window")

        self.Show(True)

    def Quit(self,e):
        #could diplay a message
        self.Close()



app = wx.App()
windowClass(None,title = "WIndow")
app.MainLoop()