"""
Project: algorithms-exercises-using-python
Created by robin1885@github on 17-2-20.
"""


def anagram_solution1(s1, s2):
    """


    @rtype : bool
    @param s1: str1
    @param s2: str2
    @return: True or False
    """
    anagram_list = list(s2)

    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(anagram_list) and not found:
            if s1[pos1] == anagram_list[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            anagram_list[pos2] = None
        else:
            still_ok = False

        pos1 += 1

    return still_ok

if __name__ == "__main__":
    print(anagram_solution1('abcd', 'dcba'))
    print(anagram_solution1('heart', 'earth'))
    print(anagram_solution1('python', 'typhon'))