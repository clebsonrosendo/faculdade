// Algoritmo de ordenação por inserção

let arr = [5, 4, 6, 1, 3]
let newValue = 2
arr.unshift(newValue)

// Passando a matriz não classificada para inserção
function insertSort(arr) {
    // Percorrendo todo o array a partir do segundo elemento
    for (i = 1; i < arr.length; i++) {

        let currentValue = arr[i]
        let j

        for (j = i-1; j >= 0 && arr[j] < currentValue; j--) {

            arr[j+1] = arr[j]
        }

        arr[j+1] = currentValue

    }

    return arr
}


console.log(insertSort(arr))
