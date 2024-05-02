import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_sum(N, M):
    prime_numbers = [i for i in range(2, 1001) if isPrime(i)]  # Tạo danh sách số nguyên tố từ 2 đến 1000
    result = []
    count = 0
    for i in range(len(prime_numbers)):
        if count == M:  # Kiểm tra nếu đã tìm đủ M số nguyên tố
            break
        for j in range(i, len(prime_numbers)):
            if sum(prime_numbers[i:j+1]) == N:  # Nếu tổng của M số nguyên tố này bằng N
                result = prime_numbers[i:j+1]
                count = M
                break
            elif sum(prime_numbers[i:j+1]) > N:  # Nếu tổng vượt quá N thì thoát vòng lặp
                break
    if count == M:
        return result
    else:
        return None

# Nhập giá trị của N và M từ người dùng
N = int(input("Nhập N: "))
M = int(input("Nhập M: "))

# Kiểm tra và in kết quả
result = find_prime_sum(N, M)
if result:
    print("Kết quả: Thoả mãn")
    print("Các số nguyên tố là:", result)
else:
    print("Kết quả: Không thoả mãn")
