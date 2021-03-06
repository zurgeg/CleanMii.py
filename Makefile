cleanuptestfiles:
    rm -rf testdir/
    rm -rf testdir2/
    rm -rf testdir3/
    rm -rf testdir4/
    rmdir testdir/
    rmdir testdir2/
    rmdir testdir3/
    rmdir testdir4/
cleanuptemporarydatafilesinmainmode:
    rm -rf config.pyc
    rm -rf config.pyc/
cleanuptemporarydatafilesindebugmode:
    rmdir config.pyc
    rmdir config.pyc/
cleanuptemporarydatafilesinmultimode:
    rm -rf config.pyc
    rmdir config.pyc
    rm -rf config.pyc/
    rmdir config.pyc/
generatetestfiles:
    mkdir testdir/
    mkdir testdir2/
runtestworkflow:
    python3 main.py
runmainworkflowwithoutlogging:
    echo Running without logging...
    python3 main.py  >/dev/null 2>&1 < /dev/null &
    echo Daemon started!
	echo Exiting makefile...
runmainworkflowwithlogging:
    echo Running with logging...
    python3 main.py  >/dev/null 2>&1 < /dev/null >> log &
    echo Daemon started!
	echo Exiting makefile...
aptgetinstalldebugtools:
    apt-get install htop
yumgetinstalldebugtools:
    apt-get install htop
aptinstalldebugtools:
    apt install htop
aptyvariantgetinstalldebugtools:
    apt -y install htop
aptivariantinstalldebugtools:
    apt -i htop
