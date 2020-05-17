import wx

from OpenGLCanvas import OpenGlCanvas


class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.OrthoFrustBox = wx.RadioBox(self, -1, pos=(820, 10), choices=['frust', 'ortho'], style=wx.RA_SPECIFY_ROWS)
        self.CamLightBox = wx.RadioBox(self, -1, pos=(900, 10), choices=['light', 'camera'], style=wx.RA_SPECIFY_ROWS)
        self.CamLightBox.SetSelection(1)

        ################################################################################################################
        self.label = wx.StaticText(self, -1, 'фоновое излучение источника', pos=(810, 80))

        self.ambientRslider = wx.Slider(self, -1, pos=(810, 100), size=(140, 25),
                                        value=40, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL)
        self.ambientGslider = wx.Slider(self, -1, pos=(810, 125), size=(140, 25),
                                        value=0, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL)
        self.ambientBslider = wx.Slider(self, -1, pos=(810, 150), size=(140, 25),
                                        value=0, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL)
        self.ambientAslider = wx.Slider(self, -1, pos=(810, 175), size=(140, 25),
                                        value=0, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL)
        self.label = wx.StaticText(self, -1, 'R', pos=(955, 100))
        self.label = wx.StaticText(self, -1, 'G', pos=(955, 125))
        self.label = wx.StaticText(self, -1, 'B', pos=(955, 150))
        self.label = wx.StaticText(self, -1, 'A', pos=(955, 175))

        ################################################################################################################
        self.label = wx.StaticText(self, -1, 'Интенсивность сцены', pos=(830, 230))

        self.modelRslider = wx.Slider(self, -1, pos=(810, 250), size=(140, 25),
                                      value=80, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL)
        self.modelGslider = wx.Slider(self, -1, pos=(810, 275), size=(140, 25),
                                      value=0, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL)
        self.modelBslider = wx.Slider(self, -1, pos=(810, 300), size=(140, 25),
                                      value=20, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL)
        self.modelAslider = wx.Slider(self, -1, pos=(810, 325), size=(140, 25),
                                      value=0, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL)
        self.label = wx.StaticText(self, -1, 'R', pos=(955, 250))
        self.label = wx.StaticText(self, -1, 'G', pos=(955, 275))
        self.label = wx.StaticText(self, -1, 'B', pos=(955, 300))
        self.label = wx.StaticText(self, -1, 'A', pos=(955, 325))

        ################################################################################################################
        self.label = wx.StaticText(self, -1, 'цвет рассеянного', pos=(840, 380))
        self.label = wx.StaticText(self, -1, 'отражения материала', pos=(830, 400))

        self.difuseRslider = wx.Slider(self, -1, pos=(810, 420), size=(140, 25),
                                       value=50, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL)
        self.difuseGslider = wx.Slider(self, -1, pos=(810, 445), size=(140, 25),
                                       value=90, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL)
        self.difuseBslider = wx.Slider(self, -1, pos=(810, 470), size=(140, 25),
                                       value=50, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL)
        self.difuseAslider = wx.Slider(self, -1, pos=(810, 495), size=(140, 25),
                                       value=100, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL)
        self.label = wx.StaticText(self, -1, 'R', pos=(955, 420))
        self.label = wx.StaticText(self, -1, 'G', pos=(955, 445))
        self.label = wx.StaticText(self, -1, 'B', pos=(955, 470))
        self.label = wx.StaticText(self, -1, 'A', pos=(955, 495))

        ################################################################################################################
        self.label = wx.StaticText(self, -1, 'степень отражения', pos=(835, 550))

        self.shininessSlider = wx.Slider(self, -1, pos=(820, 570), size=(140, 25),
                                         value=10, minValue=0, maxValue=90, style=wx.SL_HORIZONTAL)

        ################################################################################################################
        self.canvas = OpenGlCanvas(self)

        self.Bind(wx.EVT_RADIOBOX, self.SetOrthoFrust, self.OrthoFrustBox)
        self.Bind(wx.EVT_RADIOBOX, self.SetCamLight, self.CamLightBox)

        self.Bind(wx.EVT_SLIDER, self.ambientR, self.ambientRslider)
        self.Bind(wx.EVT_SLIDER, self.ambientG, self.ambientGslider)
        self.Bind(wx.EVT_SLIDER, self.ambientB, self.ambientBslider)
        self.Bind(wx.EVT_SLIDER, self.ambientA, self.ambientAslider)

        self.Bind(wx.EVT_SLIDER, self.modelR, self.modelRslider)
        self.Bind(wx.EVT_SLIDER, self.modelG, self.modelGslider)
        self.Bind(wx.EVT_SLIDER, self.modelB, self.modelBslider)
        self.Bind(wx.EVT_SLIDER, self.modelA, self.modelAslider)

        self.Bind(wx.EVT_SLIDER, self.difuseR, self.difuseRslider)
        self.Bind(wx.EVT_SLIDER, self.difuseG, self.difuseGslider)
        self.Bind(wx.EVT_SLIDER, self.difuseB, self.difuseBslider)
        self.Bind(wx.EVT_SLIDER, self.difuseA, self.difuseAslider)

        self.Bind(wx.EVT_SLIDER, self.shininess, self.shininessSlider)

    def SetOrthoFrust(self, event):
        self.canvas.ortho = self.OrthoFrustBox.GetSelection()
        self.canvas.Refresh()

    def SetCamLight(self, event):
        self.canvas.camera = self.CamLightBox.GetSelection()
        self.canvas.Refresh()

    def ambientR(self, event):
        self.canvas.ambientR = self.ambientRslider.GetValue() / 100
        self.canvas.Refresh()

    def ambientG(self, event):
        self.canvas.ambientG = self.ambientGslider.GetValue() / 100
        self.canvas.Refresh()

    def ambientB(self, event):
        self.canvas.ambientB = self.ambientBslider.GetValue() / 100
        self.canvas.Refresh()

    def ambientA(self, event):
        self.canvas.ambientR = self.ambientAslider.GetValue() / 100
        self.canvas.Refresh()

    def modelR(self, event):
        self.canvas.lightModelR = self.modelRslider.GetValue() / 100
        self.canvas.Refresh()

    def modelG(self, event):
        self.canvas.lightModelG = self.modelGslider.GetValue() / 100
        self.canvas.Refresh()

    def modelB(self, event):
        self.canvas.lightModelB = self.modelBslider.GetValue() / 100
        self.canvas.Refresh()

    def modelA(self, event):
        self.canvas.lightModelA = self.modelAslider.GetValue() / 100
        self.canvas.Refresh()

    def difuseR(self, event):
        self.canvas.difuseR = self.difuseRslider.GetValue() / 100
        self.canvas.Refresh()

    def difuseG(self, event):
        self.canvas.difuseG = self.difuseGslider.GetValue() / 100
        self.canvas.Refresh()

    def difuseB(self, event):
        self.canvas.difuseB = self.difuseBslider.GetValue() / 100
        self.canvas.Refresh()

    def difuseA(self, event):
        self.canvas.difuseA = self.difuseAslider.GetValue() / 100
        self.canvas.Refresh()

    def shininess(self, event):
        self.canvas.shininess = self.shininessSlider.GetValue()
        self.canvas.Refresh()
