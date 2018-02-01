import sys 

def main():

  test_array = []
 # str_array = []

  str_array = raw_input('Enter a series of numbers delimited by \',\': ')   
  print 'You entered: ' + str_array

  for item in str_array:
	if item !=',':
		test_array.append(int(item))

  print test_array
  print type(test_array)
  #print (test_array.sort())

if __name__ == '__main__':
  main()
