# MasterMind
A command line implementation of the board game MasterMind. 

## Info

There are blue, red, white, black, yellow and green pieces to play. After entering the guess, it will display your guess with how many are correct. Correctness are split into 2 different presentations, white and red. Just like the original game, a white indicator is telling you one of your guess is the correct colour, a red indicator is telling you that one of your guess has both correct colour and position. 

There are at most 10 turns.

Repetited colours are allowed. 

Future version will include an option to turn off repititon in auto generated board. For two player mode, this can also be prevented. 

## Example

```shell
$ python3 main.py
Please select 1 - user input colour combination or 2 - random colour combination: 2
Turn 1
Enter the colors with ',' between each:
w,w,b,bl
['w', 'w', 'b', 'bl'] []
Turn 2
Enter the colors with ',' between each:
r,y,g,g
r
['w', 'w', 'b', 'bl'] []
['r', 'y', 'g', 'g'] ['R', 'R', 'W']
Turn 3
Enter the colors with ',' between each:
r,r,g,g,
Invalid amount of colours entered!
Enter the colors with ',' between each:
r,r,g,g
['w', 'w', 'b', 'bl'] []
['r', 'y', 'g', 'g'] ['R', 'R', 'W']
['r', 'r', 'g', 'g'] ['R', 'R', 'R']
Turn 4
Enter the colors with ',' between each:
r,r,g,y
['w', 'w', 'b', 'bl'] []
['r', 'y', 'g', 'g'] ['R', 'R', 'W']
['r', 'r', 'g', 'g'] ['R', 'R', 'R']
['r', 'r', 'g', 'y'] ['R', 'R']
Turn 5
Enter the colors with ',' between each:
g,r,g,g 
['w', 'w', 'b', 'bl'] []
['r', 'y', 'g', 'g'] ['R', 'R', 'W']
['r', 'r', 'g', 'g'] ['R', 'R', 'R']
['r', 'r', 'g', 'y'] ['R', 'R']
['g', 'r', 'g', 'g'] ['R', 'R', 'R', 'R']
Won in 5 turns!
```



## Note

There are currently no error checking for the following issues:

- Entering more or less than 4 colours at a time.
- Some error with inputs. Fix soon.
