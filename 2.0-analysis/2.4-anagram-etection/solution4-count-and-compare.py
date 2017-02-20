""" 
Project: algorithms-exercises-using-python
Created by robin1885@github on 17-2-20.
"""


def anagram_solution4(s1, s2):
    """


    @rtype : bool
    @param s1: str1
    @param s2: str2
    @return: True or False
    """
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j += 1
        else:
            still_ok = False

    return still_ok


if __name__ == "__main__":
    print(anagram_solution4('apple', 'pleap'))