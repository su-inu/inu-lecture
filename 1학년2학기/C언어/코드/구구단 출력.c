#include <stdio.h>
int main(void)
{
	for (int i = 1; i < 10; i++)
	{
		printf("\n%d단 출력\n\n", i);
		for (int j = 1; j < 10; j++)
		{
			printf("%d * %d = %d\n", i, j, i * j);
		}
	}
	return 0;
}