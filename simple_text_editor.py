import wx
import os

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, -1))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()
        
        filemenu = wx.Menu()
        
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", " Open a file")
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        
        filemenu.AppendSeparator()
        
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
                
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)
        
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0, 6):
            self.buttons.append(wx.Button(self, -1, "Button &" + str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)
            
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)
        
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        
        self.Show(True)
        
    def OnOpen(self, event):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()
        
    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "A small text editor", "About Smaple Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnExit(self, event):
        self.Close(True)
        
app = wx.App(False)
frmae = MyFrame(None, 'Small editor')
app.MainLoop()
