import wx

if __name__ == '__main__':
    app = wx.PySimpleApp()
    
    dlg = wx.MessageDialog(None, "Is this explanation OK?", 'A Message Box', wx.YES_NO | wx.ICON_QUESTION)
    retCode = dlg.ShowModal()
    if (retCode == wx.ID_YES):
        print "YES"
    else:
        print "NO"
    dlg.Destroy()
