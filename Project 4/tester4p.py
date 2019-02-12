# STUDENTS: TO USE:
# 
# The following command will test all test cases on your file:
# 
#   python3 <thisfile.py> <your_one_file.py>
# 
# 
# You can also limit the tester to only the functions you want tested.
# Just add as many functions as you want tested on to the command line at the end.
# Example: to only run tests associated with func1, func2, and func3, run this command:
# 
#   python3 <thisfile.py> <your_one_file.py> func1 func2 func3
# 


# INSTRUCTOR: TO PREPARE:
#  - add test cases to class AllTests. The test case functions' names must
# be precise - to test a function named foobar, the test must be named "test_foobar_#"
# where # may be any digits at the end, such as "test_foobar_13".
# - any extra-credit tests must be named "test_extra_credit_foobar_#"
# 
# - name all required definitions in REQUIRED_DEFNS. Do not include any unofficial 
#   helper functions. If you want to make helper definitions to use while testing,
#   those can also be added there for clarity.
# 
# to run on either a single file or all .py files in a folder (recursively):
#   python3 <thisfile.py> <your_one_file.py>
#   python3 <thisfile.py> <dir_of_files>
# 
# A work in progress by Mark Snyder, Oct. 2015.
#  Edited by Yutao Zhong, Spring 2016.
#  Edited by Raven Russell, Spring 2017.


import unittest
import shutil
import sys
import os
import os.path
import time

import importlib

############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond 
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.
	
REQUIRED_DEFNS = [	"make_empty_board",
					"is_valid_location",
					"is_complete",
					"get_value_at_location",
					"set_location",
					"unset_location",
					"get_size",
					"get_valid_numbers",
					"contains_only_valid_symbols",
					"has_repeat",
					"get_row",
					"is_valid_row",
					"has_valid_rows",
					"get_column",
					"is_valid_col",
					"has_valid_cols",
					"is_valid_cage_solution",
					"is_valid",
					"get_board_string",
					"get_missing_numbers_row_or_col",
					"candidates_at_location",
					"is_symmetric"
				 ]

extra_credit = [ 	"get_missing_numbers_row_or_col",
					"candidates_at_location", 
					"is_symmetric"
				]
weight_required = 1
weight_extra_credit = 1

RENAMED_FILE = "student"

# SAMPLE BOARDS, FOR TESTING.

def board0():
	return [[3,None,2],
	 	   	[2,3,None],
			[None,2,None]]

def board1():
	return ([[1,2,3],
			 [3,1,2],
			 [2,3,1]])
	
def board2():
	return [[2,4,None,None ],
			[1,2,3,4],
			[3,1,None,None ],
			[4,3,None,None ]]
def board3():
	return [[2,4,1,3 ],
			[1,2,3,4 ],
			[3,1,4,2 ],
			[4,3,2,1 ]]

def board4():
	return ([[3,2,1],[2,3,1],[1,2,3]]) #repeat numbers in a column
	
def board5():
	return ([[2,4,None,None],[1,2,3,3],[3,1,None,5],[4,3,1,2]])
	
def	board6():
	return ([[2,1,None,None],[None,2,3,3],[3,1,None,5],[4,3,None,None]])


def cages0():
	return ['+',5,[(0,0),(1,0)]]
	
def cages1():
	return [['x', 6, [(0,0),(1,0)]],
         	['-', 1, [(0,1),(0,2)]],
         	['-', 1, [(2,0),(2,1)]],
         	['+', 7, [(1,1),(1,2),(2,2)]]
        	]

def cages2():
	return [['-',2,[(0,0),(0,1)]],
			['-',2,[(0,2),(0,3)]],
			['+',3,[(1,0),(1,1)]],
			['+',9,[(1,2),(2,2),(3,2)]],
			['x',9,[(2,0),(2,1),(3,1)]]
			]

# END SPECIALIZATION SECTION
############################################################################
############################################################################



# enter batch mode by giving a directory to work on.
BATCH_MODE = (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))

