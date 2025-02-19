import pandas
from pandas import DataFrame
import json

def readPage(task):
	try:
		name = ""
		seg = ""
		formula = ""
		f = open("../prepare/data/%s.txt" % task, "r")
		jsonString = f.read()
		f.close()
		res = json.loads(jsonString)
		for i in res:
			if (i == 'name'):
				name = res[i]
				name += '\n'
			if (i == 'data'):
				seg = res[i]
			if (i == 'formula'):
				for j in res[i]:
					formula += j
					formula += '\n'
		return task, name, seg, formula
	except Exception as e:
		print(e)
		return "-1", "", "", ""

taskIds = pandas.read_csv(
		"../prepare/allNeed.csv"
		).taskId

names = []
ssids = []
segs = []
formulas = []

for i in taskIds:
	print(i)
	_ssid = ""
	_name = ""
	_seg = ""
	_formula = ""
	_ssid, _name, _seg, _formula = readPage(i)
	if _ssid == "-1":
		continue
	ssids.append(_ssid)
	names.append(_name)
	segs.append(_seg)
	formulas.append(_formula)

result = DataFrame({
		'formula': formulas,
		'name': names,
		'seg': segs,
		'ssid': ssids,
		})

result.to_csv(
		"result.csv",
		mode = 'w',
		header = False,
		)
