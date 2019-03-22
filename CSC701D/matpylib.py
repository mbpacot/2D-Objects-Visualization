'''
Authors:    Glenn Paul P. Gara
            Mark Phil B. Pacot
            Marvin C. Santillan
'''

import matplotlib.pyplot as plt
import math

############################### Math operations ###############################

# exponent
def exp(x, y):
    return x ** y

# calculate square root of a number
def sqrt(x):
    return x ** 0.5

# Generate list of zeros
def zeros(a):
    return [0] * a

# Generate list of values
def linspace(start, stop, n):
    if n == 1:
        yield stop
        return
    h = (stop - start) / (n - 1)
    for i in range(n):
        yield start + h * i

############################### Matrix operations ###############################

# matrix shape
def shape(m):
    row_sizes = []
    for i in range(len(m)):
        row_sizes.append(len(m[i]))

    if not isinstance(m, list):
        print('Error: Input must be in a list format.')
    elif len(set(row_sizes)) == 1:
        row_size = len(m)
        column_size = len(m[0])
        return row_size, column_size
    else:
        print('Error: Matrix rows are not uniform in size.')

# matrix transpose
def transpose(m):
    row_sizes = []
    trans_list = []
    for i in range(len(m)):
        row_sizes.append(len(m[i]))

    if not isinstance(m, list):
        print('Error: Input must be in a list format.')
    elif len(set(row_sizes)) == 1:
        result = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
        for row in result:
            trans_list.append(row)
        return trans_list
    else:
        print('Error: Matrix rows are not uniform in size.')

