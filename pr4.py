def ch_even(number):
	if number % 2 == 0:
		return True
	else:
		return False

def cut_paper(size,paper_count_req):
	paper_count = 1
	if ch_even(size[0]) or ch_even(size[1]):
		flag = False
		i = 0
		while ch_even(size[0]) or ch_even(size[1]):
			# print(size)
			
			if paper_count >= paper_count_req:
				flag = True
				break
			else:
				
				if i == 0:
					i = i + 1
				else:
					i = i - 1

				if ch_even(size[i]):
					size[i] = size[i] / 2
					paper_count = paper_count + paper_count
				if paper_count >= paper_count_req:
					flag = True
				# print(paper_count)
		return flag
	else:
		if paper_count >= paper_count_req:
			return True
		else:
			return False
number_of_test_case = int(input())
for _ in range(number_of_test_case):
	temp = list(map(int,input().split(" ")))
	# print(temp[:-1],temp[-1])
	if cut_paper(temp[:-1],temp[-1]):
		print('YES')
	else:
		print('NO')
