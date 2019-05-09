#adding menuvars
import wx
class windowClass(wx.Frame):

    def __init__(self,*args,**kwargs):
        super(windowClass,self).__init__(*args,**kwargs)
        self.basicGUI()

        # self.Move((1080,250))
    def basicGUI(self):

        nameBox = wx.TextEntryDialog(None,'What is your name?','Welcome','Munesh')

        if nameBox.ShowModal()==wx.ID_OK:
            userName = nameBox.GetValue()



        # yes or no bx
        yesNoBox = wx.MessageDialog(None,'Do yo enjoy python','Question',wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()






        #creating a panel
        panel = wx.Panel(self)
        wx.TextCtrl(panel,pos = (3,100),size=(250,50))
        aweText = wx.StaticText(panel,-1,"awesome Text",(3,3))
        aweText.SetBackgroundColour("red")
        aweText.SetForegroundColour("Black")

        r1Awe = wx.StaticText(panel,-1,"customised",(3,20))
        r1Awe.SetForegroundColour("orange")
        r1Awe.SetBackgroundColour("Black")









        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        editButton = wx.Menu()
        exitItem = fileButton.Append(wx.ID_EXIT,'Exit','status mesa')

        menuBar.Append(fileButton,'&File')
        menuBar.Append(editButton,'Edit')
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU,self.Quit,exitItem)



#single choice box

        if yesNoAnswer == wx.ID_NO:
            userName = 'LOser!'


        chooseOneBox = wx.SingleChoiceDialog(None,"What is your favourite color?","COlor quesion",['Odin','Blue','Red'])

        if chooseOneBox.ShowModal() == wx.ID_OK:
            fav = chooseOneBox.GetStringSelection()






        self.SetTitle("Epic Window "+ userName)

        self.Show(True)





    def Quit(self,e):
        #could diplay a message
        self.Close()



app = wx.App()
windowClass(None,title = "WIndow")
app.MainLoop()