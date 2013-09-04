import wx
import wx.lib.imagebrowser as imagebrowser

if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = imagebrowser.ImageDialog(None)
    if dlg.ShowModal() == wx.ID_OK:
        print 'You selected:%s' % dlg.GetFile()
        
    dlg.Destroy()
