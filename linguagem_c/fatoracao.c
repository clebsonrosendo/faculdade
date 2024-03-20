#include <stdio.h>

int main()
{

    int n, fat;

    printf("Insira um numero inteiro:");
    scanf("%d", &n);

  for(fat = 1; n > 1; n = n - 1) {
      fat = fat * n;

    }

    printf("\n%d", fat);
    return 0;
}
