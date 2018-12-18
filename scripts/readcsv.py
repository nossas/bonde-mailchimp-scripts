import csv
import hashlib


def member_list_id(csv_path):
    """
    Takes the first column of csv which should be
    an email and returns a list of member ids
    """
    member_ids = []
    with open(csv_path) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            email = row[0]
            member_id = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
            member_ids.append(member_id)

    return member_ids
