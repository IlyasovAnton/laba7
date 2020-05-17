import wx
from wx import glcanvas
from OpenGL.GLU import *

from Figures import *


class OpenGlCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        self.size = (800, 800)
        glcanvas.GLCanvas.__init__(self, parent, -1, size=self.size)
        self.context = glcanvas.GLContext(self)
        self.SetCurrent(self.context)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        self.ortho = False
        self.camera = True

        self.camDistanse = 2
        self.lightDistanse = 2

        self.cameraAng1 = 0
        self.cameraAng2 = 0

        self.lightAng1 = 0
        self.lightAng2 = 0

        self.shininess = 10.0

        self.lightX = 0.0
        self.lightY = 1.0
        self.lightZ = 2.0

        self.lightDirX = 0.0
        self.lightDirY = -1.0
        self.lightDirZ = -1.0

        self.ambientR = 0.4
        self.ambientG = 0.0
        self.ambientB = 0.0
        self.ambientA = 0.0

        self.lightModelR = 0.8
        self.lightModelG = 0.0
        self.lightModelB = 0.2
        self.lightModelA = 0.0

        self.difuseR = 0.5
        self.difuseG = 0.9
        self.difuseB = 0.5
        self.difuseA = 1.0

        self.figure = Figure(0.2, 0.25, 0.3, 0.05, 0.1, 0.04, 50)

        self.Bind(wx.EVT_PAINT, self.OnDraw)
        self.Bind(wx.EVT_MOTION, self.move_camera)
        self.Bind(wx.EVT_MOUSEWHEEL, self.set_distanse)

    def OnDraw(self, event):
        glShadeModel(GL_FLAT)

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        self.draw()
        self.SwapBuffers()

    def draw(self):
        if not self.ortho:
            gluPerspective(45.0, 1, 0.5, 10.0)
        else:
            glOrtho(-1, 1, -1, 1, 0.5, 10.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        camera = rotate([-1.0, 0.5, 1.0], self.cameraAng1, self.cameraAng2)

        gluLookAt(camera[0] * self.camDistanse, camera[1] * self.camDistanse, camera[2] * self.camDistanse,
                  0.0, 0.0, 0.0,
                  0.0, 1.0, 0.0)

        glMaterialfv(GL_FRONT, GL_DIFFUSE, (self.difuseR, self.difuseG, self.difuseB, self.difuseA))
        glMaterialfv(GL_FRONT, GL_SPECULAR, (self.difuseR, self.difuseG, self.difuseB, self.difuseA))
        glMaterialfv(GL_FRONT, GL_SHININESS, self.shininess)

        self.figure.draw()

        light = rotate([0.0, 1.0, 2.0], self.lightAng1, self.lightAng2)
        glLightfv(GL_LIGHT0, GL_POSITION, (light[0] * self.lightDistanse, light[1] * self.lightDistanse, light[2] * self.lightDistanse, 1.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (self.ambientR, self.ambientG, self.ambientB, self.ambientA))
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, (self.lightDirX, self.lightDirY, self.lightDirZ))

        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (self.lightModelR, self.lightModelG, self.lightModelB, self.lightModelA))

    def move_camera(self, event):
        if event.LeftIsDown():
            pos = event.GetPosition()
            ang1 = (pos[0] - 400) * 0.45
            ang2 = (400 - pos[1]) * 0.225
            if self.camera:
                self.cameraAng1 = ang1
                self.cameraAng2 = ang2
            else:
                self.lightAng1 = ang1
                self.lightAng2 = ang2
        self.Refresh()

    def set_distanse(self, event):
        if self.camera:
            self.camDistanse -= 0.1 * np.sign(event.GetWheelRotation())
        else:
            self.lightDistanse -= 0.1 * np.sign(event.GetWheelRotation())
        self.Refresh()
