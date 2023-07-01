#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    } return (0);
}

void create_zombie_processes()
{
    int i;
    pid_t pid;

    for (i = 0; i < 5; i++)
    {
        pid = fork();

        if (pid == -1)
        {
            perror("fork");
            exit(EXIT_FAILURE);
        }
        else if (pid == 0)
        {
            // Child process
            printf("Zombie process created, PID: %d\n", getpid());
            exit(EXIT_SUCCESS);
        }
    }
}

int main(void)
{
    create_zombie_processes();
    infinite_while();
    return (EXIT_SUCCESS);
}