

T = int(input())

def turn_up(cube, di):
    if di == "+":
        temp = cube[0][0]
        cube[0][0] = cube[0][6]
        cube[0][6] = cube[0][8]
        cube[0][8] = cube[0][2]
        cube[0][2] = temp

        temp = cube[0][1]
        cube[0][1] = cube[0][3]
        cube[0][3] = cube[0][7]
        cube[0][7] = cube[0][5]
        cube[0][5] = temp

        temp = [cube[3][0], cube[3][1], cube[3][2]]
        cube[3][0], cube[3][1], cube[3][2] = cube[4][0], cube[4][1], cube[4][2]
        cube[4][0], cube[4][1], cube[4][2] = cube[2][0], cube[2][1], cube[2][2]
        cube[2][0], cube[2][1], cube[2][2] = cube[5][0], cube[5][1], cube[5][2]
        cube[5][0], cube[5][1], cube[5][2] = temp[0], temp[1], temp[2]        

    if di == "-":
        temp = cube[0][0]
        cube[0][0] = cube[0][2]
        cube[0][2] = cube[0][8]
        cube[0][8] = cube[0][6]
        cube[0][6] = temp

        temp = cube[0][1]
        cube[0][1] = cube[0][5]
        cube[0][5] = cube[0][7]
        cube[0][7] = cube[0][3]
        cube[0][3] = temp

        temp = [cube[3][0], cube[3][1], cube[3][2]]
        cube[3][0], cube[3][1], cube[3][2] = cube[5][0], cube[5][1], cube[5][2]
        cube[5][0], cube[5][1], cube[5][2] = cube[2][0], cube[2][1], cube[2][2]
        cube[2][0], cube[2][1], cube[2][2] = cube[4][0], cube[4][1], cube[4][2]
        cube[4][0], cube[4][1], cube[4][2] = temp[0], temp[1], temp[2]


def turn_down(cube, di):
    if di == "+":
        temp = cube[1][0]
        cube[1][0] = cube[1][6]
        cube[1][6] = cube[1][8]
        cube[1][8] = cube[1][2]
        cube[1][2] = temp

        temp = cube[1][1]
        cube[1][1] = cube[1][3]
        cube[1][3] = cube[1][7]
        cube[1][7] = cube[1][5]
        cube[1][5] = temp

        temp = [cube[3][6], cube[3][7], cube[3][8]]
        cube[3][6], cube[3][7], cube[3][8] = cube[5][6], cube[5][7], cube[5][8]
        cube[5][6], cube[5][7], cube[5][8] = cube[2][6], cube[2][7], cube[2][8]
        cube[2][6], cube[2][7], cube[2][8] = cube[4][6], cube[4][7], cube[4][8]
        cube[4][6], cube[4][7], cube[4][8] = temp[0], temp[1], temp[2]        

    if di == "-":
        temp = cube[1][0]
        cube[1][0] = cube[1][2]
        cube[1][2] = cube[1][8]
        cube[1][8] = cube[1][6]
        cube[1][6] = temp

        temp = cube[1][1]
        cube[1][1] = cube[1][5]
        cube[1][5] = cube[1][7]
        cube[1][7] = cube[1][3]
        cube[1][3] = temp

        temp = [cube[3][6], cube[3][7], cube[3][8]]
        cube[3][6], cube[3][7], cube[3][8] = cube[4][6], cube[4][7], cube[4][8]
        cube[4][6], cube[4][7], cube[4][8] = cube[2][6], cube[2][7], cube[2][8]
        cube[2][6], cube[2][7], cube[2][8] = cube[5][6], cube[5][7], cube[5][8]
        cube[5][6], cube[5][7], cube[5][8] = temp[0], temp[1], temp[2]  



