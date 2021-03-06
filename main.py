import config
import os
import shutil
import threading
import time

# CleanMii Daemon by 6100m, POC by Spotlightishere

def cleanallfiles(folder):
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        try:
            if os.path.isfile(filepath) or os.path.islink(filepath):
                print("Cleaning Thread: Unlinking %s" % filepath)
                os.unlink(filepath)
            elif os.path.isdir(filepath):
                print("Cleaning Thread: Deleting %s" % filepath)
                os.remove(filepath)
        except Exception as e:
            print(
                str("Cleaning Thread: Failed to delete %s: Reason: %s" % (filepath, e))
            )

def printtime(threadName, delay):
    while config.timecsprnghash:
        time.sleep(delay)
        print(str("%s: %s" % (threadName, time.ctime(time.time()))))

for x in list(config.folderrange):
    if config.cleanfiles == True:
        print("Main Thread: Cleaning thread began")
        thread[config.thread1idenitifier] = threading.Thread(target=cleanallfiles(x), group=None)
    elif config.cleanfiles == False:
        pass
    else:
        pass
    if config.dologging == True:
        print("Main Thread: Time thread began")
        thread[config.thread2identifier] = threading.Thread(
            target=printtime(
                "Time Thread: Printing Time, Time is:", config.timeprintingdelay
            ),
            group=None,
        )
    elif config.dologging == False:
        pass
    else:
        pass
    while config.threadcsprnghash:
        for n in range(config.initalthreadvalue, config.maxthreadvalue):
            print("Main Thread: Multiplexing process issued a syscall of all threads")
            thread[n].start()
