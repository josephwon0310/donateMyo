import myo
myo.init()

from myo.lowlevel import pose_t, stream_emg
from myo.six import print_
import random

class Listener(myo.DeviceListener):

    def on_pair(self, myo, timestamp):
        print_("Myo is on!")

    # def on_rssi(self, myo, timestamp, rssi):
    #     print_("RSSI:", rssi)
    #     return False # Stop the Hub

    def on_sync(self, myo, timestamp, arm, x_direction):
        print_('synced', arm, x_direction)

    def on_pose(self, myo, timestamp, pose):
    	#f.write(str(Listener.on_pose()))
    	print_('on_pose', pose)

def poser(f):
	f.write(str(Listener.on_pose()))

#f = open('sync.txt','w')

def main():
    hub = myo.Hub()
    hub.set_locking_policy(myo.locking_policy.none)
    hub.run(1000, Listener())
    try:
    	while hub.running:
    		#poser(f)
    		myo.time.sleep(0.2)
    except KeyboardInterrupt:
    		print_("myo out")
    		hub.stop(True)

if __name__ == '__main__':
    main()