# Difficulty Level: Beginner

# Can you make Python print out the song for 99 bottles of beer on the wall?

# Note: You can use range() in three different ways

# First:
# range(5) will give you a list containing [0, 1, 2, 3, 4]
# In this case, range assumes you want to start counting at 0, and the parameter you give is the number to stop *just* short of.

# Second:
# range(5, 10) will give you a list containing [5, 6, 7, 8, 9]
# In this case, the two parameters you give to range() are the number to start at and the number to stop *just* short of.
# Helpful mnemonic: range(start, stop)

# Third:
# range(5, 15, 3) will give you a list containing [5, 8, 11, 14]
# In this case, the three parameters you give to range() are the number to start at, the number to stop *just* short of, and the number to increment each time by.
# Note that normally, the number to increment each time by is assumed to be 1.  (In other words, you add 1 each time through.)
# That's why it goes [0, 1, 2, 3, 4] unless you specify that third parameter, called the step.
# Helpful mnemonic: range(start, stop, step)

for b in range(99, -1, -1):
    if b==1:
        print b,"bottle of beer on the wall,",b,"bottle of beer."
        print "Take one down and pass it around,"
        print b-1,"bottles of beer on the wall."
    elif b==0:
        print "No more bottles of beer on the wall."
    else:
        print b,"bottles of beer on the wall,",b,"bottles of beer."
        print "Take one down and pass it around,"
        print b-1,"bottles of beer on the wall."

# Using range() and a loop, print out the song.  Your output should look like this:

