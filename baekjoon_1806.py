N, S = map(int, input().split())

seq = list(map(int, input().split()))

start = 0
end = 0

length = len(seq)

min_len = length + 1
hap = seq[0]

while True:

    if hap >= S:
        if end - start + 1 < min_len:
            min_len = end - start + 1
        hap -= seq[start]
        start += 1
        
    else:
        end += 1
        if end == length:
            break
        hap += seq[end]

if min_len == len(seq) + 1:
    print(0)
else:
    print(min_len)

