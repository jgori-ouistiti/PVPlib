import matplotlib.pyplot as plt
import sys
import copy
import json
from datetime import datetime

from pvplib import PVP_alpha, __version__




def test_version():
    assert __version__ == "0.3.1"


def conv_time(time_str):
    time_format = '%H:%M:%S.%f'
    time_obj = datetime.strptime(time_str, time_format)
    unix_time = time_obj.timestamp()
    return unix_time


TEST_DATA_PATH = "tests/force.json"




block_test = []
with open(TEST_DATA_PATH, "r") as _file:
    data = json.load(_file)
    for trial in data:
        if trial['Block actuel'] == 'Block_3':
            block_test.append(trial)


D = block_test[0]['d_value']

pvp = PVP_alpha()
for trial in block_test:
    traj = trial['sensor_values']
    x = [float(e['value']) for e in traj]
    t = [conv_time(e['timestamp']) for e in traj]
    pvp.add_trajectory(
    t, x, target=[D], correct_edges=True, correct_edges_kwargs = dict(method="speed_threshold", edges = ['start', 'stop'], percent=[2,5])
    )


    
pvp.compute_profiles()
fig, axs = plt.subplots(2, 2)
pvp.plot_kinematic_profiles([axs[0,0]])
pvp.plot_std_profiles(axs[0,1], fit=False)
axs[1,0].plot(pvp._kinematic_profile[:,0,0])
axs[1,0].plot(pvp._kinematic_profile[:,0,4])
axs[1,0].plot(pvp._kinematic_profile[:,0,8])
axs[1,0].plot(pvp._kinematic_profile[:,0,17])
plt.show()
plt.close()
