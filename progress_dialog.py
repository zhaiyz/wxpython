import wx

if __name__ == '__main__':
    app = wx.PySimpleApp()
    progressMax = 15
    dialog = wx.ProgressDialog("A progress box", "Time remaing", progressMax, 
        style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
    keepGoing = (True, True)
    count = 0
    while keepGoing[0] and count < progressMax:
        count = count + 1
        wx.Sleep(1)
        keepGoing = dialog.Update(count)
        print keepGoing[0]
    
    dialog.Destroy()
