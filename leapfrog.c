#include<stdio.h>
#include <math.h>
#include <stdlib.h>

void leapfrog(float *x, float *v, int i,int j, float h , float B);
int trans(int i, int j);

float dt = 0.005, B = 1.0;
int N = 64, T = 1000;

int main (int argc, char ** argv){
  float *x = malloc(N*T*sizeof(float));
  float *v = malloc(N*T*sizeof(float));
 
  for(int i = 1; i<N-1; i++){
    x[trans(i,0)] = sin(M_PI*i/(N-1));
    v[trans(i,0)] = (M_PI/(N-1))*cos(M_PI*i/(N-1));
  }
  for(int j = 0; j<T; j++ ){
    x[trans(0,j)] = 0.0;
    x[trans(N-1,j)] = 0.0;
    v[trans(0,j)] = 0.0;
    v[trans(N-1,j)] = 0.0;
  }


  for(int j = 0; j<T;j++){
#pragma omp parallel for \shared(x,v),private(j)
    for(int i = 1; i<N-1; i++){
      leapfrog(x,v,i,j,dt,B);
    }
  }
  
  for(int i = 0; i<N; i++){
    for(int j = 0; j<T; j++){
      printf("%f\n",x[trans(i,j)]);  
	}
  }

  for(int i = 0; i<N; i++){
    for(int j = 0; j<T; j++){
      printf("%f\n",v[trans(i,j)]);
    }
  }
 
}


void leapfrog(float *x, float *v, int i,int j, float h , float B){
    float F_actual = x[trans(i+1,j)] - 2*x[trans(i,j)] + x[trans(i-1,j)] + B*(powf((x[trans(i+1,j)]-x[trans(i,j)]),3) - powf((x[trans(i,j)] - x[trans(i-1,j)]),3));
    float v_medio = v[trans(i,j)] + (1.0/2)*h*F_actual;
    x[trans(i,j+1)] = x[trans(i,j)] + h*v_medio;
    float F_futuro = x[trans(i+1,j)] - 2*x[trans(i,j)] + x[trans(i-1,j)] + B*(powf((x[trans(i+1,j)]-x[trans(i,j)]),3) - powf((x[trans(i,j)] - x[trans(i-1,j)]),3));
    v[trans(i,j+1)] = v_medio + (1.0/2)*h*F_futuro;
}  

int trans(int i, int j){ 
  return j*N + i;
}
