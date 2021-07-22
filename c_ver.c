#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <time.h>

int ary[1000]= { 0 };
int timeset[1000];
int n = 100;//좌석의 갯수

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
		printf("예약을 하시려면 1 아니면 0을 입력하시오.");
		scanf(" %d", &state);
	}

	for (int i = 0; i < n; i++)
	{
		int now = time(NULL);
		if (ary[i] == 1 || ary[i] == 2 || ary[i] == 3)
		{
			fprintf(f, "%d번 좌석이 %d초째 사용중입니다.\n", i, now - timeset[i]);
		}
	}
}

int reserve(int n)
{
	printf("이 강의실에서 예약가능한 좌석들입니다.\n");
	int count = 0;
	int number;
	for (int i = 0; i < n; i++)
	{
		if (!ary[i])
		{
			printf("%3d번 좌석", i);
			count++;
			if (count % 3 == 0)
			{
				printf("\n");
			}
		}
	}
	printf("\n예약할 좌석을 입력하시오. : ");
	scanf(" %d", &number);
	int start = time(NULL);
	ary[number] = 1;
	timeset[number] = start;
	
	printf("예약이 완료되었습니다.\n");

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
				printf("\n%d번 좌석 연장하시겠습니까? 연장하시려면 1, 아니면 0을 입력하시오.", i);
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
			printf("\n%d번 좌석 퇴실 부탁드립니다.\n");
		}
			
	}
}