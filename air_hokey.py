from pygw import Game
from pygw.graphic import CartesianPlane, Polygon


class AirHockey(Game):

  def __init__(self):
    super().__init__()

    self.title = "Air Hockey"
    self.size = (500, 800)

  def setup(self):
    self.p1 = Polygon(CartesianPlane(self.window.surface, self.size), (30,) * 10)

  def onRender(self):
    self.window.surface.fill((255, 255, 255))
    self.p1.show()
