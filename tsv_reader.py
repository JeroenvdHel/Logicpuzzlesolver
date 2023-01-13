import csv
from pprint import PrettyPrinter


def parse_data(tsv_file):
	with open(tsv_file, "r", encoding="utf8") as df:
		tsv_reader = csv.DictReader(df, delimiter="\t")
		data = []

		headers = tsv_reader.fieldnames

		for name in tsv_reader.fieldnames:
			data.append([name, []])

		for row in tsv_reader:
			for n in data:
				n[1].append(row[n[0]])

	return (headers, data)


def parse_clues(tsv_file):
	with open(tsv_file, "r", encoding="utf8") as df:
		tsv_reader = csv.reader(df, delimiter="\t")
		clues = []

		for row in tsv_reader:
			clues.append(row)

	return clues


def parse_txt(txtfile):
	with open(txtfile, "r", encoding="utf8") as f:
		lines = f.readlines()
		datatype = ""
		data = []
		clues = []

		for line in lines:
			line = line.strip()
			if "CLUES" in line:
				datatype = "clues"
				continue
			if "DATA" in line:
				datatype = "data"
				continue

			if datatype == "clues":
				print(f"Clue: [{line}]")
				
			elif datatype == "data":
				print(f"Data: [{line}]")
			else:
				print("No clue or data")


def parse_clueline(line):
	


if __name__ == '__main__':
	# pp = PrettyPrinter(indent=4)

	# data = parse_data('data.tsv')
	# pp.pprint(data)
	# print("\n##################################################\n")
	# clues = parse_clues('clues.tsv')
	# pp.pprint(clues)
	f = r'puzzles/1/data.txt'
	parse_txt(f)
