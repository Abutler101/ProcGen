from random import randint as ran
#[TIME,TYPE_OF_SQUARE,DIRECTION,SPEED]
type= ["enemy","friend"]
dirs=['"D"','"L"','"U"','"R"']
level=[]
formattedOutput ='''{
    "rankC": 1,
    "rankB": 100,
    "rankA": 180,
    "rankA+": 280'''
speed = 0
dur = 64
#Template
'''
{
    "rankC": 1,
    "rankB": 100,
    "rankA": 180,
    "rankA+": 280,
    "1":
    [
        [4.0,"enemy",],
        [],
        [],
        [],
        [],
        [],
    ],
    "2":
    [
        [],
        [],
        [],
        [],
        [],
        [],
    ]
}
'''
##########################Pre-built blocks
def DEAS(T,S): #FILLS 2 seconds
    DEAS=[
        [T+0.00, '"enemy"', '"D"', S],
        [T+0.25, '"enemy"', '"D"', S],
        [T+0.50, '"enemy"', '"L"', S],
        [T+0.75, '"enemy"', '"L"', S],
        [T+1.00, '"enemy"', '"U"', S],
        [T+1.25, '"enemy"', '"U"', S],
        [T+1.50, '"enemy"', '"R"', S],
        [T+1.75, '"enemy"', '"R"', S]
        ]
    return(DEAS)

def OEAS(T,S): #FILLS 1 second
    OEAS=[
        [T+0.00, '"enemy"', '"D"', S],
        [T+0.25, '"enemy"', '"L"', S],
        [T+0.50, '"enemy"', '"U"', S],
        [T+0.75, '"enemy"', '"R"', S]
        ]
    return(OEAS)

def FEOS(T,S,D): #FILLS 1 second
    FEOS=[
        [T+0.00, '"enemy"', dirs[D], S],
        [T+0.25, 'enemy"', dirs[D], S],
        [T+0.50, '"enemy"', dirs[D], S],
        [T+0.75, '"enemy"', dirs[D], S]
        ]
    return(FEOS)

def TEOS(T,S,D): #FILLS 1/4 seconds
    TEOS=[
        [T+0.00, '"enemy"', dirs[D], S],
        [T+0.25, '"enemy"', dirs[D], S],
        ]
    return(TEOS)

def TEOPS(T,S,D): #FILLS 1 second
    TEOPS=[
        [T+0.00, '"enemy"', dirs[D], S],
        [T+0.25, '"enemy"', dirs[D], S]
        ]
    if TEOPS[0][2] == '"D"':
        TEOPS.append([T+0.50, '"enemy"', '"U"', S])
        TEOPS.append([T+0.75, '"enemy"', '"U"', S])
    elif TEOPS[0][2] == '"U"':
        TEOPS.append([T+0.50, '"enemy"', '"D"', S])
        TEOPS.append([T+0.75, '"enemy"', '"D"', S])
    elif TEOPS[0][2] == '"L"':
        TEOPS.append([T+0.50, '"enemy"', '"R"', S])
        TEOPS.append([T+0.75, '"enemy"', '"R"', S])
    elif TEOPS[0][2] == '"R"':
        TEOPS.append([T+0.50, '"enemy"', '"L"', S])
        TEOPS.append([T+0.75, '"enemy"', '"L"', S])
    return(TEOPS)

def DFAS(T,S): #FILLS 2 seconds
    DFAS=[
        [T+0.00, '"friend"', '"D"', S],
        [T+0.25, '"friend"', '"D"', S],
        [T+0.50, '"friend"', '"L"', S],
        [T+0.75, '"friend"', '"L"', S],
        [T+1.00, '"friend"', '"U"', S],
        [T+1.25, '"friend"', '"U"', S],
        [T+1.50, '"friend"', '"R"', S],
        [T+1.75, '"friend"', '"R"', S]
        ]
    return(DFAS)

def OFAS(T,S): #FILLS 1 second
    OFAS=[
        [T+0.00, '"friend"', '"D"', S],
        [T+0.25, '"friend"', '"L"', S],
        [T+0.50, '"friend"', '"U"', S],
        [T+0.75, '"friend"', '"R"', S]
        ]
    return(OFAS)

def FFOS(T,S,D): #FILLS 1 second
    FFOS=[
        [T+0.00, '"friend"', dirs[D], S],
        [T+0.25, '"friend"', dirs[D], S],
        [T+0.50, '"friend"', dirs[D], S],
        [T+0.75, '"friend"', dirs[D], S]
        ]
    return(FFOS)

def TFOS(T,S,D): #FILLS 1/4 seconds
    TFOS=[
        [T+0.00, '"friend"', dirs[D], S],
        [T+0.25, '"friend"', dirs[D], S],
        ]
    return(TFOS)

def TFOPS(T,S,D): #FILLS 1 second
    TFOPS=[
        [T+0.00, '"friend"', dirs[D], S],
        [T+0.25, '"friend"', dirs[D], S]
        ]
    if TFOPS[0][2] == '"D"':
        TFOPS.append([T+0.50, '"friend"', '"U"', S])
        TFOPS.append([T+0.75, '"friend"', '"U"', S])
    elif TFOPS[0][2] == '"U"':
        TFOPS.append([T+0.50, '"friend"', '"D"', S])
        TFOPS.append([T+0.75, '"friend"', '"D"', S])
    elif TFOPS[0][2] == '"L"':
        TFOPS.append([T+0.50, '"friend"', '"R"', S])
        TFOPS.append([T+0.75, '"friend"', '"R"', S])
    elif TFOPS[0][2] == '"R"':
        TFOPS.append([T+0.50, '"friend"', '"L"', S])
        TFOPS.append([T+0.75, '"friend"', '"L"', S])
    return(TFOPS)
##########################Start proc Gen
speed = input("Enter Speed ->")
for i in range(dur):
    select = ran(1,10)
    
    if select == 1:
        level.append(DEAS(i,speed))
        i+=1
        
    elif select == 2:
        level.append(OEAS(i,speed))
        
    elif select == 3:
        temp = ran(0,3)
        level.append(FEOS(i,speed,temp))
        
    elif select == 4:
        for Q in range(4):
            temp = ran(0,3)
            level.append(TEOS(i,speed,temp))
            
    elif select == 5:
        temp = ran(0,3)
        level.append(TEOPS(i,speed,temp))
    ##
    if i % 2 ==0:
        
        if select == 6:
            level.append(DFAS(i,speed))
            i+=1
            
        elif select == 7:
            level.append(OFAS(i,speed))
            
        elif select == 8:
            temp = ran(0,3)
            level.append(FFOS(i,speed,temp))
            
        elif select == 9:
            for Q in range(4):
                temp = ran(0,3)
                level.append(TFOS(i,speed,temp))
                
        elif select == 10:
            temp = ran(0,3)
            level.append(TFOPS(i,speed,temp))
            
    else:
        i-=1
#for y in range(len(level)):
#    for z in range(len(level[y])):
#        print(level[y][z])

##########################Start formatting
for x in range(len(level)):
    temp = '\n    "'+str(x+1)+":"+'"\n    [\n'
    for w in range(len(level[x])):
        temp = temp+"       "+str(level[x][w])
        if (w+1) != len(level[x]):
            temp = temp+",\n"
        else:
            temp = temp+"\n"
    temp = temp + "    ]"
    if (x+1) != len(level):
        temp = temp+","
    #print(temp)
    formattedOutput = formattedOutput + temp
formattedOutput = formattedOutput + "\n}"
print(formattedOutput)
