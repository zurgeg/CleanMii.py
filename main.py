import config
import os
import shutil
import threading
import time
# CleanMii Daemon by 6100m, POC by Spotlightishere

def cleanallfiles(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				print("Cleaning Thread: Unlinking %s" % file_path)
				os.unlink(file_path)
            elif os.path.isdir(file_path):
				print("Cleaning Thread: Deleting %s" % file_path)
                shutil.rmtree(file_path)
        except Exception as e:
            print(str("Failed to delete %s. Reason: %s" % (file_path, e)))

def printtime(threadName, delay):
    while config.timecsprnghash:
        time.sleep(delay)
        count += 1
        print(str("%s: %s" % (threadName, time.ctime(time.time()))))


for x in list(config.folderrange):
	if config.cleanfiles == True:
		print("Cleaning thread began!")
		thread1 = threading.Thread(target=cleanallfiles(x), group=None)
	elif config.cleanfiles == False:
		pass
	else:
		pass
	if config.dologging == True:
		print("Time thread began!")
		thread2 = threading.Thread(target=printtime("Time Thread: Printing Time, Time is ", config.timeprintingdelay), group=None)
	elif config.dologging == False:
		pass
	else:
		pass
	while config.threadcsprnghash:
		thread1.start()
		thread2.start()
