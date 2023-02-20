// Média aritmética
function mAritmetica() {
    let it = [40.99, 50, 60]
    let divisor = it.length
    let soma = 0
    for(i=0;i<it.length;i++) {
        soma += it[i]
    }
    return soma / divisor
}


console.log(mAritmetica())