"""Dicts for different Trees that can be drawn by the SpaceTurtle (not all work properly yet)"""

DRAGON ={
    "A":"F", 
    "D": 10, 
    "S":5, 
    "AN":90, 
    "R": {
        "F": "F+G", 
        "G": "F-G"
    }
}

PLANT ={
    "A":"X", 
    "D": 5, 
    "S": 5, 
    "AN":25, 
    "R": {
        "X": "F+[[X]-X]-F[-FX]+X", 
        "F": "FF"
    }
}
BUSH_B = {
    "A":"F",
    "D":5,
    "S":10,
    "AN": 22.5,
    "R": {
        "F":"FF+[+F-F-F]-[-F+F+F]"
    }
}

XMAS = {
    "A":"VZFFF",
    "D":5,
    "S":10,
    "AN": 20,
    "R":{
        "V":"[+++W][---W]YV",
        "W":"+X[-W]Z",
        "X":"-W[+X]Z",
        "Y":"YZ",
        "Z":"[-FFF][+FFF]F"
    }
    
}
PENTA = {
    "A":"F++F++F++F++F",
    "D":2,
    "S":40,
    "AN":36,
    "R":{
        "F":"F++F++F|F-F++F"
    }
}

SIERPINSKI =  {
    "A":"F−G−G",
    "D":5,
    "S":10,
    "AN":120,
    "R":{
        "F":"F−G+F+G−F",
        "G":"GG"
    }    
}

SIERPINSKI2 =  {
    "A":"F",
    "D":5,
    "S":10,
    "AN":60,
    "R":{
        "F":"G-F−G",
        "G":"F+G+F"
    }    
}

BIN_TREE = {
    "A":"F",
    "D":5,
    "S":10,
    "AN":60,
    "R":{
        "F":"G[F]F",
        "G":"GG"
    } 
}




#     # Length factor????
#     #length factor = 1.36
#     LEAF = {
#         "A":"A",
#         "D":10,
#         "R":{
#             "F":"F",
#             "A":"F[+X]FB",
#             "B":"F[-Y]FA",
#             "X":"A",
#             "Y":"B"},
#         "AN":45,
#         "S":25
#         }
