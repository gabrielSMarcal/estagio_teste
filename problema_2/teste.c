#include <stdio.h>

int is_fibonacci(int arr[], size_t n, int num);

int main()
{

    size_t n = 20;
    int n1 = 0, n2 = 2, nextTerm, arr[20]; // Definição do fibonacci com valores 0 e 2;

    // Cálculo de Fibonacci;
    for (size_t i = 0; i < n; i++)
    {

        arr[i] = n1;
        nextTerm = n1 + n2;
        n1 = n2;
        n2 = nextTerm;
    }

    // Testes com os números 4 (True), -5 (False), -12345789 (False) e 228 (True);
    is_fibonacci(arr, n, 4) ? printf("%d sim\n", 4): printf("%d não\n", 4);
    is_fibonacci(arr, n, -5) ? printf("%d sim\n", -5): printf("%d não\n", -5);
    is_fibonacci(arr, n, -123456789) ? printf("%d sim\n", -123456789): printf("%d não\n", -123456789);
    is_fibonacci(arr, n, 288) ? printf("%d sim\n", 288): printf("%d não\n", 288);

    return 0;
}

int is_fibonacci(int arr[], size_t n, int num)
{
    
    for (size_t i = 0; i < n; i++)
    {

        if (arr[i] == num || arr[i] == -num)
        return 1;
    }
    
    return 0;
}