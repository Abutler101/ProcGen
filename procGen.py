#[TIME,TYPE_OF_SQUARE,DIRECTION,SPEED]
type= ["enemy","friend"]
dirs=["D","L","U","R"]
sp=55
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
def DEAS(x):
    DEAS=[
        [4.00, "enemy", "D", 55],
        [4.25, "enemy", "D", 55],
        [4.50, "enemy", "L", 55],
        [4.75, "enemy", "L", 55],
        [5.00, "enemy", "U", 55],
        [5.25, "enemy", "U", 55],
        [5.50, "enemy", "R", 55],
        [5.75, "enemy", "R", 55]
        ]
