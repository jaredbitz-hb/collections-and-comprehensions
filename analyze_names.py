"""
analyze_names.py

Run this file in the interpreter (python3 -i analyze_names.py)
and then call any of the functions to demo them!
"""

def load_data(filename):
    """Load the rows of the CSV file [filename]"""
    result = []

    csv_file = open(filename)
    for row in csv_file:
        data = row.rstrip().split(',')
        # Tuples are more efficient than lists - less overhead
        data_tuple = tuple(data)
        result.append(data_tuple)
    csv_file.close()

    return result

def count_unique_names_inefficient():
    """Use a list to get all the unique names in the dataset."""
    name_data = load_data('names_CA.csv')
    unique_names = []
    for row in name_data:
        if row[0] not in unique_names:
            unique_names.append(row[0])
    print(len(unique_names))

def count_unique_names_faster():
    """Use a set to get all the unique names in the dataset."""
    name_data = load_data('names_CA.csv')
    unique_names = set()
    for row in name_data:
        unique_names.add(row[0])
    print(len(unique_names))

def find_khaleesi():
    """Finds all rows with the name 'Khaleesi'"""
    
    name_data = load_data('names_CA.csv')

    matches = [ row for row in name_data if row[0] == 'Khaleesi' ]
    """
    The line above is equivalent to this code:

    matches = []
    for row in name_data:
        if row[0] == 'Khaleesi':
            matches.append(row)
    """

    print(matches)

def count_khaleesi():
    """Finds the total number of babies in the record named 'Khaleesi'"""
    name_data = load_data('names_CA.csv')

    counts = [ int(row[2]) for row in name_data if row[0] == 'Khaleesi' ]
    total = sum(counts)
    print(total)

def find_names_greater_than_1000():
    """Finds the names from all rows with > 1000 babies"""
    name_data = load_data('names_CA.csv')

    # We use a set comprehension here (curly braces {}) to avoid duplicates
    matches = { row[0] for row in name_data if int(row[2]) > 1000}
    print(matches)

def find_most_common_year(name):
    """Finds the year where [name] was most common"""
    name_data = load_data('names_CA.csv')

    matches = [row for row in name_data if row[0] == name]
    try:
        top = max(matches, key=lambda row: int(row[2]))
        print(top)
    except:
        print("That name isn't in the list!")
      