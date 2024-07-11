from typing import Tuple, List


def read_shares() -> Tuple[int, List[float]]:
    '''
    Считывание входных данных в формате:
    первая строка: количество долей
    все последующие: числовое выражение доли
    :return : <количество долей>, <лист выражений долей>
    '''
    number_of_shares = int(input())
    # read shares
    sum_of_shares = 0
    shares = []
    for share_row in range(0, number_of_shares):
        current_share = float(input())
        sum_of_shares += current_share
        shares.append(current_share)
    return sum_of_shares, shares


def print_percents_in_right_format(raw_share: float) -> None:
    '''
    Вывод процентного выражения доли строго с 3мя знаками после запятой.
    :param : процентная доля
    '''
    cut_share = round(raw_share, 3)
    str_share = str(cut_share)
    right_percent_string = str_share + '0'*(5-len(str_share))
    print(right_percent_string)


def main():
    sum_of_shares, shares = read_shares()
    share_percents = [share/sum_of_shares for share in shares]
    for percent in share_percents:
        print_percents_in_right_format(percent)


if __name__ == '__main__':
    main()
