import cvs
print("╭━━━╮╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╭╮╱╭╮╱╱╱╱╭━╮╱╱╱╱╱╭┳╮╱╱╱╱╱╱╱╱╭╮\┃╭━╮┃╱╱╱╱╱╰╮╭╮┃╱╱╱╱╱╱╱╱╱┃┃╱┃┃╱╱╱╱┃╭╯╱╱╱╱╱┃┃┃╱╱╱╱╱╱╱╱┃┃\┃╰━━┳━━┳━╮╱┃┃┃┣┳━━┳━━┳━━┫┃╱┃┣━╮╭┳╯╰┳┳━━┳━╯┃┃╱╱╭━━┳━━┫┃╭┳╮╭┳━━╮\╰━━╮┃╭╮┃╭╮╮┃┃┃┣┫┃━┫╭╮┃╭╮┃┃╱┃┃╭╮╋╋╮╭╋┫┃━┫╭╮┃┃╱╭┫╭╮┃╭╮┃╰╯┫┃┃┃╭╮┃\┃╰━╯┃╭╮┃┃┃┣╯╰╯┃┃┃━┫╰╯┃╰╯┃╰━╯┃┃┃┃┃┃┃┃┃┃━┫╰╯┃╰━╯┃╰╯┃╰╯┃╭╮┫╰╯┃╰╯┃\╰━━━┻╯╰┻╯╰┻━━━┻┻━━┻━╮┣━━┻━━━┻╯╰┻╯╰╯╰┻━━┻━━┻━━━┻━━┻━━┻╯╰┻━━┫╭━╯\╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃\╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯")

print("What year are you looking for?)
datayear = input('STATE')

print("What name or job title are you looking for?")
search_str = input('STATEMENT')

with open('San Diego Data ' + datayear + '.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for column in row:
            if search_str in column:
                print(row)
