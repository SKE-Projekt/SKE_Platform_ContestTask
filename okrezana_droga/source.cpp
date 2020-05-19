
#include <stdio.h>
#define SWAP(a,b) tmp=a; a=b; b=tmp

int N, X[12], Y[12];

int get_dir(int x1, int y1, int x2, int y2)
{
  if (x1!=x2 && y1!=y2) return -1;  /* No direction */
  if (x1==x2 && y1<y2) return 0;  /* p2 north of p1 */
  if (x1==x2 && y1>y2) return 1;  /* p2 south of p1 */
  if (y1==y2 && x1<x2) return 2;  /* p2 east of p1 */
  if (y1==y2 && x1>x2) return 3;  /* p2 west of p1 */
}

/* Check a permutation... */
int check(int *p)
{
  int i;
  for (i=1; i<=N+1; i++) {
      printf("P[i] = %d\n", p[i]);
    if (get_dir(X[p[i]], Y[p[i]], X[p[i-1]], Y[p[i-1]])==-1) return 0;
  }
  for (i=1; i<=N; i++) 
    if (get_dir(X[p[i]], Y[p[i]], X[p[i-1]], Y[p[i-1]]) ==
	get_dir(X[p[i+1]], Y[p[i+1]], X[p[i]], Y[p[i]])) return 0;
  return 1;
}

/* Generate and check all permutations... */
int perm(int n, int *so_far, int *remaining)
{
    printf("N: %d\n", n);
  int i, tmp, total=0;
  if (n==N) {return check(so_far);}
  for (i=0; i<N-n; i++) {
    printf("I: %d\n", i);
    so_far[n+1] = remaining[i];
    SWAP(remaining[i], remaining[N-n-1]);
    total += perm(n+1, so_far, remaining);
    SWAP(remaining[i], remaining[N-n-1]);
  }    
  return total;
}

int main(void)
{
  int P[12] = {0}, D[10] = {1,2,3,4,5,6,7,8,9,10}, i;

  freopen ("connect.in", "r", stdin);
  freopen ("connect.out", "w", stdout);

  scanf ("%d", &N);
  for (i=1; i<=N; i++)
    scanf ("%d %d", &X[i], &Y[i]);

  printf ("WYN: %d\n", perm (0,P,D));
  
  return 0;
}