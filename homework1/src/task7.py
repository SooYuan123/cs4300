#I choose numpy for task7
import numpy as np

#function to calculate simple statistics
def calculate_stats(num):

	arr = np.array(num)	#array
	mean = np.mean(arr)
	median = np.median(arr)
	std_dev = np.std(arr)	#standard deviation

	return {
		"mean": mean,
		"median": median,
		"std_dev": std_dev
	}


if __name__=="__main__":
	lab_data = [23,50,80,37,66]
	results = calculate_stats(lab_data)

	print(f"Mean: {results['mean']}")
	print(f"Median: {results['median']}")
	print(f"Standard Deviation: {results['std_dev']}")
