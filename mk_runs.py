#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2023-S1-US-00"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["L1157-B1"] = [ 119612, 119613, 119615, 119616, 119618, 119619, 119621, 119622,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["L1157-B1"] = "extent=500 b_order=1 dv=60 dw=60 pix_list=-13,14,15"


#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["L1157-B1"] = "pix_list=-13"

#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}

pars3["L1157-B1"] = ""



if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
