def getToken(line):
	tokens = line.split(" ")
	return tokens[2]

def readParameters(path_to_meta, d_sun_earth_path):
	meta = open(path_to_meta, "r")
	parameters = []

	for line in meta:
		if "LANDSAT_SCENE_ID" in line:
			info = getToken(line.strip())

			parameters.append(info[3])
			parameters.append(info[14:17])

			julian_day = parameters[1]
			
		elif "SUN_ELEVATION" in line:
			parameters.append( getToken(line.strip()) )

	d_sun_earth = open(d_sun_earth_path, "r")
	for line in d_sun_earth:
		if julian_day in line:
			info = line.split(" ")
			parameters.append( info[1].strip() )

	return parameters