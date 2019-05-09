#adding menuvars
import wx
class windowClass(wx.Frame):

    def __init__(self,*args,**kwargs):
        super(windowClass,self).__init__(*args,**kwargs)
        self.basicGUI()

        # self.Move((1080,250))
    def basicGUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)


        panel = wx.Panel(self)

        wx.TextCtrl(panel,pos = (500,60),size = (600,30))

        self.btn = wx.Button(panel, -1, "Add munesh",pos = (1150,70))

        vbox.Add(self.btn, 0, wx.ALIGN_CENTER)
        self.btn.Bind(wx.EVT_BUTTON, self.OnClicked)




        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        exitItem = fileButton.Append(wx.ID_EXIT,'Exit','status mesa')

        menuBar.Append(fileButton,'&File')
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU,self.Quit,exitItem)

        self.SetTitle("Employees")

        self.Show(True)

    def Quit(self,e):
        yesNoBox = wx.MessageDialog(None,'Did you enjoy python','Question',wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()

        #could diplay a message
        self.Close()
    def OnClicked(self, event):
        btn = event.GetEventObject().GetLabel()
        print("Label of pressed button = ", btn)



app = wx.App()
windowClass(None,title = "WIndow")
app.MainLoop()