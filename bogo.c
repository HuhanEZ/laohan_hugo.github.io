#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include<time.h>
#define RANGE 100
bool is_sorted(int *a, int n)
{
  while ( --n >= 1 ) {
    if ( a[n] < a[n-1] ) return false;
  }
  return true;
}
 
void shuffle(int *a, int n)
{
  int i, t, r;
  for(i=0; i < n; i++) {
    t = a[i];
    r = rand() % n;
    a[i] = a[r];
    a[r] = t;
  }
}
 
size_t bogosort(int *a, int n)
{
  size_t com=0;
  while ( !is_sorted(a, n) ){
    com++;
    /*for(int i=0;i<n;i++){
      printf("%d ",a[i] );
    }*/
    shuffle(a, n);
  }
  return com;
}
void RandomArray(int a[],int size){
  srand((unsigned)time(NULL));
  for(int i=0;i<size;i++){
    int number=rand()%RANGE+1;
    a[i]=number;
  }
} 
int main()
{
  size_t output=0;
  for(int i=2;i<=30;i++){
    int *array=malloc(sizeof(int)*30);
    RandomArray(array,i);
    output=bogosort(array,i);
    printf("Shuffles for n=%d is %ld. \n",i,output);
    free(array);
  }
  return 0;
}