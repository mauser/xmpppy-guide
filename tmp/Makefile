all:
	latex main.tex && latex main.tex

clean:
	rm -f *.aux
	rm -f *.log
	rm -f *~
	rm -f *.toc
	rm -f *.tex
	rm -f *.dvi

pdf:	all
	dvipdf main.dvi ../a_practical_guide_to_xmpppy.pdf
