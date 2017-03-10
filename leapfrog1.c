#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <omp.h>

void leapfrog(float *x, float *v, int i,int j, float h , float B);

float dt = 1.0/200, B = 1.0;
float F_actual,F_futuro,v_medio;
int N = 64, T = 10000001,i,j,k,n,m;

int main (int argc, char ** argv){

//Creacion de variables posicion y velocidad
	float *x = malloc(N*sizeof(float));
	float *v = malloc(N*sizeof(float));
	
	x[0] = 0.0;
	x[N-1] = 0.0;
	v[0] = 0.0;
	v[N-1] = 0.0;
//Asignacion de valores iniciales 
	
	for(i = 1; i<N-1; i++){
	  x[i] = sin(M_PI*i/(N-1));
	  v[i] = 0.0; 
	}

//solucion de la ecuacion diferencial con el metodo leapfrog
	float x_temp[N-1];
	float v_medio_temp[N-1];
	for(j = 0; j<T;j++){
	  if(j%10000 == 0 ){
	    for(k = 0; k<N; k++){
	      printf("%f\t%f\n",x[k],v[k]);
	    } 
	  }
#pragma omp parallel for shared(x,v)
	  for(i = 1; i<N-1; i++){
	    F_actual = x[i+1] - 2*x[i] + x[i-1] + B*(powf((x[i+1]-x[i]),2) - powf((x[i] - x[i-1]),2));
	    v_medio = v[i] + (1.0/2)*dt*F_actual;
	    x_temp[i] = x[i] + dt*v_medio;
	    v_medio_temp[i] = v_medio;
	  }
	  for(m = 1; m<N-1; m++){
	    x[m] = x_temp[m];
	  }
#pragma omp parallel for shared(x,v)
	  for(n = 1; n<N-1; n++){
	    F_futuro = x[n+1] - 2*x[n] + x[n-1] + B*(powf((x[n+1]-x[n]),3) - powf((x[n] - x[n-1]),3));
	    v[n] = v_medio_temp[n] + (1.0/2)*dt*F_futuro;
	  }
	}

	free(x);
	free(v);
	return 0;
}



