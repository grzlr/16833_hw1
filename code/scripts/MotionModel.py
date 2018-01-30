import sys
import numpy as np
import numpy.random.normal as sample
import math

class MotionModel:

    """
    References: Thrun, Sebastian, Wolfram Burgard, and Dieter Fox. Probabilistic robotics. MIT press, 2005.
    [Chapter 5]
    """

    def __init__(self,a1,a2,a3,a4):

        """
        Initialize Motion Model parameters here
        """
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4


    def update(self, u_t0, u_t1, x_t0):
        """
        param[in] u_t0 : particle state odometry reading [x, y, theta] at time (t-1) [odometry_frame]
        param[in] u_t1 : particle state odometry reading [x, y, theta] at time t [odometry_frame]
        param[in] x_t0 : particle state belief [x, y, theta] at time (t-1) [world_frame]
        param[out] x   : particle state belief [x, y, theta] at time t [world_frame]
        """
        ux_t0  = u_t0[0]
        uy_t0  = u_t0[1]
        uth_t0 = u_t0[2]
        ux_t1  = u_t1[0]
        uy_t1  = u_t1[1]
        uth_t1 = u_t1[2]

        del_rot1  = atan2(uy_t1-uy_t0,ux_t1-ux_t0) - uth_t0
        del_trans = math.sqrt((ux_t1-ux_t0)^2 + (uy_t1-uy_t0)^2)
        del_rot2  = uth_t1 - uth_t0 - del_rot1

        del_rot1  = del_rot1 - sample(0,self.a1*del_rot1^2 + self.a2*del_trans^2)
        del_trans = del_trans - sample(0, self.a3*del_trans^2 _ self.a4*(del_rot1^2 + del_rot2^2))
        del_rot2  = del_rot2 - sample(0, self.a1*del_rot2^2 + self.a2*del_trans^2)
        
        x_t1 = x_t0

        x_t1[0] = x_t0[0] + del_trans*math.cos(x_t0[2] + del_rot1)
        x_t1[1] = x_t0[1] + del_trans*math.cos(x_t0[2] + del_rot1)
        x_t1[2] = x_t0[2] + del_rot1 +del_rot2
        
        return x_t1


if __name__=="__main__":
    pass
