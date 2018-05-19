# -*- coding: utf-8 -*-
"""
Created on Wed May 16 23:47:47 2018

@author: user
"""

import wx

class Example(wx.Frame):
    
    def __init__(self,parent,title):
        super(Example,self).__init__(parent, title=title, size=(350,250))
        
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        helMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        fileMenu.Append(wx.ID_ANY,'Hello')
        menubar.Append(fileMenu, '&File')
        menubar.Append(helMenu,'&Hel')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        self.SetSize((300, 200))
        self.SetTitle('Simple menu')
        self.Centre()

    def OnQuit(self, e):
        self.Close()
        
def main():
    app = wx.App()
    
    frame = Example(None, title='Sizing')
    frame.Show()
    
    app.MainLoop()

if __name__=='__main__':
    main()
