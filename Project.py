import wx


#### Variables to be exported

path = '' ## Set directory
name = '' ## Name of the user
Cell = '' ## Type of cell
Data = '' ## Type of data
Time = [0,0] ## Time lapse


class MyFrame(wx.Frame):  ## 
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):

        ######## LAYOUT

        wx.Frame.__init__(self, parent, title= 'New App', size=( 700,500))
        panel = wx.Panel(self)

        ###### Static Boxes
        wx.StaticBox(panel, label='Personal Info', pos=(5, 5), size=(340, 230))
        wx.StaticBox(panel, label='Data Analysis', pos=(5, 245), size=(340, 230))
        wx.StaticBox(panel, label='Graph', pos=(350, 5), size=(340, 400))
        wx.StaticBox(panel, label='', pos=(350, 425), size=(340, 50))

        ###### Buttons
        
        ## Set Name 
        button1 = wx.Button(panel, label = 'Enter name', pos = (75,80), size= (150,30))
        self.Bind (wx.EVT_BUTTON, self.loadName, button1)
        # answer = box.GetValue()


        ## Set Directory
        button = wx.Button(panel, label = 'Set Directory', pos = (75,130), size= (150,30))
        self.Bind (wx.EVT_BUTTON, self.loadFile, button)
        # button = wx.Button(panel, label = 'Close', pos = (75,110), size= (150,30))
        
        ## Save Button
        button2 = wx.Button(panel, label = 'Get your Report', pos = (440,430), size= (150,30))

        ###### Check Boxes

        ## Set Cell Type
        self.typecell1 = wx.RadioButton(panel, -1, 'Yeast', (60, 320), style=wx.RB_GROUP)
        self.typecell2 = wx.RadioButton(panel, -1, 'Bacteria', (160, 320))

        self.Bind(wx.EVT_RADIOBUTTON, self.SetCell, id=self.typecell1.GetId())
        self.Bind(wx.EVT_RADIOBUTTON, self.SetCell, id=self.typecell2.GetId())
        
        self.SetCell(True)

        ## Set Data Type
        self.typedata1 = wx.RadioButton(panel, -1, 'Absorbance', (60, 370), style=wx.RB_GROUP)
        self.typedata2 = wx.RadioButton(panel, -1, 'Fluorescence', (160, 370))

        self.Bind(wx.EVT_RADIOBUTTON, self.SetData, id=self.typedata1.GetId())
        self.Bind(wx.EVT_RADIOBUTTON, self.SetData, id=self.typedata2.GetId())
        
        self.SetData(True)


        ###### Slider

        ## Time

        # time = wx.Slider(panel, value=200, minValue=1, maxValue=500, pos=(20, 170 ), 
        #     size=(250, -1), style=wx.SL_AUTOTICKS | wx.SL_LABELS)
        # time.SetTickFreq (5, 400 )
        
        # time.Bind(wx.EVT_SCROLL, self.TimeScroll)


        ###### SpinCtrl

        ## Time

        self.time1 = wx.SpinCtrl(panel, value='0', pos=(75, 430), size=(60, -1))
        self.time1.SetRange(-459, 1000)

        self.time2 = wx.SpinCtrl(panel, value='0', pos=(200, 430), size=(60, -1))
        self.time2.SetRange(-459, 1000)
        self.Bind (wx.EVT_BUTTON, self.SetTime, button2)
        
        wx.StaticText(panel, label='From: ', pos=(30, 435))
        wx.StaticText(panel, label='To: ', pos=(150, 435))
        


        ###### Quit the app
        self.Bind (wx.EVT_CLOSE, self.closewindow)
        
        


        self.Show(True)



        ######## FUNCTIONS

    
    def loadName(self, event):
        box = wx.TextEntryDialog(self, "What's your name?", 'title','')
        global name
        if box.ShowModal() == wx.ID_OK:
            name = box.GetValue()
            # print (name)
            # http://stackoverflow.com/questions/18532827/using-wxpython-to-get-input-from-user
        
    
    def loadFile(self, event):
        dlg = wx.FileDialog(self, "Choose a file", style = wx.OPEN, wildcard = "*.*")
        global path # seems to be neccesary to append the value after, otherwise the value does not change after the function is run.
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            #print (path)
    

    def SetCell(self, event):
        global Cell
        Yeast = str(self.typecell1.GetValue())
        Bacteria = str(self.typecell2.GetValue())
        # http://wiki.wxpython.org/AnotherTutorial#wx.RadioButton
        if Yeast == 'True':
            Cell = 'Yeast'
        else :
            Cell = 'Bacteria'
        #print (cell)


    def SetData(self, event):
        global Data
        Absorbance = str(self.typedata1.GetValue())
        Bacteria = str(self.typedata2.GetValue())
        # http://wiki.wxpython.org/AnotherTutorial#wx.RadioButton
        if Absorbance == 'True':
            Data = 'Absorbance'
        else :
            Data = 'Fluorescence'
        #print (Data)    




    # def TimeScroll(self, event):
    #     global Time
    #     obj = event.GetEventObject()
    #     Time = obj.GetValue()    


    def SetTime (self,event):
        # Time = (int(self.time1.GetValue(),int (self.time1.GetValue()))
        global Time
        Time[0] = int(self.time1.GetValue()) 
        Time[1] = int(self.time2.GetValue())
        # print (Time)

    def closewindow (self,event):
        self.Destroy()  


    





    

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, 'Small editor')
    app.MainLoop()


print (path)
print (name)
print (Cell)
print (Data)
print (Time)