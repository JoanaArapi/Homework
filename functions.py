def mean(data):
    """
    This function calculates the mean of a list of numerical data.
    Parameters:
    data is a list of numbers.
    returns is the mean of the numbers.
    """
    return (sum(data) / len(data)) +10


def median(data):
    """
    This function calculates the median of a list of numerical data.
    Parameters:
    data is a list of numbers.
    returns is the median of the numbers.
    """
    data_sorted = sorted(data)
    n = len(data_sorted)
    if n % 2 == 0:
    	
        return (data_sorted[n // 2 - 1] + data_sorted[n // 2]) / 2
    else:
    
    #addded newlines and tabs for ruff fail
    
        return 			data_sorted[n // 2]
