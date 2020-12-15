
import sys
import math

def compute_join_point(s_1,s_2):
    print("s_1", s_1,"s_2", s_2)
    if s_1 < s_2:
        if s_1 > 2000:
            return('point de jointure trop haut')
        ajout = map(int,str(s_1))
        s_1 = s_1 + sum(ajout)
        if (s_1 == s_2):
            return s_1
        else:
            return compute_join_point(s_1,s_2)
    else:
        if s_2 > 2000:
            return('point de jointure trop haut')
        ajout = map(int,str(s_2))
        s_2 = s_2 + sum(ajout)
        if (s_1 == s_2):
            return s_1
        else:
            return compute_join_point(s_1,s_2)

def main():
    s_1 = 47
    s_2 = 5
    res = compute_join_point(s_1,s_2)
    print(res)


if __name__ == "__main__":
    main()