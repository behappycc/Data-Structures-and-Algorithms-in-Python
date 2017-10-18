def min_edit_distance(s1, s2):
    len1 = len(s1)
    len2 = len(s2)

    m = [None] * (len1 + 1)
    for i in range(len1 + 1):
        m[i] = [0] * (len2+1)

    for i in range(1, len1+1):
        m[i][0] = i
    for j in range(1, len2+1):
        m[0][j] = j

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if s1[i-1] == s2[j-1]:
                cost = 0
            else:
                cost = 1
            replace_cost = m[i-1][j-1] + cost
            remove_cost = m[i-1][j] + 1
            insert_cost = m[i][j-1] + 1
            m[i][j] = min(replace_cost, remove_cost, insert_cost)

    print (m[len1][len2])
    print (m)
    return m[len1][len2]


def main():
    min_edit_distance('GCTAC', 'CTCA')

if __name__ == '__main__':
    main()