import myo
myo.init()

from myo.lowlevel import pose_t, stream_emg
from myo.six import print_
import random

f = open('sync.txt','w')
class Listener(myo.DeviceListener):

    def on_pair(self, myo, timestamp):
        print_("Myo is on!")

    # def on_rssi(self, myo, timestamp, rssi):
    #     print_("RSSI:", rssi)
    #     return False # Stop the Hub

    def on_sync(self, myo, timestamp, arm, x_direction):
        print_('synced', arm, x_direction)

    def on_unsync(self,myo,timestamp):
        print_('Uh, oh, unsynced!')

    def on_lock(self,myo,timestamp):
        print_('Myo is locked')

    def on_pose(self, myo, timestamp, pose):
    	print_('on_pose', pose)
    	f.write(str(pose))
    	f.write("\n")


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