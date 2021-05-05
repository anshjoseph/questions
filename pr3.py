"""
For the New Year, Polycarp decided to send postcards to all his n friends. He wants to make postcards with his own hands. For this purpose, he has a sheet of paper of size w×h, which can be cut into pieces.

Polycarp can cut any sheet of paper w×h that he has in only two cases:

If w is even, then he can cut the sheet in half and get two sheets of size w2×h;
If h is even, then he can cut the sheet in half and get two sheets of size w×h2;
If w and h are even at the same time, then Polycarp can cut the sheet according to any of the rules above.

After cutting a sheet of paper, the total number of sheets of paper is increased by 1.

Help Polycarp to find out if he can cut his sheet of size w×h at into n or more pieces, using only the rules described above.


Input
The first line contains one integer t (1≤t≤104) — the number of test cases. Then t test cases follow.

Each test case consists of one line containing three integers w, h, n (1≤w,h≤104,1≤n≤109) — the width and height of the sheet Polycarp has and the number of friends he needs to send a postcard to.

Output
For each test case, output on a separate line:

"YES", if it is possible to cut a sheet of size w×h into at least n pieces;
"NO" otherwise.
You can output "YES" and "NO" in any case (for example, the strings yEs, yes, Yes and YES will be recognized as positive).


Example
input
5
2 2 3
3 3 2
5 10 2
11 13 1
1 4 4

output
YES
NO
YES
YES
YES
"""
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
