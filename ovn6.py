def limit_to_5_high_scores(results):
	return [res for res_index, res in enumerate(results) if res_index < 5]


def save_results(results):
	results = limit_to_5_high_scores(results)

	to_save = [f'{res["name"]},{res["points"]}\n' for res in results]

	with open('high_scores.txt', 'w+') as f:
		f.writelines(to_save)


def print_results(results):
	for res_index, res in enumerate(results):
		if res_index < 5:
			print(f'{res_index + 1} {res["name"]} \t\t {res["points"]}')


def parse_results(results):
	parsed = []

	for line in results:
		line = line.split(',')

		parsed.append({
			'name': line[0],
			'points': int(line[1])
		})

	return parsed


def deep(obj, rule):
	rule_key = list(rule.keys())[0]
	rule_val = rule[rule_key]

	for element in obj:
		if str(element[rule_key]) == str(rule_val):
			return element


def sort_results(results):
	import quicksort

	if len(results) < 2:
		return results

	points = [result['points'] for result in results]

	sorted_points = quicksort.sort(points)

	return [
		deep(results, {'points': sorted_point}) for sorted_point in sorted_points
	]


def new_entry(results):
	name = input('Ange nytt namn: ')
	points = int(input('Ange poäng: '))

	with open('high_scores.txt', 'a+') as f:
		f.write(f'{name},{points}\n')


def start():
	import os

	print('High scores')

	results = []

	if os.path.isfile(f'{os.getcwd()}/high_scores.txt'):
		with open('high_scores.txt') as f:
			results = f.readlines()

	if not results:
		print('Inga resultat registrerade')
	else:
		results = sort_results(parse_results(results))[::-1]

		print_results(results)
		save_results(results)

	new_entry(results)


while True:
	start()
