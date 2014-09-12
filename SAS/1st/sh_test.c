#include <stdio.h>
#include <unistd.h>

int main ( int argc, char *argv[] )
{
	printf ( "start shell\n" );
	execl ( "/bin/sh" , "sh" , NULL );
	printf ( "stop shell\n");
	return 0;
}
