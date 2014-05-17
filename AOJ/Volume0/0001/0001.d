import std.stdio;
import std.conv;
import std.string;

int main()
{
	int i,j,tmp1,tmp2;
	char[] tmp;
	int[3] height;
	for (i=0;i<10;i++){
		tmp=readln().dup;
		tmp=chomp(tmp.idup).dup;
		tmp1=to!(int)(tmp.idup);
		for(j=0;j<3;j++)
		if(tmp1>height[j]){
			tmp2=height[j];
			height[j]=tmp1;
			tmp1=tmp2;
		}
	}
	for(i=0;i<3;i++){
		writeln(height[i]);
	}
	return 0;
}