import wx

if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = wx.DirDialog(None, "Choose a directory", 
        style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
    if dlg.ShowModal() == wx.ID_OK:
        print dlg.GetPath()
    
    dlg.Destroy()
