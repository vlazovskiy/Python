##########################################
#
# GROUP NUMBER: 2
#
# GROUP MEMBERS: Vladimir Lazovskiy, 
#
##########################################


#
# UTILITY FUNCTIONS FOR REMOVING COMMENTS FROM CODE
#


def remove_only_octothorpes(code):
    """
    Removes the octothorpes from the text in the parameter code.
    :param code: Text. Possibly valid Python code.
    :return: The same text but with all the octothorpes removed. Code that was valid before may be invalid after this.
    """
    return code.replace('#', '')
'''
For example, if this is the text in the parameter code (between and excluding the hyphens):
-----------------------------
def hello_world():        # this is a comment
    print("Hello world!") # this is another comment
print("I # like # octothorpes # .")
-----------------------------
then the string that you return should look like this (between and excluding the hyphens):
-----------------------------
def hello_world():         this is a comment
    print("Hello world!")  this is another comment
print("I  like  octothorpes  .")
-----------------------------
(Highlight the text to see exactly where the spaces are.)
'''


def remove_octothorpe_and_after(code):
    """
    Checks every line of the code and chops off everything at 
    and after the octothorpe on each line (if there is one).
    If the line has no octothorpe then it is left unchanged. 
    Returns the code with this change applied.
    :param code: Text. Possibly valid Python code.
    :return: The same text but with each line chopped at the octothorpe. Code that was valid before may be invalid after this.
    """
    return_code = ""
    for line in code.split('\n'):
        octo_index = line.find('#')
        if octo_index >= 0:
            return_code = return_code + line[0:octo_index] + '\n'
        else:
            return_code = return_code + line + '\n'
    return return_code[:-1]
'''
For example, if this is the text in the parameter code (between and excluding the hyphens):
-----------------------------
def hello_world():        # this is a comment
    print("Hello world!") # this is another comment
print("I # like # octothorpes # .")
-----------------------------
then the string that you return should look like this (between and excluding the hyphens):
-----------------------------
def hello_world():        
    print("Hello world!") 
print("I 
-----------------------------
(Highlight the text to see exactly where the spaces are.)
'''


def remove_single_line_comments(code):
    """
    Checks every line of the code and removes single line comments. 
    Does not remove octothorpes that are inside string literals. 
    Returns the code with this change applied.
    :param code: Valid Python code. This code may contain strings which have octothorpes in them. These strings are not comments.
    :return: The same text but with single line comments removed. Code should be valid and logically equivalent to the original code.
    Hints: - In order to do this you need to think about what defines a string literal.
           - Consider the code/text from the computer's point of view, not your own.
    """
    pass
'''
For example, if this is the text in the parameter code (between and excluding the hyphens):
-----------------------------
def hello_world():        # this is a comment
    print("Hello world!") # this is another comment
"""# this is a comment
This is a multiline comment
with a single line comment # this is a comment
inside of it.
"""
print("I # like # octothorpes # .")
-----------------------------
then the string that you return should look like this (between and excluding the hyphens):
-----------------------------
def hello_world():        
    print("Hello world!") 
"""
This is a multiline comment
with a single line comment 
inside of it.
"""
print("I # like # octothorpes # .")
-----------------------------
(Highlight the text to see exactly where the spaces are.)
'''



#
# STAND-ALONE FUNCTIONS RELATING TO GAMES
#

def get_square(in_map, x, y, out_of_bounds_char):
    """
    Returns the square in the map at the (x, y) location if the location
    is within bounds, or the out_of_bounds_char if (x, y) is outside of bounds.
    :param map: The two-dimensional array (i.e. list of lists) that we are examining.
    :param x: Horizontal position.
    :param y: Vertical position.
    :param out_of_bounds_char: The character to return if either x or y is out of bounds.
    :return: The character at the (x, y) position in the map.
    """
    if y >= 0 and x >= 0 and y < len(in_map) and x < len(in_map[y]):
        return in_map[y][x]
    else:
        return out_of_bounds_char
            
