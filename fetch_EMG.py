import sys
sys.path.insert(0, '/Users/josephwon/Documents/donateMyo/myo-raw')
from myo_raw import MyoRaw as MR




if __name__ == '__main__':
    myo = MR(sys.argv[1] if len(sys.argv) >= 2 else None)

    try:
        while True:
            myo.run(1)
            print "hello myoscript!"
    except KeyboardInterrupt:
        pass
    finally:
        m.disconnect()
        print()