def turn_front(cube, di):
    if di == "+":
        temp = cube[2][0]
        cube[2][0] = cube[2][6]
        cube[2][6] = cube[2][8]
        cube[2][8] = cube[2][2]
        cube[2][2] = temp

        temp = cube[2][1]
        cube[2][1] = cube[2][3]
        cube[2][3] = cube[2][7]
        cube[2][7] = cube[2][5]
        cube[2][5] = temp

        temp = [cube[0][6], cube[0][7], cube[0][8]]
        cube[0][6], cube[0][7], cube[0][8] = cube[4][8], cube[4][5], cube[4][2]
        cube[4][8], cube[4][5], cube[4][2] = cube[1][6], cube[1][7], cube[1][8]
        cube[1][6], cube[1][7], cube[1][8] = cube[5][0], cube[5][3], cube[5][6]
        cube[5][0], cube[5][3], cube[5][6] = temp[0], temp[1], temp[2]        

    if di == "-":
        temp = cube[2][0]
        cube[2][0] = cube[2][2]
        cube[2][2] = cube[2][8]
        cube[2][8] = cube[2][6]
        cube[2][6] = temp

        temp = cube[2][1]
        cube[2][1] = cube[2][5]
        cube[2][5] = cube[2][7]
        cube[2][7] = cube[2][3]
        cube[2][3] = temp

        temp = [cube[0][6], cube[0][7], cube[0][8]]
        cube[0][6], cube[0][7], cube[0][8] = cube[5][0], cube[5][3], cube[5][6]
        cube[5][0], cube[5][3], cube[5][6] = cube[1][6], cube[1][7], cube[1][8]
        cube[1][6], cube[1][7], cube[1][8] = cube[4][8], cube[4][5], cube[4][2]
        cube[4][8], cube[4][5], cube[4][2] = temp[0], temp[1], temp[2]  




def turn_back(cube, di):
    if di == "+":
        temp = cube[3][0]
        cube[3][0] = cube[3][6]
        cube[3][6] = cube[3][8]
        cube[3][8] = cube[3][2]
        cube[3][2] = temp

        temp = cube[3][1]
        cube[3][1] = cube[3][3]
        cube[3][3] = cube[3][7]
        cube[3][7] = cube[3][5]
        cube[3][5] = temp

        temp = [cube[0][2], cube[0][1], cube[0][0]]
        cube[0][2], cube[0][1], cube[0][0] = cube[5][8], cube[5][5], cube[5][2]
        cube[5][8], cube[5][5], cube[5][2] = cube[1][2], cube[1][1], cube[1][0]
        cube[1][2], cube[1][1], cube[1][0] = cube[4][0], cube[4][3], cube[4][6]
        cube[4][0], cube[4][3], cube[4][6] = temp[0], temp[1], temp[2]        

    if di == "-":
        temp = cube[3][0]
        cube[3][0] = cube[3][2]
        cube[3][2] = cube[3][8]
        cube[3][8] = cube[3][6]
        cube[3][6] = temp

        temp = cube[3][1]
        cube[3][1] = cube[3][5]
        cube[3][5] = cube[3][7]
        cube[3][7] = cube[3][3]
        cube[3][3] = temp

        temp = [cube[0][2], cube[0][1], cube[0][0]]
        cube[0][2], cube[0][1], cube[0][0] = cube[4][0], cube[4][3], cube[4][6]
        cube[4][0], cube[4][3], cube[4][6] = cube[1][2], cube[1][1], cube[1][0]
        cube[1][2], cube[1][1], cube[1][0] = cube[5][8], cube[5][5], cube[5][2]
        cube[5][8], cube[5][5], cube[5][2] = temp[0], temp[1], temp[2]


