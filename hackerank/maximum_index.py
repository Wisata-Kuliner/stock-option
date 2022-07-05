# Python3 program for the above approach

# Function to find the maximum
# index the pointer can reach
def maximumIndex(N, B):
	
	max_index = 0

	# Calculate maximum possible
	# index that can be reached
	for i in range(1, N + 1):
		max_index += i

	current_index = max_index
	step = N

	while (1):

		# Check if current index and step
		# both are greater than 0 or not
		while (current_index > 0 and N > 0):

			# Decrement current_index by step
			current_index -= N

			# Check if current index is
			# equal to B or not
			if (current_index == B):

				# Restore to previous index
				current_index += N

			# Decrement step by one
			N -= 1

		# If it reaches the 0th index
		if (current_index <= 0):
			
			# Print result
			print(max_index)
			break

		# If max index fails to
		# reach the 0th index
		else:
			N = step

			# Store max_index - 1 in current index
			current_index = max_index - 1

			# Decrement max index
			max_index -= 1

			# If current index is equal to B
			if (current_index == B):
				current_index = max_index - 1

				# Decrement current index
				max_index -= 1

# Driver Code
if __name__ == '__main__':
	
	N = 3
	B = 2
	
	maximumIndex(N, B)

# This code is contributed by mohit kumar 29
