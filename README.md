# JCPSHomelessPopulation

By Jaime Duncan

My project looks to see the total amount of homeless stundents enrolled in JCPS for the school year 2020-2021. These are students without permanent evening addresses.
Meaning students staying with friends, relatives, at shelters, in vehicles, in hotels, or other non permanent places. The data I used comes from the JCPS open district 
database on the JCPS website. The excel files with the homeless data gives suppressed information and total information. Meaning some numbers were withheld from specific 
columns to protect privacy (e.g. there many only be 1 homeless student that identifies as American Indian in the school, if that is listed, that student could easily be 
identified). You can see these numbers in the enrollment files.

Install and import to run

Pip install notebook
Pip install openpyxl

import pandas as pd
import matplotlib.pyplot as plt

Required features

  *Read in data using Pandas read_excel function
  *Clean and manipulate data (e.g. eliminating unwanted columns and rows)
  *Analyzing the data (e.g. creating datframes, sorting rows alphabetically and numerically, finding the percentage)
  *Created pie charts to visualized the supressed homeless population vs total homeless population
  *Used Markdown cells to explain what I did to the data
