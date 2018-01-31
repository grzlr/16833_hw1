import numpy as np
import math
import time
from matplotlib import pyplot as plt
from scipy.stats import norm
import pdb

from MapReader import MapReader

class SensorModel:

    """
    References: Thrun, Sebastian, Wolfram Burgard, and Dieter Fox. Probabilistic robotics. MIT press, 2005.
    [Chapter 6.3]
    """

    def __init__(self, occupancy_map, a_hit, a_short, a_max, a_rand, sigma_hit, lambda_short):

        """
        DONE : Initialize Sensor Model parameters here
        """
        self.occupancy_map = occupancy_map
        self.a_hit =a_hit
        self.a_short= a_short
        self.a_max = a_max
        self.a_rand = a_rand
        self.sigma_hit = sigma_hit
        self.lambda_short = lambda_short

    def beam_range_finder_model(self, z_t1_arr, x_t1):
        """
        param[in] z_t1_arr : laser range readings [array of 180 values] at time t
        param[in] x_t1 : particle state belief [x, y, theta] at time t [world_frame]
        param[out] prob_zt1 : likelihood of a range scan zt1 at time t
        """

        # TODO : Add your code here

        q = 1
        for k in range(0,step_size,180):
            z = z_t1_arr[k]
            theta = x_t1 + k
            z_star = raycast(x_t1,theta)
            # Maybe turn this into a log sum
            p = self.a_hit*self.p_hit(z,z_star) + 
                self.a_short*self.p_short(z,z_star) +
                self.a_max*self.p_max(z,z_star) +
                self.a_rand*self.p_rand(z,z_star)
            q = q*p

        return q

    def p_hit(self,z,z_star):
        return norm.pdf(z_star - z)

    def p_short(self,z,z_star):

        return p_unexpected

    def p_max(self,z,z_star):
        if z_star = self.z_max:
            return 1
        else 
            return 0

    def p_rand(self,z,z_star):
        if z > 0 and z < self.z_max:
            return 1/z
        else:
            return 0

    def raycast(self,x,theta):
        # TODO

        return z_star
 
if __name__=='__main__':
    pass
