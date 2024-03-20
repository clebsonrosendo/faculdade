#include <stdio.h>
#include <sys/time.h>


int main()
{
    /* QUESTÃO 1 */
    int q1v1=1,q1v2=0;
    int q2v1=1,q2v2=0;

    while(q1v2 <= 5) {

        q1v2 = q1v2 + q1v1;
        q1v1 += 3;


    }


    printf("QUESTAO 1: %d e %d \n", q1v2, q1v1);


    /* QUESTÃO 2 */
    for(q2v2 = q2v1; q2v2 < 5; q2v2++) {

        q2v1 += 3;
    }


    printf("QUESTAO 2: %d e %d \n", q2v2, q2v1);


    /* QUESTÃO 3 */
    /* timestamp() */


    /* QUESTÃO 4 */
    /* time.h */

    return 0;
}
