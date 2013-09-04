import wx

if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = wx.FontDialog(None, wx.FontData())
    if dlg.ShowModal() == wx.ID_OK:
        data = dlg.GetFontData()
        font = data.GetChosenFont()
        colour = data.GetColour()
        print 'You selected:"%s", %d points\n' % (
            font.GetFaceName(), font.GetPointSize())
            
        dlg.Destroy()
