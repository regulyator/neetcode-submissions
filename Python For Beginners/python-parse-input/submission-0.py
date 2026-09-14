from typing import List

def read_integers() -> List[int]:
    result = []
    for el in input().split(","):
        result.append(int(el))
    return result

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