# matrix addition
def add(m1, m2):
    flist1, flist2 = [], []
    sum_flist = []
    matrix = []

    for i in range(len(m1)):
        flist1.extend(m1[i])
        flist2.extend(m2[i])

    if len(flist1) == len(flist2):
        for i in range(len(flist1)):
            sum_flist.append(flist1[i] + flist2[i])
        matrix = []
        for i in range(0,len(sum_flist),len(sum_flist)//shape(m1)[0]):
            split = sum_flist[i:i+len(sum_flist)//shape(m1)[0]]
            matrix.append(split)
        return matrix
    else:
        print('Error: The two matrices are not in the same shape.')

# matrix subtraction
def sub(m1, m2):
    flist1, flist2 = [], []
    sum_flist = []
    matrix = []

    for i in range(len(m1)):
        flist1.extend(m1[i])
        flist2.extend(m2[i])

    if len(flist1) == len(flist2):
        for i in range(len(flist1)):
            sum_flist.append(flist1[i] - flist2[i])
        matrix = []
        for i in range(0,len(sum_flist),len(sum_flist)//shape(m1)[0]):
            split = sum_flist[i:i+len(sum_flist)//shape(m1)[0]]
            matrix.append(split)
        return matrix
    else:
        print('Error: The two matrices are not in the same shape.')

# element-wise matrix multiplication
def mul(m1, m2):
    flist1, flist2 = [], []
    sum_flist = []
    matrix = []

    for i in range(len(m1)):
        flist1.extend(m1[i])
        flist2.extend(m2[i])

    if len(flist1) == len(flist2):
        for i in range(len(flist1)):
            sum_flist.append(flist1[i] * flist2[i])

        matrix = []
        for i in range(0,len(sum_flist),len(sum_flist)//shape(m1)[0]):
            split = sum_flist[i:i+len(sum_flist)//shape(m1)[0]]
            matrix.append(split)

        return matrix

    else:
        print('Error: The two matrices are not in the same shape.')

# dot product of a matrix
def dot(m1, m2):
    row_sizes1, row_sizes2 = [], []
    row_size, column_size = len(m1), len(m2[0])
    trans_list = []
    mult = []

    for i in range(len(m1)):
        row_sizes1.append(len(m1[i]))
    for i in range(len(m2)):
        row_sizes2.append(len(m2[i]))

    if len(set(row_sizes1)) == 1 and len(set(row_sizes2)) == 1:
        mtrans = transpose(m2)

        if len(mtrans[0]) == len(m1[0]):
            for i in range(len(m1)):
                for j in range(len(mtrans)):
                    for k in range(len(m1[i])):
                        mult.append(m1[i][k]*mtrans[j][k])

            tmp1, tmp2 = [], []
            added = []
            matrix = []
            for i in range(0,len(mult),len(mult)//shape(m1)[0]):
                split = mult[i:i+len(mult)//shape(m1)[0]]
                tmp1.append(split)

            for i, j in enumerate(tmp1):
                for i in range(0,len(j),len(j)//shape(m2)[1]):
                    split = j[i:i+len(j)//shape(m2)[1]]
                    tmp2.append(split)

            for i in range(len(tmp2)):
                added.append(sum(tmp2[i]))

            for i in range(0,len(added),len(added)//shape(m1)[0]):
                split = added[i:i+len(added)//shape(m1)[0]]
                matrix.append(split)

            return matrix
        else:
            print('Error: The two matrices should be N x M and M x D in shape.')

    else:
        print('Error: Rows are not uniform in size.')

############################### Creating shapes ###############################

def circle(a, b, radius):
    x = list(linspace((a-radius), (a+radius), radius))
    y1, y2 = [], []

    for i in x:
        y1.append(b + sqrt(exp(radius, 2) - exp(i-a, 2)))
        y2.append(b - sqrt(exp(radius, 2) - exp(i-a, 2)))

    x = x*2
    y = y1 + y2

    points = []
    for i,j in zip(x,y):
        points.append([i,j])

    return points

def ellipse(a, b, cx, cy):
    x1 = list(linspace(-a, a, a))
    x2 = []
    y1, y2 = [], []

    for i in x1:
        x2.append(i + cx)
        y1.append((b/a * sqrt(exp(a,2) - exp(i,2))) + cy)
        y2.append(-(b/a * sqrt(exp(a,2) - exp(i,2))) + cy)

    x = x2 * 2
    y = y1 + y2

    points = []
    for i,j in zip(x,y):
        points.append([i,j])

    return points

def parabola(a, b, c, width):
    x = list(linspace(-width, width, width))
    y = []

    for i in x:
        y.append(a*exp(i, 2) + (b*i) + c)

    points = []
    for i,j in zip(x,y):
        points.append([i,j])

    return points

def hyperbola(a, b, cx, cy, dir):
    x1 = list(linspace(-a, a, a))
    x2 = []
    y1, y2 = [], []

    for i in x1:
        x2.append(i + cx)
        y1.append((b/a * sqrt(exp(a,2) + exp(i,2))) + cy)
        y2.append(-(b/a * sqrt(exp(a,2) + exp(i,2))) + cy)

    points = []
    if dir == 'h':
        x = x2 * 2
        y = y1 + y2
        for i,j in zip(x,y):
            points.append([i,j])
        return points
    elif dir == 'v':
        x = y1 + y2
        y = x2 * 2
        for i,j in zip(x,y):
            points.append([i,j])
        return points
    else:
        print('Error: direction must be specified')

############################### Drawing shapes ###############################

def drawpolygon(points, label):
    plt.style.use('bmh')
    plt.figure(figsize=(5,5))
    plt.xlim(-1000, 1000)
    plt.ylim(-1000, 1000)
    plt.plot(list(linspace(-1000,1000,2000)), zeros(2000), color='black', linestyle='-', linewidth=1.0)
    plt.plot(zeros(2000), list(linspace(-1000,1000,2000)), color='black', linestyle='-', linewidth=1.0)
    line = plt.Polygon(points, fill=None, edgecolor='green', linewidth=2.0)
    plt.title(label.upper())
    plt.gca().set_aspect('equal', adjustable='box')
    plt.gca().add_line(line)
    plt.show()

def drawconics(points, label):
    x, y = [], []

    for i in points:
        x.append(i[0])
        y.append(i[1])

    if label.lower() == 'circle' or label.lower() == 'ellipse' or label.lower() == 'hyperbola':
        x1, x2 = [], []
        y1, y2 = [], []
        for i,j in zip(x[0:len(x)//2], y[0:len(y)//2]):
            x1.append(i)
            y1.append(j)
        for i,j in zip(x[len(x)//2:len(x)], y[len(y)//2:len(y)]):
            x2.append(i)
            y2.append(j)
        plt.style.use('bmh')
        plt.figure(figsize=(5,5))
        plt.xlim(-1000, 1000)
        plt.ylim(-1000, 1000)
        plt.plot(list(linspace(-1000,1000,2000)), [0]*2000, color='black', linestyle='-', linewidth=1.0)
        plt.plot([0]*2000, list(linspace(-1000,1000,2000)), color='black', linestyle='-', linewidth=1.0)
        plt.plot(x1, y1, '-g')
        plt.plot(x2, y2, '-g')
        plt.title(label.upper())
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

    elif label == 'Parabola':
        plt.style.use('bmh')
        plt.figure(figsize=(5,5))
        plt.xlim(-1000, 1000)
        plt.ylim(-1000, 1000)
        plt.plot(list(linspace(-1000,1000,2000)), [0]*2000, color='black', linestyle='-', linewidth=1.0)
        plt.plot([0]*2000, list(linspace(-1000,1000,2000)), color='black', linestyle='-', linewidth=1.0)
        plt.plot(x, y, '-g')
        plt.title(label.upper())
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()
    else:
        print('Error: a label should be circle, ellipse, parabola or hyperbola')

############################### Transformations ###############################

def translate(points, tx, ty):
    t = []
    for i in points:
        t.extend(add([i], [[tx, ty]]))
    return t

def scale(points, sx, sy):
    s = []
    for i in points:
        s.extend(dot([i], [[sx,0], [0,sy]]))
    return s

def rotate(points, degree, rotation):
    r = []

    _cos = round(math.cos(math.radians(degree)), 3)
    _sin = round(math.sin(math.radians(degree)), 3)

    if rotation == 'cc':
        for i in points:
            r.extend(dot([i], [[_cos,_sin], [-(_sin), _cos]]))
    elif rotation == 'cw':
        for i in points:
            r.extend(dot([i], [[_cos,-(_sin)], [_sin, _cos]]))
    else:
        print('Error: input a valid rotation.')
    return r

def shear(points, shr, pos):
    sh = []
    if pos == 'x':
        for i in points:
            sh.extend(dot([i], [[1,0], [shr,1]]))
    elif pos == 'y':
        for i in points:
            sh.extend(dot([i], [[1,shr], [0,1]]))
    else:
        print('Error: input must be a string x or y')
    return sh

def reflect(points, pos):
    r = []
    if pos == 'x':
        for i in points:
            r.extend(dot([i], [[1,0], [0,-1]]))
    elif pos == 'y':
        for i in points:
            r.extend(dot([i], [[-1,0], [0,1]]))
    elif pos == 'z':
        for i in points:
            r.extend(dot([i], [[-1,0], [0,-1]]))
    else:
        print('Error: input must be a string x, y or z')
    return r

def dilate(points, dlt):
    d = []
    if dlt >= 1:
        for i in points:
            d.extend(dot([i], [[dlt,0], [0,dlt]]))
    else:
        dlt = 1
        for i in points:
            d.extend(dot([i], [[dlt,0], [0,dlt]]))
    return d

def contract(points, ct):
    c = []
    if ct <= 1:
        for i in points:
            c.extend(dot([i], [[ct,0], [0,ct]]))
    else:
        ct = 1
        for i in points:
            c.extend(dot([i], [[ct,0], [0,ct]]))
    return c

def project(points, px, py):
    p = []
    for i in points:
        prod = dot([i], [[px], [py]])
        v = sqrt(exp(px,2) + exp(py,2))
        p.extend(dot([[(prod[0][0]/v)]], [[px,py]]))
    return p
