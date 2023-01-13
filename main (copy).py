#pylint:disable=W0401
from constraint import Problem, AllDifferentConstraint
from tsv_reader import parse_data, parse_clues

p = Problem()
datafile = 'data.tsv'
cluesfile = 'clues.tsv'

data = parse_data(datafile)
clues = parse_clues(cluesfile)

criteria_items = []
for i in data:
	criteria_items += i[1]

p.addVariables(criteria_items, list(range(1, len(data[0][1]) + 1)))
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
for i in range(1, len(data[0][1]) + 1):
	r = []
	print("--------------------")
	for x in solution:
		if solution[x] == i:
			r.append(x)
	print(f"{i}: {r}")
