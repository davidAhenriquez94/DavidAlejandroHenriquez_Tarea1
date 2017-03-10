energia.pdf: datos1.txt datos2.txt datos4.txt
	python graficador.py

datos1.txt: a.out 
	export OMP_NUM_THREADS=1
	./a.out > datos1.txt

datos2.txt: a.out 
	export OMP_NUM_THREADS=2
	./a.out > datos2.txt

datos4.txt: a.out	
	export OMP_NUM_THREADS=4
	./a.out > datos4.txt

 
a.out: leapfrog1.c
	cc leapfrog1.c -lm -fopenmp

clean:
	rm *.out *.txt
