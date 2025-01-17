# Matrix Operations Program

This Python program allows users to perform basic operations on matrices of up to 4x4 in size. The operations include matrix addition, subtraction, multiplication, determinant calculation, and finding the inverse of a square matrix.

## Features

1. **Matrix Addition**: Add two matrices of the same size (up to 4x4).
2. **Matrix Subtraction**: Subtract one matrix from another of the same size (up to 4x4).
3. **Matrix Multiplication**: Multiply two compatible matrices (up to 4x4).
4. **Determinant Calculation**: Compute the determinant of a square matrix (up to 4x4).
5. **Matrix Inversion**: Find the inverse of a square matrix (up to 4x4), if it exists.

## Requirements

- Python 3.6 or higher.
- No external libraries are required.

## Usage

1. Clone the repository or copy the program file.
2. Run the program using Python:
   
   ```bash
   python matrix_operations.py
   ```
3. Follow the on-screen instructions to choose an operation and input matrix values.

## Input Constraints

- The maximum matrix size is 4x4.
- Matrix elements must be integers.
- For determinant and inverse calculations, the input matrix must be square.
- If the determinant of a matrix is zero, its inverse does not exist.

## Example

### Matrix Addition

Input:
```
Pilih operasi:
1. Penjumlahan Matriks
2. Pengurangan Matriks
3. Perkalian Matriks
4. Determinan Matriks
5. Invers Matriks
6. Keluar
Masukkan pilihan: 1
Masukkan ukuran matriks (n m): 2 2
Masukkan elemen matriks A:
[1][1]: 1
[1][2]: 2
[2][1]: 3
[2][2]: 4
Masukkan elemen matriks B:
[1][1]: 5
[1][2]: 6
[2][1]: 7
[2][2]: 8
```

Output:
```
Hasil Penjumlahan Matriks:
6 8
10 12
```

## Error Handling

- If the input matrix size exceeds 4x4, the program will display an error message: `"Ukuran matriks maksimal adalah 4x4."`
- If invalid inputs are provided, the program will prompt the user to try again.

## License

This project is licensed under the MIT License.

## Author

Developed by Wyatt Matthew.
