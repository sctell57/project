def make_empty_board(n):
   board = []
   for i in range(n):
       board2 = []
       for k in range(n):
           board2.append(None)
       board.append(board2)
   return board
	

def is_valid_location (loc, puzzle):
   dim = len(puzzle)
   x, y = loc
   if (x < dim) and (-1 < x) and (y < dim) and (-1 < y):
       return True
   else:
       return False
	  
def is_complete(puzzle):
	for x in range(len(puzzle)):
		for y in range(len(puzzle)):
			if puzzle[x][y] == None:
				return
			else:
				return True
def get_value_at_location(puzzle, loc):
   x,y = loc
   return puzzle[x][y]

def set_location(puzzle, value, loc):
   x,y = loc
   if is_valid_location(loc, puzzle):
       puzzle[x][y] = value
       return True
   else:
       return False
	   
def unset_location(puzzle, loc):
	x,y = loc
	if is_valid_location(loc, puzzle) == False:
		return False
	x, y = loc
	row = puzzle[x]
	element = row[y]
	if element == None:
		return False # loaction is already None
	else: # make location None
		row[y] = None
		return True
		
def get_size(puzzle):
	count = 0 # keeps count of the size
	for row in puzzle:
		count = count + 1
		return count

def get_valid_numbers(size):
	validList = [] # initially it is empty
	for i in range(1, size + 1):
		validList.append(i)
	return validList

def contains_only_valid_symbols(puzzle, complete):
	size = get_size(puzzle)
	validList = get_valid_numbers(size)
	if complete == False: # if it is not complete then allow None
		validList.append(None)
	for row in puzzle:
		for element in row:
			if element not in validList:
				return False # one invalid symbol makes it false
	return True 
	
def has_repeat(xs, v):
	count = 0
	for i in xs:
		if i == v:
			count = count + 1
	if count > 1:
		return True
	else:
		return False
		
def get_row(puzzle, row_index):
	size = get_size(puzzle)
	if row_index > size-1:
		return None # invalid index
	elif(row_index<0):
		if row_index > -(size-1):
			return None
	return puzzle[row_index] # return the list at row_index
	
def is_valid_row(puzzle, row_index, complete):
	row = get_row(puzzle, row_index)
	if row == None:
		return False
	repeat = has_repeat(row, get_valid_numbers(puzzle))
	if complete == True:
		for i in row:
			if None in i:
				return False
			elif i >= get_size(row):
				return False
		return True
	elif complete == False:
		for i in row:
			if i >= get_size(row):
				return False
		if repeat == True:
			return False
		else:
			return True

def has_valid_rows(puzzle, complete):
	comp_row = is_valid_row(puzzle, row_index, complete)
	getrow = get_row(puzzle, row_index)
	
#def get_column(puzzle, col_index):
	
	
	

			
		
 


		
		
