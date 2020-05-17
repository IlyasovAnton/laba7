import wx
import sys

from MyPanel import MyPanel


class MyFrame(wx.Frame):
    def __init__(self):
        self.size = (1005, 800)
        wx.Frame.__init__(self, None, title='3d object', size=self.size,
                          style=wx.DEFAULT_FRAME_STYLE | wx.FULL_REPAINT_ON_RESIZE)
        self.SetMinSize(self.size)
        self.SetMaxSize(self.size)
        self.SetBackgroundColour(wx.Colour(200, 200, 200))

        self.panel = MyPanel(self)

        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_close(self, event):
        self.Destroy()
        sys.exit(0)

