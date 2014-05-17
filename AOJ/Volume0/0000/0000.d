import std.stdio;

void main()
{
	int i,j;
	for (i=1;i<10;i++){
		for (j=1;j<10;j++){
			writefln("%dx%d=%d",i,j,i*j);
		}
	}
}