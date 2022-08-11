import csv

file_data = []

with open('main.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        file_data.append(row)

headers = file_data[0]
headers[0] = 'row_num'
file_data_rows = file_data[1:]

for star_data in file_data_rows:
    star_mass = star_data[3]
    if star_mass.lower() == 'unknown':
        file_data_rows.remove(star_data)
        continue
    else:
        try:
            star_mass = float(star_mass) * 1.989e+30
            star_data[3] = star_mass
        except: 
            file_data_rows.remove(star_data)
    
for star_data in file_data_rows:
    star_radius = star_data[4]
    if star_radius.lower() == 'unknown':
        file_data_rows.remove(star_data)
        continue
    else:
        try:
            star_radius = float(star_radius) * 6.957e+8
            star_data[4] = star_radius
        except:
            file_data_rows.remove(star_data)

star_masses = []
star_radiuses = []
star_names = []
for star_data in file_data_rows:
    star_masses.append(star_data[3])
    star_radiuses.append(star_data[4])
    star_names.append(star_data[1])
star_gravities = []

for index, name in enumerate(star_names):
    try:
        gravity = (float(star_masses[index])*6.67*10e-11 / float(star_radiuses[index])*float(star_radiuses[index]))
    except:
        pass
    star_gravities.append(gravity)

temp_file_data_rows = []
for i in range(0, (len(star_gravities)-1)):
    row = file_data_rows[i]
    row.append(star_gravities[i])
    row.pop(0)
    temp_file_data_rows.append(row)

file_data_rows = list(temp_file_data_rows)
headers.pop(0)
headers.append('Star_gravity')

with open('final.csv', 'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(file_data_rows)