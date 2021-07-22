#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <time.h>

int ary[1000]= { 0 };
int timeset[1000];
int n = 100;//�¼��� ����

int reserve(int n);
int check(int n);

int main(void)
{
	FILE* f;
	fopen_s(&f, "output.txt", "w");

	for (int i = 1; i < 1000; i += 2)
		ary[i] = 5;
	int state = 1;
	while (state)
	{
		check(n);
		reserve(n);
		printf("������ �Ͻ÷��� 1 �ƴϸ� 0�� �Է��Ͻÿ�.");
		scanf(" %d", &state);
	}

	for (int i = 0; i < n; i++)
	{
		int now = time(NULL);
		if (ary[i] == 1 || ary[i] == 2 || ary[i] == 3)
		{
			fprintf(f, "%d�� �¼��� %d��° ������Դϴ�.\n", i, now - timeset[i]);
		}
	}
}

int reserve(int n)
{
	printf("�� ���ǽǿ��� ���డ���� �¼����Դϴ�.\n");
	int count = 0;
	int number;
	for (int i = 0; i < n; i++)
	{
		if (!ary[i])
		{
			printf("%3d�� �¼�", i);
			count++;
			if (count % 3 == 0)
			{
				printf("\n");
			}
		}
	}
	printf("\n������ �¼��� �Է��Ͻÿ�. : ");
	scanf(" %d", &number);
	int start = time(NULL);
	ary[number] = 1;
	timeset[number] = start;
	
	printf("������ �Ϸ�Ǿ����ϴ�.\n");

}

int check(int n)
{
	int now = time(NULL);
	int state;
	for (int i = 0; i < n; i++)
	{
		int dif = now - timeset[i];
		if (ary[i] == 1 || ary[i] == 2)
		{
			if (14100 <= dif && dif < 14400)
			{
				printf("\n%d�� �¼� �����Ͻðڽ��ϱ�? �����Ͻ÷��� 1, �ƴϸ� 0�� �Է��Ͻÿ�.", i);
				scanf(" %d", &state);
				if (state)
				{
					timeset[i] += 7200;
					ary[i]++;
				}
				else
					ary[i] = 3;
			}
			else
			{

			}
		}
		else if (ary[i] == 3 && dif > 14400)
		{
			printf("\n%d�� �¼� ��� ��Ź�帳�ϴ�.\n");
		}
			
	}
}