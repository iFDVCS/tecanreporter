import wx


#### Variables to be exported

path = '' ## Set directory
Name = '' ## Name of the user
Cell = '' ## Type of cell
Data = '' ## Type of data
Time = [0,0] ## Time lapse
Strain = ''
listcolumns1 = ['Column','1','2','3','4','5','6','7','8','9','10','11','12']
listcolumns2 = ['Column']
listrows1 = ['Row','A','B','C','D','E','F','G','H']
listrows2 = ['Row']


class MyFrame(wx.Frame):  ## 
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):

        ### The code is divided in two big parts. One related to the layout of the widgets
        ### and the other containing all the functions associatated to the widgets.

        #################### LAYOUT ------------------------------------------------

        wx.Frame.__init__(self, parent, title= 'New App', size=( 700,500))
        panel = wx.Panel(self)

        ###### Static Text --------------------
        ## Name
        wx.StaticText(panel, label="- What's your name?", pos=(20, 30))

        ## Directory
        wx.StaticText(panel, label="- Chose file to analyse: ", pos=(20, 100))
        wx.StaticText(panel, label="Chosen file must be either excel file or .csv file", pos=(20, 170))

        ## Type of cell
        wx.StaticText(panel, label="- What kind of cell are you using?", pos=(370, 30))
        wx.StaticText(panel, label="Strain: ", pos=(550, 55))


        ## Type of data
        wx.StaticText(panel, label="- What kind of method are you using?", pos=(370, 90))

        ## Time lapse
        wx.StaticText(panel, label="- Set the time lapse you want to analyse: ", pos=(370, 170))
        wx.StaticText(panel, label='From: ', pos=(370, 210))
        wx.StaticText(panel, label='To: ', pos=(490, 210))

        ## Wells Selection
        wx.StaticText(panel, label="- Select the wells you want to analyse: ", pos=(370, 260))
        wx.StaticText(panel, label="- Select columns: ", pos=(420, 280))
        wx.StaticText(panel, label='From: ', pos=(400, 305))
        wx.StaticText(panel, label='To: ', pos=(570, 305))

        wx.StaticText(panel, label="- Select rows ", pos=(420, 340))
        wx.StaticText(panel, label='From: ', pos=(400, 363))
        wx.StaticText(panel, label='To: ', pos=(570, 363))

        ## Color Graphs
        wx.StaticText(panel, label="- Select color for the graph: ", pos=(20, 280))


        ## Labels Graphs
        wx.StaticText(panel, label="- Label for the graphs: ", pos=(20, 380))





        ###### Entry boxes ----------------------
        ## Name
        self.editname = wx.TextCtrl(panel, value="", pos=(80, 60), size=(200,-1))

        ## Directory
        self.editpath = wx.TextCtrl(panel, value="", pos=(15, 130), size=(180,-1))

        ## Strain
        self.setstrain = wx.TextCtrl(panel, value="", pos=(600, 53), size=(80,-1))






        ###### Static Boxes -----------------------
        wx.StaticBox(panel, label='Personal Info', pos=(5, 5), size=(340, 230))
        wx.StaticBox(panel, label='Graph', pos=(5, 245), size=(340, 230))
        wx.StaticBox(panel, label='Data Analysis', pos=(350, 5), size=(340, 400))
        wx.StaticBox(panel, label='', pos=(350, 425), size=(340, 50))






        ###### Combo boxes -------------------------

        ## Columns

        listcolumns1 = ['Column','1','2','3','4','5','6','7','8','9','10','11','12']
        column1 = wx.ComboBox(panel, pos=(450, 300),size = (70,-1), choices=listcolumns1, style=wx.CB_READONLY)
        listcolumns2 = ['Column']
        column2 = wx.ComboBox(panel, pos=(600, 300),size = (70,-1), choices=listcolumns2, style=wx.CB_READONLY)
        
        column1.Bind(wx.EVT_COMBOBOX, self.OnSelectColumns1)
        column2.Bind(wx.EVT_COMBOBOX, self.OnSelectColumns2)
        # # wx.StaticText(panel, label="- Select rows ", pos=(420, 260))


        ## Rows
        listrows1 = ['Row','A','B','C','D','E','F','G','H']
        row1 = wx.ComboBox(panel, pos=(450, 360),size = (70,-1), choices=listrows1, style=wx.CB_READONLY)
        listrows2 = ['Row']
        row2 = wx.ComboBox(panel, pos=(600, 360),size = (70,-1), choices=listrows2, style=wx.CB_READONLY)
        
        row1.Bind(wx.EVT_COMBOBOX, self.OnSelectRows1)
        # row2.Bind(wx.EVT_COMBOBOX, self.OnSelectRows2)


        ## Colors
        listcolors = ['Colors','Red','Green','Yellow','Orange']
        colorbox = wx.ComboBox(panel, pos=(120, 330), choices=listcolors, style=wx.CB_READONLY)

        colorbox.Bind(wx.EVT_COMBOBOX, self.GetColor)





        ###### Buttons -----------------------------

        ## Set Directory
        button = wx.Button(panel, label = 'Browse', pos = (215,121), size= (100,30))
        self.Bind (wx.EVT_BUTTON, self.loadFile, button)

        
        ## Get Report Button
        button2 = wx.Button(panel, label = 'Get your Report', pos = (440,430), size= (150,30))
        self.Bind (wx.EVT_BUTTON, self.GetReport, button2)
       


        ###### Check Boxes ---------------------------

        ## Set Cell Type
        self.typecell1 = wx.RadioButton(panel, -1, 'Yeast', (370, 55), style=wx.RB_GROUP)
        self.typecell2 = wx.RadioButton(panel, -1, 'Bacteria', (450, 55))

        self.Bind(wx.EVT_RADIOBUTTON, self.SetCell, id=self.typecell1.GetId())
        self.Bind(wx.EVT_RADIOBUTTON, self.SetCell, id=self.typecell2.GetId())
        
        self.SetCell(True)

        ## Set Data Type
        self.typedata1 = wx.RadioButton(panel, -1, 'Absorbance', (370, 115), style=wx.RB_GROUP)
        self.typedata2 = wx.RadioButton(panel, -1, 'Fluorescence', (500, 115))

        self.Bind(wx.EVT_RADIOBUTTON, self.SetData, id=self.typedata1.GetId())
        self.Bind(wx.EVT_RADIOBUTTON, self.SetData, id=self.typedata2.GetId())
        
        self.SetData(True)

        ## Labels
        self.graphlabel1 = wx.RadioButton(panel, -1, 'Show', (70, 420), style=wx.RB_GROUP)
        self.graphlabel2 = wx.RadioButton(panel, -1, 'Do not show', (150, 420))

        self.Bind(wx.EVT_RADIOBUTTON, self.SetLabels, id=self.graphlabel1.GetId())
        self.Bind(wx.EVT_RADIOBUTTON, self.SetLabels, id=self.graphlabel2.GetId())
        
        self.SetLabels(True)


        ###### SpinCtrl ----------------------------------

        ## Time

        self.time1 = wx.SpinCtrl(panel, value='0', pos=(410, 207), size=(60, -1))
        self.time1.SetRange(-459, 1000)

        self.time2 = wx.SpinCtrl(panel, value='0', pos=(530, 207), size=(60, -1))
        self.time2.SetRange(-459, 1000)
        



        ###### Quit the app --------------------------------
        self.Bind (wx.EVT_CLOSE, self.closewindow)
        
        


        self.Show(True)



        ######## FUNCTIONS ----------------------------------------------------------
    
    def loadFile(self, event):
        dlg = wx.FileDialog(self, "Choose a file", style = wx.OPEN, wildcard = "*.*")
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.editpath.SetValue(path)
            print path
        return (path)
    

    def SetCell(self, event):
        # global Cell
        Yeast = str(self.typecell1.GetValue())
        Bacteria = str(self.typecell2.GetValue())
        # http://wiki.wxpython.org/AnotherTutorial#wx.RadioButton
        if Yeast == 'True':
            Cell = 'Yeast'
        else :
            Cell = 'Bacteria'
        #print (cell)


    def SetData(self, event):
        Absorbance = str(self.typedata1.GetValue())
        Bacteria = str(self.typedata2.GetValue())
        if Absorbance == 'True':
            Data = 'Absorbance'
        else :
            Data = 'Fluorescence'
        #print (Data)      

    def SetLabels (self,event):
        Show = str(self.graphlabel1.GetValue())
        Donotshow = str(self.graphlabel1.GetValue())
        if Show == 'True':
            Label = 'Show'
        else :
            Label = 'Do not Show'
        print Label


    
    def OnSelectColumns1(panel, event):
        listcolumns2 = [''] # needed to refresh the list each time the function is run.
        ## i = row selected
        i = event.GetString()
        global columns
        columns = [int(i)]
        ## x is the index of the number selected
        x = listcolumns1.index(i)
        ## this way i append the possible rows selestred from the "to: " list to this list
        for index in range((x+1),13):
            listcolumns2.append(listcolumns1[index])
        listcolumns2.pop(0)
        column2 = wx.ComboBox(panel, pos=(600, 300),size = (70,-1), choices=listcolumns2, style=wx.CB_READONLY)
        # print listcolumns2
        # print columns

    def OnSelectColumns2(panel, event):
        j = event.GetString()
        columns = [int(j)]
        # print columns



    def OnSelectRows1(panel, event):
        listrows2 = [''] 
        k = event.GetString()
        columns = [str(k)]
        z = listrows1.index(k)
        for indec in range((z+1),9):
            listrows2.append(listrows1[indec])
        listrows2.pop(0)
        row2 = wx.ComboBox(panel, pos=(600, 360),size = (70,-1), choices=listrows2, style=wx.CB_READONLY)


    def GetColor(panel,event):
        color = event.GetString()
        # print color
        return color



    def GetReport (self,event):
        # Time = (int(self.time1.GetValue(),int (self.time1.GetValue()))
        # global Time
        Time[0] = int(self.time1.GetValue()) 
        Time[1] = int(self.time2.GetValue()) 
        print (Time)

        # global Name
        Name = str(self.editname.GetValue()) 
        print Name

        # global Strain
        Strain = str(self.setstrain.GetValue())
        print Strain




    def closewindow (self,event):
        self.Destroy()  






if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, 'Small editor')
    app.MainLoop()
