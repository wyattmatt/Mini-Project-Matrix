def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:.2f}" if isinstance(val, float) else str(val) for val in row))
    print()

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return sum(((-1) ** c) * matrix[0][c] * determinant([row[:c] + row[c+1:] for row in matrix[1:]]) for c in range(len(matrix)))

def inverse_matrix(matrix):
    det = determinant(matrix)
    if det == 0:
        return None
    cofactors = [[((-1) ** (r + c)) * determinant([row[:c] + row[c+1:] for row in matrix[:r] + matrix[r+1:]]) for c in range(len(matrix))] for r in range(len(matrix))]
    cofactors = list(map(list, zip(*cofactors)))  # Transpose
    return [[cofactors[r][c] / det for c in range(len(cofactors))] for r in range(len(cofactors))]

def input_matrix(rows, cols):
    if rows > 4 or cols > 4:
        raise ValueError("Ukuran matriks maksimal adalah 4x4.")
    print(f"Masukkan elemen matriks ({rows}x{cols}):")
    return [[int(input(f"[{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)]

def main():
    operations = {
        1: ("Penjumlahan Matriks", add_matrices),
        2: ("Pengurangan Matriks", subtract_matrices),
        3: ("Perkalian Matriks", multiply_matrices),
        4: ("Determinan Matriks", determinant),
        5: ("Invers Matriks", inverse_matrix)
    }

    while True:
        print("Pilih operasi:")
        for i, (name, _) in operations.items():
            print(f"{i}. {name}")
        print("6. Keluar")

        try:
            choice = int(input("Masukkan pilihan: "))
            if choice == 6:
                print("Terima kasih telah menggunakan program.")
                break

            if choice in [1, 2, 3]:
                n, m = map(int, input("Masukkan ukuran matriks (n m): ").split())
                A = input_matrix(n, m)

                if choice == 3:
                    p = int(input("Masukkan jumlah kolom matriks B: "))
                    B = input_matrix(m, p)
                else:
                    B = input_matrix(n, m)

                print(f"Hasil {operations[choice][0]}:")
                print_matrix(operations[choice][1](A, B))

            elif choice == 4:
                n = int(input("Masukkan ukuran matriks persegi (n): "))
                if n > 4:
                    raise ValueError("Ukuran matriks maksimal adalah 4x4.")
                matrix = input_matrix(n, n)
                print(f"Determinan matriks adalah: {determinant(matrix)}")

            elif choice == 5:
                n = int(input("Masukkan ukuran matriks persegi (n): "))
                if n > 4:
                    raise ValueError("Ukuran matriks maksimal adalah 4x4.")
                matrix = input_matrix(n, n)
                inv = inverse_matrix(matrix)
                if inv:
                    print("Invers matriks adalah:")
                    print_matrix(inv)
                else:
                    print("Matriks tidak memiliki invers (determinan 0).")
        except ValueError as ve:
            print(f"Kesalahan: {ve}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
