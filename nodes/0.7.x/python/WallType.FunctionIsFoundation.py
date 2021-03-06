import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

walltypes = UnwrapElement(IN[0])
booleans = list()

for item in walltypes:
	try:
		wallfunction = item.get_Parameter(BuiltInParameter.FUNCTION_PARAM).AsInteger()
		if wallfunction == 2:
			booleans.append(True)
		else:
			booleans.append(False)
	except:
		booleans.append(False)
OUT = booleans