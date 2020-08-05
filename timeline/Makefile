ALL: ../src/timeline/timeline_rc.py
 
RES:=$(shell /usr/bin/find media -type f -newer timeline_rc.py)
RES+=$(shell /usr/bin/find . -iname \*.js -type f -newer timeline_rc.py)
RES+=index.html

../src/timeline/timeline_rc.py: timeline.qrc $(RES)
	pyrcc5 timeline.qrc -o $@
