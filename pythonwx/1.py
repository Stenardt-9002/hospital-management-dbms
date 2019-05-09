import wx
import pdb
# app = wx.App()

# frame = wx.Frame(None,-1,'Window Title',style = wx.MAXIMIZE_BOX | wx.SYSTEM_M| wx.CAPTION)
# frame.show()
# app.MainLoop()

# window = wx.Frame(None, title = "wxPython Frame", size = (300,200))
# panel = wx.Panel(window)
# label = wx.StaticText(panel, label = "Hello World", pos = (100,50))
# window.Show(True)
# app.MainLoop()
# input()
# exit()

class windowClass(wx.Frame):

    def __init__(self,parent ,title):
        super(windowClass,self).__init__(parent,title = title ,size = (1920,1080))

        # self.Move(80,250) # x ,y coorrdinates of table
        # self.Show()
        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)
        menuBar = wx.MenuBar()


        editButton = wx.Menu()





#3
        # menuBar = wx.MenuBar()

        fileButton = wx.Menu()

        exitItem = fileButton.Append(wx.ID_EXIT,'Exit',' status msg') # no status bar

        menuBar.Append(fileButton, '&File')
        menuBar.Append(editButton, 'Edit')
        #button
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU,self.Quit,exitItem)






        # 5

        nameBox = wx.TextEntryDialog(None,"what is your name?",'Welcome','name')
        if nameBox.ShowModal() == wx.ID_OK:
            userName = nameBox.GetValue()


        yesNoBox = wx.MessageDialog(None,'Do you like to shit poop','Question',wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()

        yesNoBox.Destroy()






        wx.TextCtrl(panel, pos=(10,10),size = (250,150))

        #check for answer
        if yesNoAnswer == wx.ID_NO:
            userName = "non python lover"



        #6
        chooseOneBox = wx.SingleChoiceDialog(None,"What is favourite food ?",'color question',['Pizza', 'Burger', 'Chowmein', 'Pasta'])

        if chooseOneBox.ShowModal() == wx.ID_OK:
            favFood = chooseOneBox.GetStringSelection()



        #7
        wx.TextCtrl(panel, pos=(30,100),size = (150,50))
        aweText = wx.StaticText(panel,-1,"Awesome is the text",(5,190))
        aweText.SetForegroundColour('yellow')
        aweText.SetBackgroundColour('red'   )





        self.SetTitle('Epic windows for '+userName)

        self.Show(True)

    def Quit(self,e):

        self.Close()
# file and eixt


app = wx.App()
windowClass(None,title = "Hela biatches")
app.MainLoop()








#
# if __name__ == '__main__':
#     app = wx.App()
#     windowClass(None,title = "Hela biatches")
#     app.MainLoop()
# table done now menu

