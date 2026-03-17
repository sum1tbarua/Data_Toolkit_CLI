import csv, logging

def load_csv(filename) -> list:
    """
    Arg: filename -> str
    Output: A list with dictionaries.
    """
    data = []
    
    try:
        with open(filename) as file:
            csv_reader = csv.DictReader(file) 
            for row in csv_reader:
                data.append(row)
            logging.info("File has been imported.")
    except FileNotFoundError:
        logging.error(f'File {filename} Not found. Please try again with the correct file.')
    
    return data
    