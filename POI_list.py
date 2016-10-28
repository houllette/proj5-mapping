def process():
	'''
	reads information from txt file containing POI data and returns a list of
	dictionaries of individual POI
	'''
	poi = []

	with open('points_of_interest.txt', 'r') as f:
		points = f.readlines()

	for raw_point in points:
		parts = raw_point.split(",")
		point = {"Description": parts[0].strip(), "Latitude": float(parts[1].strip()), "Longitude": float(parts[2].strip())}
		poi.append(point)

	return poi