# 99 bottles of beer on the wall, 99 bottles of beer ...
# If one of those bottles should happen to fall, 98 bottles of beer on the wall
# 98 bottles of beer on the wall, 98 bottles of beer ...
# If one of those bottles should happen to fall, 97 bottles of beer on the wall
# 97 bottles of beer on the wall, 97 bottles of beer ...
# If one of those bottles should happen to fall, 96 bottles of beer on the wall
# 96 bottles of beer on the wall, 96 bottles of beer ...
# If one of those bottles should happen to fall, 95 bottles of beer on the wall
# 95 bottles of beer on the wall, 95 bottles of beer ...
# If one of those bottles should happen to fall, 94 bottles of beer on the wall
# 94 bottles of beer on the wall, 94 bottles of beer ...
# If one of those bottles should happen to fall, 93 bottles of beer on the wall
# 93 bottles of beer on the wall, 93 bottles of beer ...
# If one of those bottles should happen to fall, 92 bottles of beer on the wall
# 92 bottles of beer on the wall, 92 bottles of beer ...
# If one of those bottles should happen to fall, 91 bottles of beer on the wall
# 91 bottles of beer on the wall, 91 bottles of beer ...
# If one of those bottles should happen to fall, 90 bottles of beer on the wall
# 90 bottles of beer on the wall, 90 bottles of beer ...
# If one of those bottles should happen to fall, 89 bottles of beer on the wall
# 89 bottles of beer on the wall, 89 bottles of beer ...
# If one of those bottles should happen to fall, 88 bottles of beer on the wall
# 88 bottles of beer on the wall, 88 bottles of beer ...
# If one of those bottles should happen to fall, 87 bottles of beer on the wall
# 87 bottles of beer on the wall, 87 bottles of beer ...
# If one of those bottles should happen to fall, 86 bottles of beer on the wall
# 86 bottles of beer on the wall, 86 bottles of beer ...
# If one of those bottles should happen to fall, 85 bottles of beer on the wall
# 85 bottles of beer on the wall, 85 bottles of beer ...
# If one of those bottles should happen to fall, 84 bottles of beer on the wall
# 84 bottles of beer on the wall, 84 bottles of beer ...
# If one of those bottles should happen to fall, 83 bottles of beer on the wall
# 83 bottles of beer on the wall, 83 bottles of beer ...
# If one of those bottles should happen to fall, 82 bottles of beer on the wall
# 82 bottles of beer on the wall, 82 bottles of beer ...
# If one of those bottles should happen to fall, 81 bottles of beer on the wall
# 81 bottles of beer on the wall, 81 bottles of beer ...
# If one of those bottles should happen to fall, 80 bottles of beer on the wall
# 80 bottles of beer on the wall, 80 bottles of beer ...
# If one of those bottles should happen to fall, 79 bottles of beer on the wall
# 79 bottles of beer on the wall, 79 bottles of beer ...
# If one of those bottles should happen to fall, 78 bottles of beer on the wall
# 78 bottles of beer on the wall, 78 bottles of beer ...
# If one of those bottles should happen to fall, 77 bottles of beer on the wall
# 77 bottles of beer on the wall, 77 bottles of beer ...
# If one of those bottles should happen to fall, 76 bottles of beer on the wall
# 76 bottles of beer on the wall, 76 bottles of beer ...
# If one of those bottles should happen to fall, 75 bottles of beer on the wall
# 75 bottles of beer on the wall, 75 bottles of beer ...
# If one of those bottles should happen to fall, 74 bottles of beer on the wall
# 74 bottles of beer on the wall, 74 bottles of beer ...
# If one of those bottles should happen to fall, 73 bottles of beer on the wall
# 73 bottles of beer on the wall, 73 bottles of beer ...
# If one of those bottles should happen to fall, 72 bottles of beer on the wall
# 72 bottles of beer on the wall, 72 bottles of beer ...
# If one of those bottles should happen to fall, 71 bottles of beer on the wall
# 71 bottles of beer on the wall, 71 bottles of beer ...
# If one of those bottles should happen to fall, 70 bottles of beer on the wall
# 70 bottles of beer on the wall, 70 bottles of beer ...
# If one of those bottles should happen to fall, 69 bottles of beer on the wall
# 69 bottles of beer on the wall, 69 bottles of beer ...
# If one of those bottles should happen to fall, 68 bottles of beer on the wall
# 68 bottles of beer on the wall, 68 bottles of beer ...
# If one of those bottles should happen to fall, 67 bottles of beer on the wall
# 67 bottles of beer on the wall, 67 bottles of beer ...
# If one of those bottles should happen to fall, 66 bottles of beer on the wall
# 66 bottles of beer on the wall, 66 bottles of beer ...
# If one of those bottles should happen to fall, 65 bottles of beer on the wall
# 65 bottles of beer on the wall, 65 bottles of beer ...
# If one of those bottles should happen to fall, 64 bottles of beer on the wall
# 64 bottles of beer on the wall, 64 bottles of beer ...
# If one of those bottles should happen to fall, 63 bottles of beer on the wall
# 63 bottles of beer on the wall, 63 bottles of beer ...
# If one of those bottles should happen to fall, 62 bottles of beer on the wall
# 62 bottles of beer on the wall, 62 bottles of beer ...
# If one of those bottles should happen to fall, 61 bottles of beer on the wall
# 61 bottles of beer on the wall, 61 bottles of beer ...
# If one of those bottles should happen to fall, 60 bottles of beer on the wall
# 60 bottles of beer on the wall, 60 bottles of beer ...
# If one of those bottles should happen to fall, 59 bottles of beer on the wall
# 59 bottles of beer on the wall, 59 bottles of beer ...
# If one of those bottles should happen to fall, 58 bottles of beer on the wall
# 58 bottles of beer on the wall, 58 bottles of beer ...
# If one of those bottles should happen to fall, 57 bottles of beer on the wall
# 57 bottles of beer on the wall, 57 bottles of beer ...
# If one of those bottles should happen to fall, 56 bottles of beer on the wall
# 56 bottles of beer on the wall, 56 bottles of beer ...
# If one of those bottles should happen to fall, 55 bottles of beer on the wall
# 55 bottles of beer on the wall, 55 bottles of beer ...
# If one of those bottles should happen to fall, 54 bottles of beer on the wall
# 54 bottles of beer on the wall, 54 bottles of beer ...
# If one of those bottles should happen to fall, 53 bottles of beer on the wall
# 53 bottles of beer on the wall, 53 bottles of beer ...
# If one of those bottles should happen to fall, 52 bottles of beer on the wall
# 52 bottles of beer on the wall, 52 bottles of beer ...
# If one of those bottles should happen to fall, 51 bottles of beer on the wall
# 51 bottles of beer on the wall, 51 bottles of beer ...
# If one of those bottles should happen to fall, 50 bottles of beer on the wall
# 50 bottles of beer on the wall, 50 bottles of beer ...
# If one of those bottles should happen to fall, 49 bottles of beer on the wall
# 49 bottles of beer on the wall, 49 bottles of beer ...
# If one of those bottles should happen to fall, 48 bottles of beer on the wall
# 48 bottles of beer on the wall, 48 bottles of beer ...
# If one of those bottles should happen to fall, 47 bottles of beer on the wall
# 47 bottles of beer on the wall, 47 bottles of beer ...
# If one of those bottles should happen to fall, 46 bottles of beer on the wall
# 46 bottles of beer on the wall, 46 bottles of beer ...
# If one of those bottles should happen to fall, 45 bottles of beer on the wall
# 45 bottles of beer on the wall, 45 bottles of beer ...
# If one of those bottles should happen to fall, 44 bottles of beer on the wall
# 44 bottles of beer on the wall, 44 bottles of beer ...
# If one of those bottles should happen to fall, 43 bottles of beer on the wall
# 43 bottles of beer on the wall, 43 bottles of beer ...
# If one of those bottles should happen to fall, 42 bottles of beer on the wall
# 42 bottles of beer on the wall, 42 bottles of beer ...
# If one of those bottles should happen to fall, 41 bottles of beer on the wall
# 41 bottles of beer on the wall, 41 bottles of beer ...
# If one of those bottles should happen to fall, 40 bottles of beer on the wall
# 40 bottles of beer on the wall, 40 bottles of beer ...
# If one of those bottles should happen to fall, 39 bottles of beer on the wall
# 39 bottles of beer on the wall, 39 bottles of beer ...
# If one of those bottles should happen to fall, 38 bottles of beer on the wall
# 38 bottles of beer on the wall, 38 bottles of beer ...
# If one of those bottles should happen to fall, 37 bottles of beer on the wall
# 37 bottles of beer on the wall, 37 bottles of beer ...
# If one of those bottles should happen to fall, 36 bottles of beer on the wall
# 36 bottles of beer on the wall, 36 bottles of beer ...
# If one of those bottles should happen to fall, 35 bottles of beer on the wall
# 35 bottles of beer on the wall, 35 bottles of beer ...
# If one of those bottles should happen to fall, 34 bottles of beer on the wall
# 34 bottles of beer on the wall, 34 bottles of beer ...
# If one of those bottles should happen to fall, 33 bottles of beer on the wall
# 33 bottles of beer on the wall, 33 bottles of beer ...
# If one of those bottles should happen to fall, 32 bottles of beer on the wall
# 32 bottles of beer on the wall, 32 bottles of beer ...
# If one of those bottles should happen to fall, 31 bottles of beer on the wall
# 31 bottles of beer on the wall, 31 bottles of beer ...
# If one of those bottles should happen to fall, 30 bottles of beer on the wall
# 30 bottles of beer on the wall, 30 bottles of beer ...
# If one of those bottles should happen to fall, 29 bottles of beer on the wall
# 29 bottles of beer on the wall, 29 bottles of beer ...
# If one of those bottles should happen to fall, 28 bottles of beer on the wall
# 28 bottles of beer on the wall, 28 bottles of beer ...
# If one of those bottles should happen to fall, 27 bottles of beer on the wall
# 27 bottles of beer on the wall, 27 bottles of beer ...
# If one of those bottles should happen to fall, 26 bottles of beer on the wall
# 26 bottles of beer on the wall, 26 bottles of beer ...
# If one of those bottles should happen to fall, 25 bottles of beer on the wall
# 25 bottles of beer on the wall, 25 bottles of beer ...
# If one of those bottles should happen to fall, 24 bottles of beer on the wall
# 24 bottles of beer on the wall, 24 bottles of beer ...
# If one of those bottles should happen to fall, 23 bottles of beer on the wall
# 23 bottles of beer on the wall, 23 bottles of beer ...
# If one of those bottles should happen to fall, 22 bottles of beer on the wall
# 22 bottles of beer on the wall, 22 bottles of beer ...
# If one of those bottles should happen to fall, 21 bottles of beer on the wall
# 21 bottles of beer on the wall, 21 bottles of beer ...
# If one of those bottles should happen to fall, 20 bottles of beer on the wall
# 20 bottles of beer on the wall, 20 bottles of beer ...
# If one of those bottles should happen to fall, 19 bottles of beer on the wall
# 19 bottles of beer on the wall, 19 bottles of beer ...
# If one of those bottles should happen to fall, 18 bottles of beer on the wall
# 18 bottles of beer on the wall, 18 bottles of beer ...
# If one of those bottles should happen to fall, 17 bottles of beer on the wall
# 17 bottles of beer on the wall, 17 bottles of beer ...
# If one of those bottles should happen to fall, 16 bottles of beer on the wall
# 16 bottles of beer on the wall, 16 bottles of beer ...
# If one of those bottles should happen to fall, 15 bottles of beer on the wall
# 15 bottles of beer on the wall, 15 bottles of beer ...
# If one of those bottles should happen to fall, 14 bottles of beer on the wall
# 14 bottles of beer on the wall, 14 bottles of beer ...
# If one of those bottles should happen to fall, 13 bottles of beer on the wall
# 13 bottles of beer on the wall, 13 bottles of beer ...
# If one of those bottles should happen to fall, 12 bottles of beer on the wall
# 12 bottles of beer on the wall, 12 bottles of beer ...
# If one of those bottles should happen to fall, 11 bottles of beer on the wall
# 11 bottles of beer on the wall, 11 bottles of beer ...
# If one of those bottles should happen to fall, 10 bottles of beer on the wall
# 10 bottles of beer on the wall, 10 bottles of beer ...
# If one of those bottles should happen to fall, 9 bottles of beer on the wall
# 9 bottles of beer on the wall, 9 bottles of beer ...
# If one of those bottles should happen to fall, 8 bottles of beer on the wall
# 8 bottles of beer on the wall, 8 bottles of beer ...
# If one of those bottles should happen to fall, 7 bottles of beer on the wall
# 7 bottles of beer on the wall, 7 bottles of beer ...
# If one of those bottles should happen to fall, 6 bottles of beer on the wall
# 6 bottles of beer on the wall, 6 bottles of beer ...
# If one of those bottles should happen to fall, 5 bottles of beer on the wall
# 5 bottles of beer on the wall, 5 bottles of beer ...
# If one of those bottles should happen to fall, 4 bottles of beer on the wall
# 4 bottles of beer on the wall, 4 bottles of beer ...
# If one of those bottles should happen to fall, 3 bottles of beer on the wall
# 3 bottles of beer on the wall, 3 bottles of beer ...
# If one of those bottles should happen to fall, 2 bottles of beer on the wall
# 2 bottles of beer on the wall, 2 bottles of beer ...
# If one of those bottles should happen to fall, 1 bottles of beer on the wall