'''
For example, if the map looks like this:
SOME_MAP = [[ 'a', 'b', 'c', 'd' ],
            [ 'e', 'f', 'g', 'h' ],
            [ 'i', 'j', 'k', 'l' ]]
then the following function calls would return these values:
get_square(SOME_MAP, 0, 2, 'X')  -->  'i'
get_square(SOME_MAP, 3, 0, 'X')  -->  'd'
get_square(SOME_MAP, 4, 3, 'X')  -->  'X'
get_square(SOME_MAP, 0, -1, 'X')  -->  'X'
get_square(SOME_MAP, -3, 1, 'X')  -->  'X' 
'''


def set_square(in_map, x, y, new_value):
    """
    Sets the square in the map at the (x, y) location and returns True if the location is within bounds,
    or returns False if (x, y) is outside of bounds.
    :param map: The two-dimensional array (i.e. list of lists) that we are examining.
    :param x: Horizontal position.
    :param y: Vertical position.
    :param new_value: The new value to assign at (x, y).
    :return: True if (x, y) is within bounds and you could set the value or False if not.
    """
    if y >= 0 and x >= 0 and y < len(in_map) and x < len(in_map[y]):
        in_map[y][x] = new_value
        return True
    else:
        return False
'''
Examples of calling set_square() and return values:
SOME_MAP = [[ 'a', 'b', 'c', 'd' ],
            [ 'e', 'f', 'g', 'h' ],
            [ 'i', 'j', 'k', 'l' ]]
set_square(SOME_MAP, 1, 0, 'W') --> True
and now SOME_MAP looks like this:
SOME_MAP = [[ 'a', 'W', 'c', 'd' ],
            [ 'e', 'f', 'g', 'h' ],
            [ 'i', 'j', 'k', 'l' ]]
Then, separately...
set_square(SOME_MAP, -1, 0, 'W') --> False
and SOME_MAP is not changed.
'''


def get_map_from_user():
    """
    Asks the user to type in a custom map. Saves each line of text that 
    the user enters as a separate row. An empty line ends the process.
    :return: The two-dimensional array (i.e. list of lists) of characters that the user has typed in.
    """
    user_input = input()
    text = ''
    while user_input != '':
        text = text + user_input + '\n'
        user_input = input()
        
    custom_map = []
    row_index = 0
    for line in text[:-1].split('\n'):
        inner_row = []
        for char in line:
            inner_row.append(char)
        if len(inner_row) > 0:
            custom_map.append(inner_row)
    row_index = row_index + 1
        
    return custom_map
'''
For example, if the user types this (between and excluding the lines of hyphens):
--------------
  hello
this is a 
map!   

--------------
(Highlight the text to see exactly where the spaces are.)
then the map should look like this:
[[' ', ' ', 'h', 'e', 'l', 'l', 'o'],
 [', 't', 'h', 'i', 's ', 'i', 's', ' ', 'a'], 
 ['m', 'a', 'p', '!', ' ', ' ', ' ']]
Notice that spaces are kept, rows can be different lengths, and the 
blank line that ends the process is not part of the result.
If the user just hits ENTER without typing anything, it would look
like this (between and excluding the lines of hyphens):
--------------

--------------
and the result would be an empty map with no rows:
[]
'''


def extract_positions(in_map, player, werewolf):
    """
    Looks through the map for a 'P' (capital P) character and 'W' (capital W)
    character that mark the positions of the Player and Werewolf and assigns 
    the corresponding column and row values to the x and y attributes of 
    player and werewolf, respectively.
    :param map: The two-dimensional array (i.e. list of lists) of characters that we are examining.
    :param player: Player info object.
    :param werewolf: Werewolf info object.
    """
    for y_index in range(len(in_map)):
        for x_index in range(len(in_map[y_index])):
            if in_map[y_index][x_index] == 'P':
                player.x = x_index
                player.y = y_index
            if in_map[y_index][x_index] == 'W':
                werewolf.x = x_index
                werewolf.y = y_index
