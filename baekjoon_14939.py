# 10줄의 입력 받기
grid = []
for _ in range(10):
    row = input().strip()  # 입력된 문자열의 양 끝 공백 제거
    grid.append(list(row))  # 각 줄을 리스트로 변환하여 10x10 리스트에 추가


grid2 =  [arr[:] for arr in grid]



def turn_one_switch(row, col):
    if grid[row][col] == '#':
        grid[row][col] = 'O'
    else:
        grid[row][col] = '#'




def turn_switch(row, col):

    turn_one_switch(row, col)
    if not is_out_bound(row-1, col):
        turn_one_switch(row-1, col)
    if not is_out_bound(row+1, col):
        turn_one_switch(row+1, col)
    if not is_out_bound(row, col-1):
        turn_one_switch(row, col-1)
    if not is_out_bound(row, col+1):
        turn_one_switch(row, col+1)




def turn_first_row_switch(flag_list):
    for col, flag in enumerate(flag_list):
        if flag == True:
            turn_switch(0, col)



def is_out_bound(row, col):
    if 0 <= row and row < 10 and 0<= col and col < 10:
        return False
    else:
        return True



def is_up_on(row, col):
    if grid[row-1][col] == 'O':
        return True
    else:
        return False



def is_night():
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'O':
                return False
            
    return True
            



result_list = []

# 10x10 리스트 출력
for i0 in [True, False]:
    for i1 in [True, False]:
        for i2 in [True, False]:
            for i3 in [True, False]:
                for i4 in [True, False]:
                    for i5 in [True, False]:
                        for i6 in [True, False]:
                            for i7 in [True, False]:
                                for i8 in [True, False]:
                                    for i9 in [True, False]:
                                        # 맨 윗줄 1024 개의 경우의 수

                                        grid =  [arr[:] for arr in grid2]

                                        turn_first_row_switch([i0, i1, i2, i3, i4, i5, i6, i7, i8, i9])
                                        
                                        result = sum([i0, i1, i2, i3, i4, i5, i6, i7, i8, i9])
                                        # print(result)
                                        # 2번째 줄부터 
                                        for row in range(1, 10):
                                            # 모든 열을 확인
                                            for col in range(0, 10):
                                                # 각 열의 윗쪽 값이 켜져있으면 끔
                                                if is_up_on(row, col):
                                                    # 스위치 누름
                                                    turn_switch(row, col)
                                                    result += 1
                                                else:
                                                    pass
                                        if is_night():
                                            result_list.append(result)

if len(result_list) > 0:
    print(min(result_list))
else:
    print(-1)
