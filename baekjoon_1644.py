N = int(input())

def find_prime_num(x):

    num_list = [1 for i in range(x+1)]
    num_list[0] = 0
    num_list[1] = 0
    
    for i in range(2, int((x+1)**0.5) +1):
        if num_list[i] == 1:
            for j in range(2*i, x+1, i):
                num_list[j] = 0
    
    prime_list =[]

    for i in range(x, -1, -1):
        if num_list[i] == 1:
            prime_list.append(i)

    return prime_list



prime_list = find_prime_num(N)

start = 0
end = 1

result = 0
while end <= len(prime_list):
    hap = sum(prime_list[start:end])

    if hap == N:
        result += 1
        start += 1
        continue
    elif hap < N:
        end += 1
        continue
    elif hap > N:
        start += 1
        continue

print(result)
