all:
	./replaceExamples.py
	cd ./tmp; make all	

clean:
	cd ./tmp; make clean	

pdf:	all
	cd ./tmp; make pdf
