import os
import pandas as pd

def get_emails():
    """
    Opens up "emails.xlsx" and re-orginizes the data as a list of tuples where the first
    item in the tuple is the name under the "Name" column in "emails.xlsx" and the second
    item is the email associated with thate name.

    :return: a list of tuples
    """
    pair_list = []
    # Extract emails and names from excel sheet
    names = pd.read_excel('emails.xlsx', usecols='A')
    emails = pd.read_excel('emails.xlsx', usecols='B')
    # Convert from pd.Dataframe to list
    name_list = names.values.tolist()
    email_list = emails.values.tolist()
    # Restructure data so that emails and names are paired in tuples and then placed in a list
    length = len(names)
    for n in range(length):
        #Checks if empty cell in excel sheet
        print(type(name_list[n][0]))
        if type(name_list[n][0]) != float and type(email_list[n][0]) != float:
            holder = tuple([name_list[n][0], email_list[n][0]])
            #print(holder)
            pair_list.append(holder)
            #print(pair_list)

    return pair_list