'''
For example, if the map looks like this:
[[ ' ', ' ', '.', 'P'],
 [ ' ', 'W', '.', '.']]
then after this code executes...
   player.x should be 3
   player.y should be 0
   werewolf.x should be 1
   werewolf.y should be 1
'''


def clear_screen():
    """
    Displays 100 blank lines to the screen. Must be completely blank, without any extra characters
    """
    print('\n' * 99)


def print_map_or_section(map_or_section):
    """
    Display the map (or section of map) to the screen.
    :param map_or_section: The two-dimensional array (i.e. list of lists) that we are examining.
    """
    for row in map_or_section:
        display_text = ''
        for char in row:
            display_text = display_text + char
        print(display_text)
'''
For example, if the map_or_section looks like this:
[[' ', ' ', 'h', 'e', 'l', 'l', 'o'],
 [', 't', 'h', 'i', 's ', 'i', 's', ' ', 'a'], 
 ['m', 'a', 'p', '!', ' ', ' ', ' ']]
then you should display this (between and excluding the lines of hyphens):
--------------
  hello
this is a 
map!   
--------------
(Highlight the text to see exactly where the spaces are.)
'''


def make_map_section(in_map, x, y, width, height, out_of_bounds_char):
    """
    Returns a copy of a section of the map starting from (x, y). Any integer values for x and y are valid.
    :param map: The two-dimensional array (i.e. list of lists) of characters that we are examining.
    :param x: The horizontal position. Any integer value is valid.
    :param y: The vertical position. Any integer value is valid.
    :param width: How many characters wide this section is.
    :param height: How many characters tall this section is.
    :param out_of_bounds_char: The character to use for points outside of the natural bounds of the map.
    :return: A two-dimensional array of characters containing the specified section of the map.
    """
    out_map = []
    for y_index in range(height):
        row = []
        for x_index in range(width):
            row.append(get_square(in_map, x + x_index, 
            y + y_index, out_of_bounds_char))
        out_map.append(row)
    return out_map
'''
For example, if the map looks like this:
SOME_MAP = [[ 'a', 'b', 'c', 'd' ],
            [ 'e', 'f', 'g', 'h' ],
            [ 'i', 'j', 'k', 'l' ],
            [ 'm', 'n', 'o', 'p' ]]
then the following function calls would return the corresponding results:
make_map_section(SOME_MAP, 1, 0, 3, 2, '#') --> [[ 'b', 'c', 'd' ], [ 'f', 'g', 'h' ]]
make_map_section(SOME_MAP, -1, -1, 2, 3, '#') --> [[ '#', '#'], ['#', 'a'], ['#', 'b']]
make_map_section(SOME_MAP, 3, 3, 3, 3, '@') --> [[ 'k', 'l', '@' ], [ 'o', 'p', '@' ], [ '@', '@', '@' ]]
make_map_section(SOME_MAP, 1, 2, 0, 0, '$') --> []
make_map_section(SOME_MAP, -1, -2, 0, 0, '$') --> []
make_map_section(SOME_MAP, -1, -2, 1, 1, '$') --> [[ '$' ]]
'''


def print_map_section(in_map, x, y, width, height, out_of_bounds_char):
    """
    Displays a section of the map starting from (x, y). Any integer values for x and y are valid.
    :param map: The two-dimensional array (i.e. list of lists) of characters that we are examining.
    :param x: The horizontal position. Any integer value is valid.
    :param y: The vertical position. Any integer value is valid.
    :param width: How many characters wide this section is.
    :param height: How many characters tall this section is.
    :param out_of_bounds_char: The character to use for points outside of the natural bounds of the map.
    :return:
    """
    display_map = make_map_section(in_map, x, y, width, height, out_of_bounds_char)
    print_map_or_section(display_map)
'''
See examples above for expectations of extracting a section of the map and displaying it.
'''
