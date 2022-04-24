# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(qualifying_loans, csvpath):
    """Saves the qualifying loans to a CSV file. 
    
    Args:
        qualifying_loans (list of lists): The qualified bank loans.
        csvpath: A direct path to save the file into 
        
    Returns:
        A CSV file saved as whatever name the user inputs that is located in
        the folder the user inputs
    """
    #header is first as it is the "header" insided the csv/table.  square brackets and then the name of 
    #each header within the square brackets with ""
    header = ["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"]
    #with open is next, the reverance csvpath as it's in the arguments for save_csv, 'w' means write, and 
    #newline='' we leave open since the new line will be filled with whatever information that is pulled from 
    #the list.  csvwriter is the  new variable that we create that will equal csvfile when called. 
    #csvwriter.writerow(header) tells us to write the header
    #for "row" - row can be anything word such as unicorn - in qualifying loans - needed to bring in the 
    #second argument with qualifying loans - we repeat row and add .values().  values will be pulled from 
    #list
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(header)

        for row in qualifying_loans:
            csvwriter.writerow(row.values())  
            