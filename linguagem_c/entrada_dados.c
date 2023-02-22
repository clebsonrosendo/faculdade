#include <stdio.h>
#include <string.h>



// funcao para limpar entrada e evitar conflito no fgets
void limpar_entrada() {

    char c;
    while ((c = getchar()) != '\n' && c != EOF) {}

}


int main() {

    // Definindo variaveis
    int idade;
    double salario, altura;
    char genero = 'F';
    char nome[50];

    // Entrada de dados
    printf("Digite seu nome: ");
    fgets(nome, 50, stdin);
    strtok(nome, "\n");

    printf("Digite o valor da idade: ");
    scanf("%d", &idade);

    printf("Digite o valor do salario: ");
    scanf("%lf", &salario);

    printf("Digite o valor da altura: ");
    scanf("%lf", &altura);

    // Saida de dados
    printf("NOME: %s\n", nome);
    printf("IDADE: %d\n", idade);
    printf("SALARIO: %.2lf\n", salario);
    printf("ALTURA: %.2lf\n", altura);

    return 0;

}
