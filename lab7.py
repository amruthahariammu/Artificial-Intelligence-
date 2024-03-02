from itertools import permutations
def solve_cryptarithmetic():
    for values in permutations(range(10), 8):
        f,i,r,s,t,h,d = values
        if f != 0 and t!= 0: 
            first = f * 10000 +i * 1000 + r * 100 + s * 10 + t
            first = f * 10000 +i * 1000 + r * 100 + s * 10 + t
            third = t * 10000 + h * 1000 + i * 100 + r * 10 + d
            if first + first == third:
                return first, first , thrid

result = solve_cryptarithmetic()
if result:
    first, first, thrid = result
    print(f"FIRST = {first},FIRST = {first}, THRID = {thrid}")
else:
    print("No solution found.")
