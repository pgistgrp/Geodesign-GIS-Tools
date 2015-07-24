### Import relevant modules.

import arcpy

import sys
import os
import datetime
import time


### Start the script.

arcpy.AddMessage("\n{0:*^33}".format(" Script initiated. "))


### Import parameters.

label = "Importing parameters..."
arcpy.AddMessage("\n" + label)
arcpy.SetProgressorLabel(label)

# Import parameters from tool dialog box.
in_feat   = arcpy.GetParameter(0)
out_feat  = arcpy.GetParameterAsText(1)
tolerance = arcpy.GetParameter(2)

# State each input parameter with its value.
for param in arcpy.GetParameterInfo():
    if param.direction == "Input":
        arcpy.AddMessage("\n{0}:\n{1}".format(param.displayName, param.value))


### Run Simplify Polygon with default and user parameters.

label = "Running Simplify Polygon..."
arcpy.AddMessage("\n" + label)
arcpy.SetProgressorLabel(label)

running_code = (
"SimplifyPolygon_cartography(in_features={0}, out_feature_class={1}, "
"algorithm='BEND_SIMPLIFY', tolerance={2}, minimum_area=None, "
"error_option='RESOLVE_ERRORS', collapsed_point_option=None)"
).format(repr(str(in_feat)), repr(out_feat), repr(tolerance.value))

arcpy.AddMessage("\nRunning code:\n{0}".format(running_code))
arcpy.AddWarning("\n*** If script fails, compare code above to Simplify "
                 "Polygon documentation to see if parameters have changed. "
                 "***")

arcpy.SimplifyPolygon_cartography(in_feat, out_feat, "BEND_SIMPLIFY",
                                  tolerance, None, "RESOLVE_ERRORS")


### Restate results.

label = "Restating results..."
arcpy.AddMessage("\n" + label)
arcpy.SetProgressorLabel(label)

# State each output parameter with its value.
for param in arcpy.GetParameterInfo():
    if param.direction == "Output":
        arcpy.AddMessage("\n{0}:\n{1}".format(param.displayName, param.value))


### End the script.

arcpy.AddMessage("\n{0:*^33}\n".format(" Script completed. "))
