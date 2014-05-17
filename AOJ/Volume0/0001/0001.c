#include <stdio.h>

int main()
{
	int i,j,tmp1,tmp2,height[3]={0,0,0};
	for (i=0;i<10;i++){
		scanf("%d",&tmp1);
		for(j=0;j<3;j++)
		if(tmp1>height[j]){
			tmp2=height[j];
			height[j]=tmp1;
			tmp1=tmp2;
		}
	}
	for(i=0;i<3;i++){
		printf("%d\n",height[i]);
	}
}