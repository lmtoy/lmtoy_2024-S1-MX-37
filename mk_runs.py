#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-37"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["L1157-B1"] = [ 119612, 119613, 119615, 119616, 119618, 119619, 119621, 119622,
                   119700, 119701, 119703, 119704, 119706, 119707, 119711, 119712,
                   119714, 119715, 119717, 119718, 119722, 119723, 119725, 119726,
                   119728, 119729,
                   119859, 119860, 119862, 119863, 119865, 119866, 119872, 119873, 
                   119875, 119876, 119878, 119879, 119883, 119884, 119886, 119887, 
                   119889, 119890, 119896, 119897, 119899, 119900, 119902, 119903,
                   120222, 120223, 120225, 120226, 120228, 120229, 120231, 120232,
                   120234, 120235, 120237, 120238, 120240, 120241,]
		   

on["L1157-B1_SB0"] = [ 120673, 120674, 120810, 120811, 121085, 121086,\
                       121270, 121271,
                       132933, 132934,     # apr 5
                       134461, 134462, 135122, 135123, 135125, 135126,
                       135567, 135568, 135570, 135571, 135573, 135574,]


on["L1157-B1_SB1"] = [ 120670, 120671, 120807, 120808, 120966, 120967, 120969, \
                       120970, 121071, 121072, 121074, 121075, 121077, 121078, \
                       121082, 121083,
                      -121854,-121855,   # nov-6 (all bad)
	               122015, 122016, 122018, 122019,        # nov-7
                       132936, 132937,-132939,]               # apr 5

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["L1157-B1"]     = "extent=240 b_order=1 pix_list=-15 dv=200 dw=200"
pars1["L1157-B1_SB0"] = "extent=240 b_order=1 pix_list=-13 dv=200 dw=200"
pars1["L1157-B1_SB1"] = "extent=240 b_order=1 pix_list=-13 dv=200 dw=200"


#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["L1157-B1"]     = "bank=0 pix_list=-0,1,4,5,10,11,12,13 birdies=2045,2048,2051,3069,3072,3075"
pars2["L1157-B1_SB0"] = "bank=0 pix_list=-8,9,12,13"
pars2["L1157-B1_SB1"] = "bank=0 pix_list=-5,8,9,12,13"

#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}

pars3["L1157-B1"]     = "bank=1 birdies=2045,2048,2051,2176,2258,2261,2264,2433,2471,2474,2477,2643,2646,2649,2687,2856,2859,2862,3069,3072,3075 pix_list=-3,8,13,15"


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
