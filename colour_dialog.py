import wx

if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = wx.ColourDialog(None)
    dlg.GetColourData().SetChooseFull(True)
    if dlg.ShowModal() == wx.ID_OK:
        data = dlg.GetColourData()
        print 'You selected: %s\n' % str(data.GetColour().Get())
        
    dlg.Destroy()
