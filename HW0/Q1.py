# -*- coding: utf-8 -*-
def main():
    with open('./words.txt') as f:
        content = f.read()
        content = content.rstrip()
    words = content.split(' ')

    counter = {}
    for word in words:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1

    with open('./Q1.txt', 'w') as f:
        is_first_line = True
        for (index, (word, count)) in enumerate(counter.items()):
            f.write(f'{word} {index} {count}')
            if is_first_line:
                is_first_line = False
            else:
                f.write('\n')


if __name__ == '__main__':
    main()
