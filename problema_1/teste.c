#include <stdio.h>

int main (void)
{

    int INDICE = 13, SOMA = 0, K = 0;

    while(K < INDICE)
    {   
        
        // Contator
        K++;
        // Operação
        SOMA += K;
        // Retorno
        printf("%i", SOMA);
    }
    return 0;
}