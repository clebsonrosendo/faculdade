function fibonacciGenerator(n) {
    // declare the array starting with the first 2 values of the fibonacci sequence
    // starting at array index 1, and push current index + previous index to the array
    for (var fibonacci = [0, 1], i = 2; i < n; i++) 
        
    fibonacci.push(fibonacci[i-1] + fibonacci[i - 2])
  
    return fibonacci
  }
  
  console.log(fibonacciGenerator(10))