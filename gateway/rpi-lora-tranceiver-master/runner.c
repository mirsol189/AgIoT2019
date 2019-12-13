#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

void loop()
{
	FILE *src;
	char buf;

	if((src = fopen("actuator.txt", "rt")) == NULL)
	{
		perror("fopen");
		exit(1);
	}

	fseek(src, -2 * sizeof(char), SEEK_END);
	fread(&buf, sizeof(char), 1, src);

	//"/home/pi/rpi-lora-tranceiver-master/app"
	//if(execlp("./app", "sender", buf, NULL) < 0)
	//{
		//perror("execlp");
		//exit(1);
	//}

	char cmd[50];
	sprintf(cmd, "./app sender %c", buf);
	printf("%s\n", cmd);

	system(cmd);

	fclose(src);
}

int main()
{
	while(1)
	{
		loop();
		sleep(10);
	}
	
	return 0;
}
