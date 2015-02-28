import sys
import time
sys.path.insert(0, '/Users/josephwon/Documents/donateMyo/myo-raw')

from myo_raw import MyoRaw as MR
from myo_raw import BT


f = open('emg.txt', 'w')

myo = MR(sys.argv[1] if len(sys.argv) >= 2 else None)

def proc_emg(emg, moving, times=[]):
    print(emg)
    f.write(str(emg))
    f.write("\n")
    ## print framerate of received data
    times.append(time.time())
    if len(times) > 20:
        #print((len(times) - 1) / (times[-1] - times[0]))
        times.pop(0)

myo.add_emg_handler(proc_emg)

myo.connect()

#myo.add_pose_handler(lambda p: print('pose', p))

try:
    while True:
        myo.run(1)
        
except KeyboardInterrupt:
    pass
finally:
    myo.disconnect()
    f.close()
    print()