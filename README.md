# Saddle-Points
Finding Saddle Points in a Matrix

Author of solution: Lucas Noritomi-Hartwig

I did not author this question.
Here is the link to the video where I first encountered this question:
https://youtu.be/Wm5eLTeC9KM

The original question:

    University of Waterloo, Faculty of Engineering, Department of Electrical & Computer Engineering

    ECE150 - Fundamentals of Programming, December 2020 Final Exam Question:

    We define a saddle point in a matrix as being an entry of a matrix that is:
    - Strictly less than any entry in the given row
    - Strictly greater than any entry in the given column

The goal is to complete given C++ starter code to identify if a given matrix has a saddle point or not.
If the matrix does have a saddle point, the program should return true, and if it does not, the program shoudl return false.

This question was originally intended for the solution to be in written in C++. However, I have written my own solution to the problem in Python.

In my Python implementation, as soon as the first saddle point is found, the program returns the index of the point and terminates the search.
This is because there can only be at most one saddle point (as defined in the question) for any given matrix.


Proof that there can only exist at most one saddle point in a matrix:
(The question asked on the exam did not ask for a proof, I am only including it here to help readers understand why the program only checks for one saddle point.)

Assume there exists a matrix A that has two or more saddle points.
We will only consider two saddle points, a and b, that lie in a matrix. However, this is not a problem as the reasoning in this proof can be reapplied to any number of saddle points.

Let a and b be the two saddle points in matrix A.
Then we know that a and b must lie on different rows and different columns.

Let x be the point on the same column as a and on the same row as b, and let y be the point on the same column as b and on the same row as a.

Then, W.L.O.G, the following grid is in A:

          .       .
          .       .
          .       .
    . . . a . . . y . . .
          .       .
          .       .
          .       .
    . . . x . . . b . . .
          .       .
          .       .
          .       .

By definition, a is the smallest number in its row, so a < y, and a is also the largest number in its column, so a > x.
The following is true for b for the same reason as above: b < x, b > y.

If we combine the satements for a, we get:
x < a < y, implying x < y

and if we combine the statements for b, we get:
y < b < x, implying y < x

This is a contradiction as there exist no numbers x, y such that x < y and y < x.

Therefore, either a or b (not both) can be a saddle point.

As mentioned eariler, this reasoning can be applied again to the next supposed saddle point, and so on.

Therefore, it is proven that no matrix has more than one saddle point (as defined by the question).
