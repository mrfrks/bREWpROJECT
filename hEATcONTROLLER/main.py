
def print_me(fam):
    with open('input.txt', 'a') as f:
        f.truncate(0)
        for height in fam:
            f.write('%lf,\n' % height)

if __name__ == '__main__':
    fam = [1.73, 1.68, 1.71, 1.89]
    print_me(fam)
