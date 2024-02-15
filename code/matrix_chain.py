import sys 

def matrix_chain(my_mat, i, j):
    # This implies the matrix has no elements
    if i == j:
        return 0
    
    minim_comp=sys.maxsize
    for k in range(i, j):
        count=(matrix_chain(my_mat, i, k) + matrix_chain(my_mat, k+1, j) + my_mat[i-1] + my_mat[k] * my_mat[j])
        
        if count < minim_comp:
            minim_comp = count 
        return minim_comp
    
matrix_sizes= [10, 23, 34, 10]

print("Minimum multiplications are: ", matrix_chain(matrix_sizes, 1, len(matrix_sizes) - 1))

    
Docs="""
Imagine you have a bunch of matrices, and you want to multiply them together in the most efficient way possible. This algorithm helps you find out the minimum number of multiplications needed to achieve that.

Here's how it works:

1. First, it defines a function called `matrix_chain` that takes three parameters: `my_mat` (which represents the list of matrix sizes), `i` (which represents the starting index of the matrices), and `j` (which represents the ending index of the matrices).

2. Inside the function, it checks if `i` is equal to `j`. If it is, that means there's only one matrix, and in that case, it returns 0 because you don't need to multiply anything.

3. Then, it initializes a variable called `minim_comp` with a really large value. This variable will keep track of the minimum number of computations needed.

4. Next, it goes through a loop that iterates from `i` to `j-1`. This loop helps in breaking down the problem into smaller subproblems.

5. Within the loop, it calculates the number of multiplications needed to multiply the matrices from `i` to `k` and from `k+1` to `j`. It also includes the multiplication needed for the current combination of matrices. This is represented by the formula `count=(matrix_chain(my_mat, i, k) + matrix_chain(my_mat, k+1, j) + my_mat[i-1] + my_mat[k] * my_mat[j])`.

6. It compares this count with the current minimum computation (`minim_comp`) and updates `minim_comp` if the count is smaller.

7. Finally, it returns `minim_comp`, which represents the minimum number of multiplications needed to multiply the matrices from index `i` to `j`.

8. Outside the function, it initializes a list called `matrix_sizes` which represents the sizes of the matrices.

9. Then, it calls the `matrix_chain` function with the `matrix_sizes` list, starting index 1, and ending index as length of `matrix_sizes` minus 1.

10. It prints out the result which represents the minimum number of multiplications needed to multiply the matrices in the most efficient way.

So, this algorithm recursively breaks down the problem of multiplying matrices into smaller subproblems and finds the most efficient way to do it.

"""