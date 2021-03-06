from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname,"r")
    fString = f.read()
    fList = fString.split("\n")
    # print(fList)

    i = 0
    while (i < len(fList)):
        if fList[i] == "line":
            p = fList[i+1].split(" ")
            add_edge(points,int(p[0]),int(p[1]),int(p[2]),int(p[3]),int(p[4]),int(p[5]))
            i += 1

        elif fList[i] == "ident":
            ident(transform)

        elif fList[i] == "scale":
            n = fList[i+1].split(" ")
            m = make_scale(int(n[0]),int(n[1]),int(n[2]))
            matrix_mult(m, transform)
            i += 1

        elif fList[i] == "move":
            n = fList[i+1].split(" ")
            m = make_translate(int(n[0]),int(n[1]),int(n[2]))
            matrix_mult(m, transform)
            i += 1

        elif fList[i] == "rotate":
            n = fList[i+1].split(" ")
            m = []
            if n[0] == "x":
                print("xrotate "+n[1])
                m = make_rotX(int(n[1]))
                print_matrix(m)
            elif n[0] == "y":
                print("yrotate "+n[1])
                m = make_rotY(int(n[1]))
                print_matrix(m)
            elif n[0] == "z":
                print("zrotate "+n[1])
                m = make_rotZ(int(n[1]))
                print_matrix(m)
            print("before")
            print_matrix(transform)
            matrix_mult(m, transform)
            print("after")
            print_matrix(transform)
            i += 1

        elif fList[i] == "apply":
            print("points")
            matrix_mult(transform,points)
            print_matrix(points)

        elif fList[i] == "display":
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)

        elif fList[i] == "save":
            clear_screen(screen)
            draw_lines(points,screen,color)
            save_extension(screen,fList[i+1])
            i += 1

        elif fList[i] == "quit":
            break

        i += 1
