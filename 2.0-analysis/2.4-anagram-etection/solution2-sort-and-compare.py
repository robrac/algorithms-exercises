""" 
Project: algorithms-exercises-using-python
Created by robin1885@github on 17-2-20.
"""


def anagram_solution2(s1, s2):
    """


    @rtype : bool
    @param s1: str1
    @param s2: str2
    @return: True or False
    """
    anagram_list1 = list(s1)
    anagram_list2 = list(s2)

    anagram_list1.sort()
    anagram_list2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if anagram_list1[pos] == anagram_list2[pos]:
            pos += 1
        else:
            matches = False

    return matches

if __name__ == "__main__":
    print(anagram_solution2('abcde', 'edcba'))
