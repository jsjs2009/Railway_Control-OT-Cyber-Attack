#-----------------------------------------------------------------------------
# Name:        railwayGlobal.py
#
# Purpose:     This module is used as the Local config file to set constants, 
#              global parameters which will be used in the other modules.
#              
# Author:      Yuancheng Liu
#
# Created:     2019/05/17
# Copyright:   YC
# License:     YC
#-----------------------------------------------------------------------------
import os

dirpath = os.getcwd()
print("Current working directory is : %s" %dirpath)

#------<CONSTANTS>-------------------------------------------------------------
BGPNG_PATH = "".join([dirpath, "\\img\\Trainbg.png"])
WKJPG_PATH = "".join([dirpath, "\\img\\walk.jpg"])
LTPNG_PATH = "".join([dirpath, "\\img\\left.png"])


# PLC basic config: (type, IP address, port, input_#, output_#)
PLC_CFG = {
    'PLC0'  : ('[m221]',    "192.168.0.101", '4343', 8, 8), 
    'PLC1'  : ('[m221]',    "192.168.0.102", '4343', 8, 8), 
    'PLC2'  : ('[S7-1200]', "192.168.0.103", '4343', 8, 8)
}

#-------<GLOBAL PARAMTERS>-----------------------------------------------------
# Set the global reference here.

iPlcPanelList = []  # Plc panel list. 
iMapPanel = None    # History chart panel
iMainFrame = None   # Main frame. 
iSensorCount = 0    # number of sensors. 