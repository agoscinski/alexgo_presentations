## Data set downloaded at https://qmml.org/datasets.html (see GDB7-13 (QM7b))
## This file is for postporcessing quick and dirty

import os

data_points = 55
filename = 'dsgdb7njp.xyz'
filename_new = 'dsgdb7njp_small'+str(data_points)+'.xyz'
f = open(filename, 'rw')
f_new = open(filename_new, 'w')
it_data_points = 0
for line in f:
    if line != '\n':
        f_new.write(line)
    else:
        it_data_points += 1
        if it_data_points == 55: break
f.close()
f_new.close()

filename_new = 'dsgdb7njp_atomic_energy_small_'+str(data_points)+'.xyz'
f = open(filename, 'rw')
f_label_new = open(filename_new, 'w')
it_data_points = 0

f.readline()
labels = f.readline().split(' ')[0]
f_label_new.write(labels)
it_data_points += 1
f_label_new.write('\n')
while True:
    line = f.readline()
    if line == '\n':
        f.readline()
        labels = f.readline().split(' ')[0]
        f_label_new.write(labels)
        it_data_points += 1
        if it_data_points == 55: break
        f_label_new.write('\n')

f_label_new.close()
f.close()
