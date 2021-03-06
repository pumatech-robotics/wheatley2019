import wpilib
import math
from wpilib import Encoder

class Encoders:
  """
  Encoder group class for drivetrain
     - We use 2 E4T encoders
  """

  dpp = 6 * math.pi / 1440 # 6 in. wheels, 1440 ppr on e4ts

  def __init__(self,
              l_a = 0,
              l_b = 1,
              r_a = 2,
              r_b = 3):

    self.left = Encoder(l_a,l_b, reverseDirection=True)
    self.right = Encoder(r_a,r_b)

    self.left.setDistancePerPulse(self.dpp)
    self.right.setDistancePerPulse(self.dpp)

  def getDist(self):
    return (self.left.GetDistance + self.right.getDistance) /2

  def get_R_Dist(self):
    return self.right.GetDistance

  def get_L_Dist(self):
    return self.left.gGetDistance()

  def reset(self):
    self.right.reset()
    self.left.reset()

