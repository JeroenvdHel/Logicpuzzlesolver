#pylint:disable=W0401
from constraint import Problem, AllDifferentConstraint
# from tsv_reader import parse_data, parse_clues
from txt_reader import parse_txt

p = Problem()
# datafile = 'data.tsv'
# cluesfile = 'clues.tsv'
datafile = r'puzzles/einstein/moeilijk/1/data.txt'
# datafile_part = input()

data, clues = parse_txt(datafile)
# clues = parse_clues(cluesfile)
groups = len(data[0][1])
domains = len(data)
criteria_items = []
for i in data:
	criteria_items += i[1]

p.addVariables(criteria_items, list(range(1, groups + 1)))
for row in data:
	# p.addConstraint(AllDifferentConstraint(), cat)
	p.addConstraint(AllDifferentConstraint(), row[1])


def no_match(a, b):
	return a != b


def match(a, b):
	return a == b


for clue in clues:
	if clue[2] == '1':
		p.addConstraint(match, (clue[0], clue[1]))
	else:
		p.addConstraint(no_match, (clue[0], clue[1]))

solutions = p.getSolutions()
solution = solutions[0]
print(len(solution))

sorteddict = {}
for d in range(domains):
	# globals()[f"d{d+1}"] = []
	sorteddict[f"d{d+1}"] = []

for i in range(1, domains + 1):
	r = []

	print("--------------------")
	for x in solution:
		if solution[x] == i:
			y = [x, solution[x], i]
			domain = ''
			for idx, d in enumerate(data, start=1):
				if x in d[1]:
					domain = idx
					break
			r.append([x, solution[x], domain])

	r.sort(key=lambda x: x[2])
	# print(r)
	sorted = [x[0] for x in r]
	print(sorted)
	# for c in range(domains):
	# 	r.append(sorteddict[f"d{c+1}"][i-1])
	# print(f"{i}: {r}")

	# for x in solution:
	# 	if solution[x] == i:
	# 		r.append(x)
	# print(f"{i}: {r}")
