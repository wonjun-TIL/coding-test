N = int(input())

alpha = dict()

for _ in range(N):
    new_voca = input()

    i = 1
    while new_voca:
        voca = new_voca[-1]
        new_voca = new_voca[:-1]
        if voca in alpha:
            alpha[voca] += i
        else:
            alpha[voca] = i
        i *= 10

sorted_dict = dict(sorted(alpha.items(), key=lambda item: item[1], reverse=True))

# print(sorted_dict)

num = 9
result = 0
for key, value in sorted_dict.items():
    # print(num, value)
    result += num*value
    num -= 1
print(result)