# This class contains multiple "unit tests" that each check
# various inputs to specific functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):
	
	############################################################
	
	def test_make_empty_board_01 (self): self.assertEqual (make_empty_board(1),[[None]])
	def test_make_empty_board_02 (self): self.assertEqual (make_empty_board(2),[[None,None],[None,None]])
	def test_make_empty_board_03 (self): 
		board = make_empty_board(2)
		self.assertEqual (len(board), 2)
		id_1 = id(board[0])
		id_2 = id(board[1])
		self.assertTrue(id_1 != id_2)  #making sure the board has separate rows, no aliases

	def test_make_empty_board_04 (self):
		board = make_empty_board(3)
		self.assertEqual(board,[[None,None,None],[None,None,None],[None,None,None]])
		self.assertEqual (len(board), 3)
		id_1 = id(board[0])
		id_2 = id(board[1])
		id_3 = id(board[2])
		self.assertTrue(id_1 != id_2 and id_1!=id_3 and id_2!=id_3)  
			#making sure the board has separate rows, no aliases
	
	############################################################

	def test_is_valid_location_01 (self): self.assertEqual (is_valid_location((0,0),board0()),True)
	def test_is_valid_location_02 (self): self.assertEqual (is_valid_location((1,2),board0()),True)
	def test_is_valid_location_03 (self): self.assertEqual (is_valid_location((-1,1),board0()),False)
	def test_is_valid_location_04 (self): self.assertEqual (is_valid_location((3,2),board0()),False)
	def test_is_valid_location_05 (self): self.assertEqual (is_valid_location((1,5),board0()),False)

	############################################################

	def test_is_complete_01 (self): self.assertEqual (is_complete(board0()),False)
	def test_is_complete_02 (self): self.assertEqual (is_complete(board1()),True)
	def test_is_complete_03 (self): self.assertEqual (is_complete([[None,None],[None,None]]),False)
	def test_is_complete_04 (self): self.assertEqual (is_complete([[1,1,1],[1,1,1],[1,1,1]]),True)
	def test_is_complete_05 (self): self.assertEqual (is_complete([[1,2],[-1,1]]),True)

	############################################################
	
	def test_get_value_at_location_01 (self): self.assertEqual (get_value_at_location(board0(),(0,0)),3)
	def test_get_value_at_location_02 (self): self.assertEqual (get_value_at_location(board0(),(1,2)),None)
	def test_get_value_at_location_03 (self): self.assertEqual (get_value_at_location(board6(), (3,1)),3)
	def test_get_value_at_location_04 (self): self.assertEqual (get_value_at_location([[-4]], (0,0)),-4)

	############################################################
	
	def test_set_location_01 (self): 
		board = board0()
		self.assertEqual(set_location(board,1,(0,1)),True) #testing return value
		self.assertEqual(board, [[3,1,2], [2,3,None],[None,2,None]]) # testing board updating
	def test_set_location_02 (self): 
		board = board0()
		self.assertEqual(set_location(board,1,(0,4)),False) #invalid location
		self.assertEqual(board, board0())
	def test_set_location_03 (self): 
		board = board0()
		self.assertEqual(set_location(board,1,(0,0)),False) #cell already filled 
		self.assertEqual(board, board0())
	def test_set_location_04 (self): 
		board = board0()
		self.assertEqual(set_location(board,3,(2,0)),True) 
		self.assertEqual(board, [[3,None,2], [2,3,None],[3,2,None]])

	############################################################
	
	def test_unset_location_01 (self): 
		board = board0()
		self.assertEqual(unset_location(board,(0,0)),True)
		self.assertEqual(board,[[None,None,2], [2,3,None],[None,2,None]])
	def test_unset_location_02 (self): 
		board = board0()
		self.assertEqual(unset_location(board,(0,4)),False) #invalid location
		self.assertEqual(board, board0())
	def test_unset_location_03 (self): 
		board = board0()
		self.assertEqual(unset_location(board,(2,2)),False) # empty cell: nothing to unset
		self.assertEqual(board, board0())
	def test_unset_location_04 (self): 
		board = board0()
		self.assertEqual(unset_location(board,(1,1)),True) # empty cell: nothing to unset
		self.assertEqual(board,[[3,None,2], [2,None,None],[None,2,None]] )

	############################################################
	
	def test_get_size_01 (self): self.assertEqual (get_size([[None]]),1)
	def test_get_size_02 (self): self.assertEqual (get_size([[1,2],[3,4]]),2)
	def test_get_size_03 (self): self.assertEqual (get_size(board3()),4)
	def test_get_size_04 (self): self.assertEqual (get_size([[1,-1,1,-1],[1,-1,1,-1],[1,-1,1,-1],[1,-1,1,-1]]),4)
		
	############################################################
	
	def test_get_valid_numbers_01 (self): self.assertEqual (get_valid_numbers(1),[1])
	def test_get_valid_numbers_02 (self): self.assertEqual (get_valid_numbers(3),[1,2,3])
	def test_get_valid_numbers_03 (self): self.assertEqual (get_valid_numbers(4),[1,2,3,4])
	def test_get_valid_numbers_04 (self): self.assertEqual (get_valid_numbers(9),[1,2,3,4,5,6,7,8,9])
		
	############################################################
	
	def test_contains_only_valid_symbols_01 (self): self.assertEqual (contains_only_valid_symbols(board0(),False),True)
	def test_contains_only_valid_symbols_02 (self): self.assertEqual (contains_only_valid_symbols(board0(),True),False)
	def test_contains_only_valid_symbols_03 (self): 
		self.assertEqual (contains_only_valid_symbols([[1,2],[3,4]],True),False)
		self.assertEqual (contains_only_valid_symbols([[1,2],[2,-1]],True),False)
	def test_contains_only_valid_symbols_04 (self): self.assertEqual (contains_only_valid_symbols(board3(),True),True)
	def test_contains_only_valid_symbols_05 (self): self.assertEqual (contains_only_valid_symbols(board6(),False),False)

	############################################################
	
	def test_has_repeat_01 (self): self.assertEqual (has_repeat([None],1),False)
	def test_has_repeat_02 (self): self.assertEqual (has_repeat([2,1,3],1),False)
	def test_has_repeat_03 (self): self.assertEqual (has_repeat([1,2,1],1),True)
	def test_has_repeat_04 (self): self.assertEqual (has_repeat([1,None,3],1),False)
	def test_has_repeat_05 (self): self.assertEqual (has_repeat([1,None,3,1,2,4,5,6,7,8,9],3),False)

	############################################################
	
	def test_get_row_01 (self): self.assertEqual (get_row(board0(),0),[3,None,2])
	def test_get_row_02 (self): self.assertEqual (get_row(board0(),-2),None)
	def test_get_row_03 (self): self.assertEqual (get_row(board0(),4),None)
	def test_get_row_04 (self): self.assertEqual (get_row(board3(),2),[3,1,4,2])

	############################################################
	
	def test_is_valid_row_01 (self): 
		self.assertEqual (is_valid_row([[None,1],[1,2]],0,False),True)
		self.assertEqual (is_valid_row([[None,1],[1,2]],0,True),False)
	def test_is_valid_row_02 (self): self.assertEqual (is_valid_row(board5(),2,False),False)
	def test_is_valid_row_03 (self): self.assertEqual (is_valid_row(board5(),0,False),True) #repeated None is ok
	def test_is_valid_row_04 (self): self.assertEqual (is_valid_row(board5(),7,True),False) 
	def test_is_valid_row_05 (self): self.assertEqual (is_valid_row(board5(),3,True),True)

	############################################################
	
	def test_has_valid_rows_01 (self): self.assertEqual (has_valid_rows(board0(), False),True)
	def test_has_valid_rows_02 (self): self.assertEqual (has_valid_rows(board0(), True),False)
	def test_has_valid_rows_03 (self): self.assertEqual (has_valid_rows(board3(), True),True)
	def test_has_valid_rows_04 (self): self.assertEqual (has_valid_rows(board5(), False),False)
	def test_has_valid_rows_05 (self): self.assertEqual (has_valid_rows([[1,2,3],[2,1,3],[3,1,3]], True),False) #repeat
	
	############################################################
	
	def test_get_column_01 (self): self.assertEqual (get_column(board0(),0),[3,2,None])
	def test_get_column_02 (self): self.assertEqual (get_column(board0(),1),[None,3,2])
	def test_get_column_03 (self): self.assertEqual (get_column(board0(),-1),None)
	def test_get_column_04 (self): self.assertEqual (get_column(board0(),6),None)
	def test_get_column_05 (self): self.assertEqual (get_column(board3(),0),[2,1,3,4])

	############################################################
	
	def test_is_valid_col_01 (self): 
		self.assertEqual (is_valid_col([[None,1],[1,2]],0,False),True)
		self.assertEqual (is_valid_col([[None,1],[1,2]],0,True),False)
	def test_is_valid_col_02 (self): self.assertEqual (is_valid_col(board6(),1,True),False)
	def test_is_valid_col_03 (self): self.assertEqual (is_valid_col(board6(),3,False),False)
	def test_is_valid_col_04 (self): self.assertEqual (is_valid_col(board6(),-2,True),False)
	def test_is_valid_col_05 (self): self.assertEqual (is_valid_col(board3(),2,True),True)

	############################################################
	
	def test_has_valid_cols_01 (self): self.assertEqual (has_valid_cols(board0(), False),True)
	def test_has_valid_cols_02 (self): self.assertEqual (has_valid_cols(board0(), True),False)
	def test_has_valid_cols_03 (self): self.assertEqual (has_valid_cols(board3(), True),True)
	def test_has_valid_cols_04 (self): self.assertEqual (has_valid_cols(board6(), False),False) #invalid num and repeat
	def test_has_valid_cols_05 (self): self.assertEqual (has_valid_cols(board4(), True),False) #repeat
	
	############################################################
	
	def test_is_valid_cage_solution_01 (self): self.assertEqual (is_valid_cage_solution([[1]], '+', 1, [(0,0)]),True)
	def test_is_valid_cage_solution_02 (self): self.assertEqual (is_valid_cage_solution([[1,2],[2,1]], '-', 1, [(0,0),(1,0)]),True)
	def test_is_valid_cage_solution_03 (self): self.assertEqual (is_valid_cage_solution([[1,2],[2,1]], '-', 1, [(1,0),(0,0)]),True)
	def test_is_valid_cage_solution_04 (self): self.assertEqual (is_valid_cage_solution([[1,2],[2,1]], 'x', 4, [(0,0),(0,1),(1,0),(1,1)]),True)
	def test_is_valid_cage_solution_05 (self): self.assertEqual (is_valid_cage_solution([[1,2],[2,1]], '+', 4, [(0,0),(0,1)]),False)
	def test_is_valid_cage_solution_06 (self): self.assertEqual (is_valid_cage_solution(board1(), '-', 5, [(0,0),(0,1)]),False)
	def test_is_valid_cage_solution_07 (self): self.assertEqual (is_valid_cage_solution(board3(), 'x', 6, [(1,1),(1,2),(1,3)]),False)

	############################################################
	
	def test_is_valid_01 (self): 
		self.assertEqual (is_valid(board0(),[],False),True)
		self.assertEqual (is_valid(board1(),[],True),True)
	def test_is_valid_02 (self): 
		self.assertEqual (is_valid(board4(),[],True),False)
		self.assertEqual (is_valid(board5(),[],False),False)
	def test_is_valid_03 (self): 
		self.assertEqual (is_valid(board1(),[['+',4,[(0,0),(1,0)]],['x',3,[(0,2),(1,2),(2,2)]]],True),False)
		self.assertEqual (is_valid(board1(),[['+',4,[(0,0),(1,0)]],['x',6,[(0,2),(1,2),(2,2)]]],True),True)
	def test_is_valid_04 (self): self.assertEqual (is_valid(board2(),[['+',5,[(0,0),(1,0)]],['x',6,[(0,0),(1,0),(2,0)]]],False),True)

	def test_is_valid_05 (self): 
		board = [[3,1,2],[2,3,1],[1,2,3]]
		cages = [['x', 6, [(0,0),(1,0)]],
				 ['-', 1, [(0,1),(0,2)]],
				 ['-', 1, [(2,0),(2,1)]],
			 	['+', 7, [(1,1),(1,2),(2,2)]]
				]
		self.assertEqual (is_valid(board,cages,True),True)

	def test_is_valid_06 (self): 
		board = [[4,2,1,3],[2,3,4,1],[3,1,2,4],[1,4,3,2]]
		cages = [['-', 2,[(0,0),(1,0)]],
			 	['-', 2,[(2,0),(3,0)]],
			 	['-', 2,[(1,1),(2,1)]],
			 	['-', 2,[(0,3),(1,3)]],
			 	['-', 1,[(0,1),(0,2)]],
			 	['+',10,[(1,2),(2,2),(2,3)]],
			 	['+', 9,[(3,1),(3,2),(3,3)]]
				]
		self.assertEqual (is_valid(board,cages,True),True)

	############################################################
	
	def test_get_board_string_01 (self): self.assertEqual (get_board_string(board0()),'     [0] [1] [2]\n    -------------\n[0] | 3 | . | 2 |\n[1] | 2 | 3 | . |\n[2] | . | 2 | . |\n    -------------')
	def test_get_board_string_02 (self): self.assertEqual (get_board_string(board2()),'     [0] [1] [2] [3]\n    -----------------\n[0] | 2 | 4 | . | . |\n[1] | 1 | 2 | 3 | 4 |\n[2] | 3 | 1 | . | . |\n[3] | 4 | 3 | . | . |\n    -----------------')
	def test_get_board_string_03 (self): self.assertEqual (get_board_string([[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]),'     [0] [1] [2] [3]\n    -----------------\n[0] | . | . | . | . |\n[1] | . | . | . | . |\n[2] | . | . | . | . |\n[3] | . | . | . | . |\n    -----------------')
	def test_get_board_string_04 (self): self.assertEqual (get_board_string([[4]]),'     [0]\n    -----\n[0] | 4 |\n    -----')

	############################################################
	
	def test_extra_credit_get_missing_numbers_row_or_col_01 (self): 
		self.check_get_missing_numbers_1() 
		self.check_get_missing_numbers_2() 
		self.check_get_missing_numbers_3() 
		self.check_get_missing_numbers_4() 
		self.check_get_missing_numbers_5() 
		
	def check_get_missing_numbers_1(self):self.assertEqual(get_missing_numbers_row_or_col([1,2]),[])	  # no values missing
	def check_get_missing_numbers_2(self):self.assertEqual(get_missing_numbers_row_or_col([1,None,2]),[3])
	def check_get_missing_numbers_3(self):self.assertEqual(get_missing_numbers_row_or_col([None,None,None]),[1,2,3]) # all missing
	def check_get_missing_numbers_4(self):self.assertEqual(get_missing_numbers_row_or_col([None,None,1]),[2,3]) # 1 is in place
	def check_get_missing_numbers_5(self):self.assertEqual(get_missing_numbers_row_or_col([1,1,1]),[2,3]) # 1 is in place

	############################################################
	def test_extra_credit_candidates_at_location_01 (self): 
		self.check_candidates_at_location_1()
		self.check_candidates_at_location_2()
		self.check_candidates_at_location_3() 

	def test_extra_credit_candidates_at_location_02 (self): 
		self.check_candidates_at_location_4()
		self.check_candidates_at_location_5()
		self.check_candidates_at_location_6()
		
	def check_candidates_at_location_1(self):self.assertEqual(candidates_at_location([[None]], (0,0)),[1])
	def check_candidates_at_location_2(self):self.assertEqual(candidates_at_location([[1]], (0,0)),None)	# location already contains a value 
	def check_candidates_at_location_3(self):self.assertEqual(candidates_at_location([[None]], (1,1)),None) # location is invalid

	def check_candidates_at_location_4(self):self.assertEqual(candidates_at_location([[1,2,3],[2,3,1],[3,None,None]], (2,1)),[1])
	def check_candidates_at_location_5(self):self.assertEqual(candidates_at_location([[1,2,3],[1,3,2],[1,None,None]], (2,1)),[])
	def check_candidates_at_location_6(self):self.assertEqual(candidates_at_location(board2(),(0,2)),[1])

			
	############################################################
	def test_extra_credit_is_symmetric_01 (self): 
		self.check_is_symmetric_1()
		self.check_is_symmetric_2()
		self.check_is_symmetric_3()
		
	def test_extra_credit_is_symmetric_02 (self): 
		self.check_is_symmetric_4()
		self.check_is_symmetric_5()
		self.check_is_symmetric_6()
				
	def check_is_symmetric_1(self): self.assertEqual(is_symmetric(board0()),False)
	def check_is_symmetric_2(self): self.assertEqual(is_symmetric(board4()),False)
	def check_is_symmetric_3(self): self.assertEqual(is_symmetric([[None]]),True)
	def check_is_symmetric_4(self): self.assertEqual(is_symmetric([[1,2],[1,2]]),False)
	def check_is_symmetric_5(self): 
		board = [[1,2,3],[2,3,1],[3,1,2]]
		self.assertEqual(is_symmetric(board),True)
		self.assertEqual(board, [[1,2,3],[2,3,1],[3,1,2]]) #board not changed
		
	def check_is_symmetric_6(self): 
		board = [[4,1,2,3],[1,2,3,4],[2,3,4,1],[3,4,1,2]]
		self.assertEqual(is_symmetric(board),True)
		self.assertEqual(board,[[4,1,2,3],[1,2,3,4],[2,3,4,1],[3,4,1,2]])

# This class digs through AllTests, counts and builds all the tests,
# so that we have an entire test suite that can be run as a group.
class TheTestSuite (unittest.TestSuite):
	# constructor.
	def __init__(self,wants):
		# find all methods that begin with "test".
		fs = []
		for w in wants:
			for func in AllTests.__dict__:
				# append regular tests
				# drop any digits from the end of str(func).
				dropnum = str(func)
				while dropnum[-1] in "1234567890":
					dropnum = dropnum[:-1]
				
				if dropnum==("test_"+w+"_") and (not (dropnum==("test_extra_credit_"+w+"_"))):
					fs.append(AllTests(str(func)))
				if dropnum==("test_extra_credit_"+w+"_") and not BATCH_MODE:
					fs.append(AllTests(str(func)))
		
		# call parent class's constructor.
		unittest.TestSuite.__init__(self,fs)

class TheExtraCreditTestSuite (unittest.TestSuite):
		# constructor.
		def __init__(self,wants):
			# find all methods that begin with "test_extra_credit_".
			fs = []
			for w in wants:
				for func in AllTests.__dict__:
					if BATCH_MODE and str(func).startswith("test_extra_credit_"+w):
						fs.append(AllTests(str(func)))
		
			# call parent class's constructor.
			unittest.TestSuite.__init__(self,fs)

# all (non-directory) file names, regardless of folder depth,
# under the given directory 'dir'.
def files_list(dir):
	info = os.walk(dir)
	filenames = []
	for (dirpath,dirnames,filez) in info:
#		print(dirpath,dirnames,filez)
		if dirpath==".":
			continue
		for file in filez:
			filenames.append(os.path.join(dirpath,file))
#		print(dirpath,dirnames,filez,"\n")
#		filenames.extend(os.path.join(dirpath, filez))
	return filenames

def main():
	if len(sys.argv)<2:
		raise Exception("needed student's file name as command-line argument:"\
			+"\n\t\"python3 tester4L.py gmason76_2xx_L4.py\"")
	want_all = len(sys.argv) <=2
	wants = []
	
	# remove batch_mode signifiers from want-candidates.
	want_candidates = sys.argv[2:]
	for i in range(len(want_candidates)-1,-1,-1):
		if want_candidates[i] in ['.'] or os.path.isdir(want_candidates[i]):
			del want_candidates[i]
	
	if not want_all:
		#print("args: ",sys.argv)
		for w in want_candidates:
			if w in REQUIRED_DEFNS:
				wants.append(w)
			else:
				raise Exception("asked to limit testing to unknown function '%s'."%w)
	else:
		wants = REQUIRED_DEFNS

	if not BATCH_MODE:
		#time.sleep(1) #make sure there is a time gap between last check run and this one
		#run_file(sys.argv[1],wants)
		if not want_all:
			run_file(sys.argv[1],wants)
		else:
			if len(extra_credit) == 0:
				(tag, passed1,tried1,ec) = run_file(sys.argv[1],wants)

				print('='*40)
				print("\nTest cases: %d/%d passed" % (passed1,tried1) )
				print("Score based on test cases: %.0f/100" % (passed1*weight_required))
			
			else:	
				print("Testing required functions:")			
				(tag, passed1,tried1,ec) = run_file(sys.argv[1],wants[:-len(extra_credit)])
				if passed1 == None:
					return

				print("\nTesting extra credit functions:")			
				(tag, passed2,tried2,ec) = run_file(sys.argv[1],extra_credit)
				if passed2!= None:
					print('='*40)
					print("Required test cases: %d/%d passed" % (passed1,tried1) )
					print("Extra credit test cases: %d/%d passed" % (passed2, tried2))
					print("Score based on test cases: %.2f (%.2f+%d) " % (passed1*weight_required+passed2*weight_extra_credit, 
														passed1*weight_required, passed2*weight_extra_credit))

				else:
					print('='*40)
					print("Required test cases: %d/%d passed" % (passed1,tried1) )
					print("Extra credit test cases: 0 passed")
					print("Score based on test cases: %.2f (%.2f+0) " % (passed1*weight_required, 
														passed1*weight_required))

	else:
		filenames = files_list(sys.argv[1])
	
# 		print(filenames)
	
		results = []
		for filename in filenames:
			try:
				print("\n\n\nRUNNING: "+filename)
				(tag, passed,tried,ec) = run_file(filename,wants)
				results.append((tag,passed,tried,ec))
			except SyntaxError as e:
				results.append((filename+"_SYNTAX_ERROR",0,1))	
			except NameError as e:
				results.append((filename+"_Name_ERROR",0,1))	
			except ValueError as e:
				results.append(filename+"_VALUE_ERROR",0,1)
			except TypeError as e:
				results.append(filename+"_TYPE_ERROR",0,1)
			except ImportError as e:
				results.append((filename+"_IMPORT_ERROR_TRY_AGAIN	",0,1))	
			except Exception as e:
				results.append(filename+str(e.__reduce__()[0]),0,1)
			
		print("\n\n\nGRAND RESULTS:\n")
		for (tag, passed, tried, ec) in results:
			print(("%.0f%%  (%d/%d, %dEC) - " % (passed/tried*100 + ec, passed, tried, ec))+tag)

def try_copy(filename1, filename2, numTries):
	have_copy = False
	i = 0
	while (not have_copy) and (i < numTries):
		try:
			# move the student's code to a valid file.
			shutil.copy(filename1,filename2)
			
			# wait for file I/O to catch up...
			if(not wait_for_access(filename2, numTries)):
				return False
				
			have_copy = True
		except PermissionError:
			print("Trying to copy "+filename1+", may be locked...")
			i += 1
			time.sleep(1)
	
	if(i == numTries):
		return False
	return True
			
def try_remove(filename, numTries):
	removed = False
	i = 0
	while os.path.exists(filename) and (not removed) and (i < numTries):
		try:
			os.remove(filename)
			removed = True
		except OSError:
			print("Trying to remove "+filename+", may be locked...")
			i += 1
			time.sleep(1)
	if(i == numTries):
		return False
	return True

def wait_for_access(filename, numTries):
	i = 0
	while (not os.path.exists(filename) or not os.access(filename, os.R_OK)) and i < numTries:
		print("Waiting for access to "+filename+", may be locked...")
		time.sleep(1)
		i += 1
	if(i == numTries):
		return False
	return True

# this will group all the tests together, prepare them as 
# a test suite, and run them.
def run_file(filename,wants=[]):
	if(not try_copy(filename,"student.py", 5)):
		print("Failed to copy " + filename + " to student.py.")
		quit()
	
	# import student's code, and *only* copy over the expected functions
	# for later use.
	import imp
	count = 0
	while True:
		try:
			import student
			imp.reload(student)
			break
		except ImportError as e:
			print("import error getting student.. trying again. "+os.getcwd(), os.path.exists("student.py"))
			time.sleep(0.5)
			count+=1
			if count>3:
				raise ImportError("too many attempts at importing!")
		except SyntaxError as e:
			print("SyntaxError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return((filename+"_SYNTAX_ERROR",None,1,0))
		except NameError as e:
			print("NameError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return((filename+"_Name_ERROR",None,1,0))	
		except ValueError as e:
			print("ValueError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_VALUE_ERROR",None,1,0)
		except TypeError as e:
			print("TypeError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_TYPE_ERROR",None,1,0)
		except ImportError as e:			
			print("ImportError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details or try again")
			return((filename+"_IMPORT_ERROR_TRY_AGAIN	",None,1,0))	
		except Exception as e:
			print("Exception in loading"+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+str(e.__reduce__()[0]),None,1,0)
		#except Exception as e:
		#	print("didn't get to import student yet... " + e)
	# but we want to re-load this between student runs...
	# the imp module helps us force this reload.s
	
	import student
	imp.reload(student)
	
	# make a global for each expected definition.
	def decoy(name):
		return (lambda x: "<no '%s' definition found>" % name)
		
	for fn in wants:#REQUIRED_DEFNS
		globals()[fn] = decoy(fn)
		try:
			globals()[fn] = getattr(student,fn)
		except:
			print("\nNO DEFINITION FOR '%s'." % fn)	
			if fn in extra_credit:
				return ("no extra",0,0,0)
	
	# create an object that can run tests.
	runner1 = unittest.TextTestRunner()
	
	# define the suite of tests that should be run.
	suite1 = TheTestSuite(wants)
	
	# let the runner run the suite of tests.
	ans = runner1.run(suite1)
	num_errors   = len(ans.__dict__['errors'])
	num_failures = len(ans.__dict__['failures'])
	num_tests    = ans.__dict__['testsRun']
	num_passed   = num_tests - num_errors - num_failures
	# print(ans)

	if BATCH_MODE:
		# do the same for the extra credit.
		runnerEC = unittest.TextTestRunner()
		suiteEC = TheExtraCreditTestSuite(wants)
		ansEC = runnerEC.run(suiteEC)
		num_errorsEC   = len(ansEC.__dict__['errors'])
		num_failuresEC = len(ansEC.__dict__['failures'])
		num_testsEC    = ansEC.__dict__['testsRun']
		num_passedEC   = num_testsEC - num_errorsEC - num_failuresEC
		print(ansEC)
	else:
		num_passedEC = 0
	
	# remove our temporary files.
	if os.path.exists("__pycache__"):
		shutil.rmtree("__pycache__", ignore_errors=True)
	if(not try_remove("student.py", 5)):
		print("Failed to copy " + filename + " to student.py.")
	
	tag = ".".join(filename.split(".")[:-1])
	return (tag, num_passed, num_tests,num_passedEC)

# this determines if we were imported (not __main__) or not;
# when we are the one file being run, perform the tests! :)
if __name__ == "__main__":
	main()
