from random import randint

names = ['יואב', 'טליה', 'יעל', 'גלעד']
gots = ['קיבל', 'קיבלה', 'קיבלה', 'קיבל']


def compare(i, j):
    d = i - j
    if d == 0:
        return 'אותה כמות של סוכריות כמו'

    rel = 'יותר' if d > 0 else 'פחות'
    d = abs(d)

    if d == 1:
        return f'סוכריה אחת {rel} מאשר'

    return f'{d} סוכריות {rel} מאשר'


def eq(*nums):
    n = len(nums)
    s = ', '.join(names[:n-1])
    s += f' ו{names[n-1]} קיבלו {sum(nums)} סוכריות. '
    tos = [randint(0, i - 1) for i in range(1, n)]
    s += ', '.join([
        f'{names[i]} {gots[i]} {compare(nums[i], nums[tos[i-1]])} {names[tos[i-1]]}'
        for i in range(1, n)
    ])
    s += '. כמה סוכריות כל אחד קיבל?'
    return s


if __name__ == "__main__":
    qs = [[randint(1, 20) for _ in range(4)] for _ in range(4)]

    with open('q.tex', 'w') as f:
        print('''
        \\documentclass[12pt]{article}
        \\usepackage[margin=2.5cm, top=2cm, bottom=1.5cm]{geometry}
        \\usepackage{polyglossia,enumitem}
        \\newfontfamily\\hebrewfont[Script=Hebrew]{Hadasim CLM Regular}
        \\setmainlanguage{hebrew}
        \\let\\hebrewfonttt\\ttfamily
        \\setlist[itemize,1]{label={\\fontfamily{cmr}\\fontencoding{T1}\\selectfont\\textbullet}}        
        \\begin{document}
        ''', file=f)

        print('\\begin{enumerate}', file=f)
        print('\\itemsep4cm', file=f)
        for i, nums in enumerate(qs):
            print('\\item', eq(*nums), file=f)
        print('\\end{enumerate}', file=f)

        print('\\end{document}', file=f)
