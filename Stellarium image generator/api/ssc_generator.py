import os 
from datetime import datetime

            

import os

def generate_moon_ssc(date_str, time_str="20:00:00"):
    datetime_iso = f"{date_str}T{time_str}"
    os.makedirs("scripts", exist_ok=True)
    moon_path = os.path.join("scripts", "moon.ssc")

    with open(moon_path, "w") as f:
        f.write(f"""
var path = "D:/Stellarium project/output"

core.clear("natural");
LandscapeMgr.setFlagLandscape(false);
LandscapeMgr.setFlagAtmosphere(false);
LandscapeMgr.setFlagFog(false);
core.setDate("{datetime_iso}");
core.selectObjectByName("Moon", false);
StelMovementMgr.setFlagTracking(true);
StelMovementMgr.zoomTo(0.547, 2); 
core.wait(2)
core.setGuiVisible(false);
StelMovementMgr.autoZoomIn(2);
core.setTimeRate(0.0);
core.screenshot("moon",false,path,true);
core.quitStellarium();
""")
    return moon_path


def generate_sky_ssc(date_str, time_str="20:00:00"):
    datetime_iso = f"{date_str}T21:00:00"
    os.makedirs("scripts", exist_ok=True)
    sky_path = os.path.join("scripts", "sky.ssc")

    with open(sky_path, "w") as f:
        f.write(f"""
var path = "D:/Stellarium project/output"
core.setDate("{datetime_iso}");
core.setObserverLocation("26.2389, 73.0243");
LandscapeMgr.setFlagLandscapeUseMinimalBrightness (false);
MilkyWay.setIntensity(4)
LandscapeMgr.setFlagLandscape(true);
LandscapeMgr.setFlagAtmosphere(false);
core.setGuiVisible(false);

// View east at 45 elevation
core.moveToAltAzi(89, 90);  // Altitude 89, Azimuth 90 (East)
StelMovementMgr.zoomTo(130, 1);
core.wait(1);
core.screenshot("sky",false,path,true);
core.quitStellarium();
""")
    return sky_path
