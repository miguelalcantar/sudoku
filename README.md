# sudoku
---

The solution consists of iterating over the length of the sudoku game, which is 9.

On every iteration it validates the *i'th* **row**, **column** and **box**, which its shape is (3,3),

For rows and columns is quite simple: it just finds out whether the line contains 0's or if, after converting it into a set, its size is 9. Due the nature of sets, if there is any repeated number it will only counted once, so that the lenght would be cut.

Probably the "tricky" part is for getting the boxes, here I explain it:
Imagine the sudoku game, we all know it consists on 9 by 9 little boxes and 3 by 3 medium boxes with the shape of 3 by 3 little boxes each.

My initial question was: how do we pick one by one medium box?

Let's just try it out on Python shell:

sudoku = [

     [5, 3, 4, 6, 7, 8, 9, 1, 2],
     [6, 7, 2, 1, 9, 5, 3, 4, 8],
     [1, 9, 8, 3, 4, 2, 5, 6, 7],
     [8, 5, 9, 7, 6, 1, 4, 2, 3],
     [4, 2, 6, 8, 5, 3, 7, 9, 1],
     [7, 1, 3, 9, 2, 4, 8, 5, 6],
     [9, 6, 1, 5, 3, 7, 2, 8, 4],
     [2, 8, 7, 4, 1, 9, 6, 3, 5],
     [3, 4, 5, 2, 8, 6, 1, 7, 9]
     
   ]
   
Picking the box at the upper left side, which is:

     [5, 3, 4]
     [6, 7, 2]
     [1, 9, 8]

With Python would be:

>>> sudoku[0:3][0][0:3]
     
     [5, 3, 4]
>>> sudoku[0:3][1][0:3]

     [6, 7, 2]
>>> sudoku[0:3][2][0:3]

     [1, 9, 8]

Here we can just generalize it in the following way:

>>> [sudoku[0:3][i][0:3] for i in range(3)]
[[5, 3, 4], [6, 7, 2], [1, 9, 8]]

Obtaining the second box:

     [6, 7, 8]
     [1, 9, 5]
     [3, 4, 2]

>>> [sudoku[0:3][i][3:6] for i in range(3)]
[[6, 7, 8], [1, 9, 5], [3, 4, 2]]

And the forth box:

     [8, 5, 9]
     [4, 2, 6]
     [7, 1, 3]

>>> [sudoku[3:6][i][0:3] for i in range(3)]
[[8, 5, 9], [4, 2, 6], [7, 1, 3]]


So that, we can conclude that:

sudoku[y][i][x]

where: 
- **y** manipulates the Y axis,
- **x** manipulates the X axis,
- **i** is our index

But my goal was to find a method to generalize the way to get each box.

For instance, we have a **i** variable which goes from 0 to 8, and knowing how to access to a specific box:

The variable **xi** controls the **x** axis from 1 to 3 thanks to the *modulo* operation:
- **xi** <- i % 3 + 1
The variable **yi** controls the **y** axis from 1 to 3 thanks to the *integer division* operation:
- **yi** <- i // 3 + 1

**Finaly:**

box <- sudoku[(yi - 1) * 3: yi * 3][i][(xi - i) * 3: xi * 3]
