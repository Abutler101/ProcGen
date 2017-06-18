#[TIME,TYPE_OF_SQUARE,DIRECTION,SPEED]
type= ["enemy","friend"]
dirs=["D","L","U","R"]
level=[]
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
    ],
'''
##########################Pre-built blocks
def DEAS(T,S):
    DEAS=[
        [T+0.00, "enemy", "D", S],
        [T+0.25, "enemy", "D", S],
        [T+0.50, "enemy", "L", S],
        [T+0.75, "enemy", "L", S],
        [T+1.00, "enemy", "U", S],
        [T+1.25, "enemy", "U", S],
        [T+1.50, "enemy", "R", S],
        [T+1.75, "enemy", "R", S]
        ]
def FEOS(T,S,D):
    FEOS=[
        [T+0.00, "enemy", D, S],
        [T+0.25, "enemy", D, S],
        [T+0.50, "enemy", D, S],
        [T+0.75, "enemy", D, S]
        ]
def TEOS(T,S,D):
    FEOS=[
        [T+0.00, "enemy", D, S],
        [T+0.25, "enemy", D, S],
        ]