def turn_left(cube, di):
    if di == "+":
        temp = cube[4][0]
        cube[4][0] = cube[4][6]
        cube[4][6] = cube[4][8]
        cube[4][8] = cube[4][2]
        cube[4][2] = temp

        temp = cube[4][1]
        cube[4][1] = cube[4][3]
        cube[4][3] = cube[4][7]
        cube[4][7] = cube[4][5]
        cube[4][5] = temp

        temp = [cube[0][0], cube[0][3], cube[0][6]]
        cube[0][0], cube[0][3], cube[0][6] = cube[3][8], cube[3][5], cube[3][2]
        cube[3][8], cube[3][5], cube[3][2] = cube[1][8], cube[1][5], cube[1][2]
        cube[1][8], cube[1][5], cube[1][2] = cube[2][0], cube[2][3], cube[2][6]
        cube[2][0], cube[2][3], cube[2][6] = temp[0], temp[1], temp[2]        

    if di == "-":
        temp = cube[4][0]
        cube[4][0] = cube[4][2]
        cube[4][2] = cube[4][8]
        cube[4][8] = cube[4][6]
        cube[4][6] = temp

        temp = cube[4][1]
        cube[4][1] = cube[4][5]
        cube[4][5] = cube[4][7]
        cube[4][7] = cube[4][3]
        cube[4][3] = temp

        temp = [cube[0][0], cube[0][3], cube[0][6]]
        cube[0][0], cube[0][3], cube[0][6] = cube[2][0], cube[2][3], cube[2][6]
        cube[2][0], cube[2][3], cube[2][6] = cube[1][8], cube[1][5], cube[1][2]
        cube[1][8], cube[1][5], cube[1][2] = cube[3][8], cube[3][5], cube[3][2]
        cube[3][8], cube[3][5], cube[3][2] = temp[0], temp[1], temp[2] 



def turn_right(cube, di):
    if di == "+":
        temp = cube[5][0]
        cube[5][0] = cube[5][6]
        cube[5][6] = cube[5][8]
        cube[5][8] = cube[5][2]
        cube[5][2] = temp

        temp = cube[5][1]
        cube[5][1] = cube[5][3]
        cube[5][3] = cube[5][7]
        cube[5][7] = cube[5][5]
        cube[5][5] = temp

        temp = [cube[0][8], cube[0][5], cube[0][2]]
        cube[0][8], cube[0][5], cube[0][2] = cube[2][8], cube[2][5], cube[2][2]
        cube[2][8], cube[2][5], cube[2][2] = cube[1][0], cube[1][3], cube[1][6]
        cube[1][0], cube[1][3], cube[1][6] = cube[3][0], cube[3][3], cube[3][6]
        cube[3][0], cube[3][3], cube[3][6] = temp[0], temp[1], temp[2]        

    if di == "-":
        temp = cube[5][0]
        cube[5][0] = cube[5][2]
        cube[5][2] = cube[5][8]
        cube[5][8] = cube[5][6]
        cube[5][6] = temp

        temp = cube[5][1]
        cube[5][1] = cube[5][5]
        cube[5][5] = cube[5][7]
        cube[5][7] = cube[5][3]
        cube[5][3] = temp

        temp = [cube[0][8], cube[0][5], cube[0][2]]
        cube[0][8], cube[0][5], cube[0][2] = cube[3][0], cube[3][3], cube[3][6]
        cube[3][0], cube[3][3], cube[3][6] = cube[1][0], cube[1][3], cube[1][6]
        cube[1][0], cube[1][3], cube[1][6] = cube[2][8], cube[2][5], cube[2][2]
        cube[2][8], cube[2][5], cube[2][2] = temp[0], temp[1], temp[2] 



for _ in range(T):

    # 위 아래 앞 뒤 왼 오 
    cube = [[j for i in range(9)] for j in ['w', 'y', 'r', 'o', 'g', 'b']] # 0: 흰, 1: 노, 2: 빨, 3: 주, 4: 초, 5: 파    

    n = int(input())
    turns = list(input().split())

    for turn in turns:
        if turn[0] == "U":
            turn_up(cube, turn[1])
        elif turn[0] == "D":
            turn_down(cube, turn[1])
        elif turn[0] == "F":
            turn_front(cube, turn[1])
        elif turn[0] == "B":
            turn_back(cube, turn[1])
        elif turn[0] == "L":
            turn_left(cube, turn[1])
        elif turn[0] == "R":
            turn_right(cube, turn[1])

    for i in range(9):
        print(cube[0][i], end = "")
        if (i+1) % 3 == 0:
            print()



       
    
