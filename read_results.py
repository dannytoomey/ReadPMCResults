import sys

open_file = str(sys.argv[1])
print("reading file "+open_file)

with open(open_file,"r") as results:
	lines = results.readlines()

	result_num = 0
	result_num_array = []
	title = []
	authors = []
	publication_info = []
	pmc_id = []

	count = 0

	for line in lines:
		as_list = line.split(", ")
		appended = False

		if count == 0 and appended != True:
			line = as_list[0].replace("\n","")

			title.append([as_list[0].replace("\n","")])
			result_num += 1
			result_num_array.append([result_num])

			appended = True
			count += 1

		if count == 1 and appended != True:
			if as_list != ['\n']:
				authors.append([as_list[0].replace("\n","")])

			else:
				authors.append(["No authors listed"])

			appended = True
			count += 1

		if count == 2 and appended != True:
			if as_list != ['\n']:
				publication_info.append([as_list[0].replace("\n","")])
			else:
				publication_info.append(["No publication information listed"])

			appended = True
			count += 1

		if count == 3 and appended != True:
			tmp = as_list[0].replace("\n","")
			pmc_id.append([tmp.replace("PMCID: ","")])

			appended = True
			count += 1

		if count == 4 and appended != True:
			if as_list == ['\n']:
				count = 0
				appended = True


import csv

fields = ['Result Number','Title','Authors','Publication Info','PMC ID']
rows = []

print("num resuts: "+str(len(result_num_array)))
print("num titles: "+str(len(title)))
print("num authors: "+str(len(authors)))
print("num publication info: "+str(len(publication_info)))
print("num pmc ids: "+str(len(pmc_id)))

num_resuls = max(result_num_array)
for row in range(0,num_resuls[0]):
	#print(row)
	rows.append([result_num_array[row],title[row],authors[row],publication_info[row],pmc_id[row]])


clean_rows = []
for row in range(0,len(rows[:])):
	this_col = []
	for col in range (0,len(rows[0][:])):
		cell = rows[row][col][0]
		this_col.append(cell)
	clean_rows.append(this_col)

file = str(open_file.split(".txt")[0])+'_cleaned_results.csv'

with open(file,'w') as csv_file:
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(fields)
	csv_writer.writerows(clean_rows)

print("saved new CSV file named "+file)
