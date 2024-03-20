#!/usr/bin/python3

"""Exports data to CSV"""

import csv
import requests
import sys


if __name__ == "__main__":
    APIURL = "https://jsonplaceholder.typicode.com/"
    FileName = "{}.csv".format(sys.argv[1])
    EmployeeName = requests.get(APIURL + "/users/{}".format(sys.argv[1]))
    EmployeeJD = EmployeeName.json()
    ToDos = requests.get(APIURL + "/users/{}/todos".format(sys.argv[1]))
    ToDosJD = ToDos.json()
    File = open(FileName, "w")
    CSVF = csv.writer(File, quoting=csv.QUOTE_ALL)
    for ToDo in ToDosJD:
        CSVF.writerow([
            EmployeeJD["id"],
            EmployeeJD["username"],
            ToDo["completed"],
            ToDo["title"]
            ])
    File.close()
