import csv 

rows = [] 

with open("final_data.csv",'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        rows.append(row)


headers = rows[0]

planet_data_rows = rows[1:]

#print(headers)
#['', 'Star_name', 'Distance', 'Mass', 'Radius']

temp_planet_data_rows = list(planet_data_rows)

for planet_data in temp_planet_data_rows:
    planet_mass = planet_data[3]
    if planet_mass.lower() == 'unknown':
        planet_data_rows.remove(planet_data)
        continue
    else:
        planet_mass_values = planet_mass.split(' ')[0]
        planet_mass_ref = planet_mass_values('')[1]
        if planet_mass_ref == "Jupiters":
            planet_mass_values = float(planet_mass_values) * 1.989e+30
        planet_data[3] = planet_mass_values

    planet_radius = planet_data[4]
    if planet_radius.lower() == 'unknown':
        planet_data_rows.remove(planet_data)
        continue
    else:
        planet_radius_values = planet_radius.split(' ')[0]
        planet_radius_ref = planet_radius.split(' ')[1]
        if planet_radius_ref == "Jupiters":
            planet_radius_values = float(planet_radius_values) * 6.957e+8
        planet_data[4] = planet_radius_values


planet_masses = [] 
planet_radiuses = []
planet_names = [] 

for planet_data in planet_data_rows:
    planet_masses.append(planet_data[3])
    planet_radiuses.append(planet_data[4])
    planet_names.append(planet_data[1])

planet_gravity = [] 

for index,name in enumerate(planet_names):
    gravity = (float(planet_masses[index]) * 5.972e+24) / (float(planet_radius[index]) * float(planet_radius[index])) * 6371000 * 6371000 * 6.674e-11
    planet_gravity.append(gravity)

