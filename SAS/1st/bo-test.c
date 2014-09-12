#include <stdio.h>
#include <string.h>

unsigned long sp (void){
	__asm__("movl %esp, %eax");
}

int main (int argc, char *argv[]){
	char buffer[500];
	long esp;

	esp = sp();

	strcpy (buffer, argv[1]);
	return 0;
}	
