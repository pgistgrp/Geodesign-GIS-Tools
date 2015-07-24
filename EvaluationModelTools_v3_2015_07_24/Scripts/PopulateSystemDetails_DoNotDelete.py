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
in_table     = arcpy.GetParameter(0)
proj_area    = arcpy.GetParameterAsText(1)
systems      = arcpy.GetParameter(2)
target_table = arcpy.GetParameter(3)

# State each input parameter with its value.
for param in arcpy.GetParameterInfo():
    if param.direction == "Input":
        arcpy.AddMessage("\n{0}:\n{1}".format(param.displayName, param.value))


### Delete existing records in input table (derived output table).

label = "Deleting existing records..."
arcpy.AddMessage("\n" + label)
arcpy.SetProgressorLabel(label)

arcpy.DeleteRows_management(target_table)


### Sort new records in input feature set.

label = "Sorting new records..."
arcpy.AddMessage("\n" + label)
arcpy.SetProgressorLabel(label)

# Use in_memory workspace to ensure cleanup of intermediate data.
systems_sorted = r"in_memory\systems_sorted"
arcpy.Sort_management(systems, systems_sorted, [["sysnumber", "ASCENDING"]])

# Calculate all new records to defined Project Area.
arcpy.CalculateField_management(systems_sorted, "projarea", repr(proj_area),
                                "PYTHON_9.3")


### Add new records to target table.

label = "Adding new records..."
arcpy.AddMessage("\n" + label)
arcpy.SetProgressorLabel(label)

# Append all records.
arcpy.Append_management(systems_sorted, target_table, "NO_TEST")


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
