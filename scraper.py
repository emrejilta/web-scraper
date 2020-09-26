#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://redis.io/commands"

# Gets the entire html
content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(content, "lxml")

# D
section = soup.find_all("section", attrs={"id": "commands"})
container = section[0].find_all("div", attrs={"class": "container"})

# Due to 2 div's named "container", the second one is chosen
commands = container[1].find_all("li")

# The headings of the table
headings = ["Command", "Arguments", "Summary"]

# The matrix to be shown as table
all_rows = []

for i in range(len(commands)):
    row = []

    # Commands
    command = commands[i].find_all("span", attrs={"class": "command"})
    row.append(command[0].contents[0].strip())

    # Parameters
    args = commands[i].findAll("span", attrs={"class": "args"})
    row.append(args[0].text.strip())

    # Description
    summary = commands[i].findAll("span", attrs={"class": "summary"})
    row.append(summary[0].text)

    all_rows.append(row)




df = pd.DataFrame(data=all_rows, columns=headings)
df.to_csv("Redis-Commands.csv")
