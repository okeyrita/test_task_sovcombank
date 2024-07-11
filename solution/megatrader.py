from collections.abc import Iterator
from itertools import combinations
from typing import List


class Lot:
    '''
    Класс хранения лота с рынка, имеющий такие аттрибуты:
    day - день выставление лота на рынок
    bond_name - название облигации
    price - цена облигации
    count - количество облигаций
    lot_sum - суммарная цена лота
    final_profit - итоговая прибыль с данного лота
    '''

    def __init__(self, day: str, bond_name: str, price: str, count: str):
        self.day = int(day)
        self.bond_name = bond_name
        self.price = float(price)
        self.count = int(count)
        self.lot_sum = self.price * self.count * 10
        self.final_profit = None

    def get_final_profit(self, predicated_n_days: int) -> float:
        '''
        Вычисление финальной прибыли с данного лота высчитывается по формуле
        чистая прибыль = количество облигаций * (30 дней + N - день предложения)
        погашение стоимости акции = стоимость покупки лота -
        количество лотов * 1000 у.е.
        доход = чистая прибыль - погашение стоимости акции
        :param predicated_n_days: количество дней предложений N
        :return : финальная прибыль данного лота
        '''
        # прибыль на N+30 день - чистая прибыль
        pure_profit = self.count * (30 + predicated_n_days - self.day)
        # погашениe акции
        bond_redemption = self.lot_sum - 1000 * self.count
        return pure_profit - bond_redemption


def read_input() -> tuple[int, List[Lot]]:
    '''
    Считывание входных данных.
    Первая строка строка содержит 3 числа N, M и S - ближайшие N дней,
    максимально возможное количество лотов M в день, сумма денежных средств
    трейдера S.
    Следущие строки имеют формат:
    <день> <название облигации в виде строки без пробелов> <цена> <количество>
    Последняя строка ввода пустая.
    :return : средства трейдера, лист лотов
    '''
    predicated_n_days, lots_num_day, traders_funds = map(int, input().split())
    lots = []
    while True:
        input_row = input()
        if input_row == '':
            break
        current_lot = Lot(*input_row.split())
        final_profit = current_lot.get_final_profit(predicated_n_days)
        # отфильтровать лоты, не использовать лоты с отрицательной финальной
        # прибылью лота.
        if current_lot.lot_sum <= traders_funds and final_profit > 0:
            current_lot.final_profit = final_profit
            lots.append(current_lot)
    return traders_funds, lots


def get_all_accepted_combinations(
    traders_funds: int, lots: List[Lot]
) -> Iterator[tuple[int, ...]]:
    '''
    Получить все возможные уникальные комбинации лотов в формате генератора,
    чья сумма покупки <= сумме денежных средств трейдера. 
    :param traders_funds: сумма денежных средств трейдера
    :param lots: предложенные лоты
    :return : итератор по возможным комбинациям лотов
    '''
    lots_len = len(lots)
    for len_combination in range(1, lots_len + 1):
        for combination in combinations(range(len(lots)), len_combination):
            purchase_amount = 0
            for lot_id in combination:
                purchase_amount += lots[lot_id].lot_sum
                if purchase_amount > traders_funds:
                    break
            if purchase_amount > traders_funds:
                continue
            else:
                yield combination
    return


def get_full_profit_and_lot_sum(
    lots_id_tuple: tuple[int, ...], lots: List[Lot]
) -> tuple[float, float]:
    '''
    Получение общей суммы дохода данной комбинации лотов и суммы закупки данных
    лотов.
    :param lots_id_tuple: кортеж id позиций лотов в изначальном листе
    предложенных лотов
    :param lots: лист предложенных лотов
    :return : <общая сумма дохода>, <сумма закупки лотов>
    '''
    full_profit = 0
    full_lot_sum = 0
    for lot_id in lots_id_tuple:
        full_profit += lots[lot_id].final_profit
        full_lot_sum += lots[lot_id].lot_sum
    return full_profit, full_lot_sum


def get_best_lots_combination(
    accepted_lots_id_comb: Iterator[tuple[int, ...]], lots: List[Lot]
) -> tuple[int, tuple[int, ...]]:
    '''
    Получение наибольшей суммы прибыли и комбинации лотов с самой большой
    суммарной прибылью.
    :param accepted_lots_id_comb: итератор комбинаций id лотов
    :param lots: лист предложенных лотов
    :return : <общая максимальная сумма дохода>, <кортеж id лотов>
    '''
    max_final_profit = 0
    min_lot_sum = 0
    result_lots = []
    for combination in accepted_lots_id_comb:
        current_profit_sum, full_lot_sum = get_full_profit_and_lot_sum(
            combination, lots
        )
        if current_profit_sum > max_final_profit or (
                current_profit_sum == max_final_profit and
                full_lot_sum < min_lot_sum):
            max_final_profit = current_profit_sum
            min_lot_sum = min_lot_sum
            result_lots = combination
    return max_final_profit, result_lots


def pretty_print_result(
    full_profit: float, result_lots_ids: tuple[int, ...], lots: List[Lot]
) -> None:
    '''
    :param full_profit: общая максимальная сумма дохода
    :param result_lots_ids: кортеж id лотов
    :param lots: лист предложенных лотов
    Вывод результата подсчета в формате:
    <доход>
    <день> <название облигации в виде строки без пробелов> <цена> <количество>
    ...
    <пустая строка>
    '''
    print(full_profit)
    for lot_id in result_lots_ids:
        print(
            f'{lots[lot_id].day} {lots[lot_id].bond_name} '
            f'{lots[lot_id].price} {lots[lot_id].count}'
        )
    print('')


def main():
    traders_funds, all_lots = read_input()
    accepted_lot_combinations = get_all_accepted_combinations(
        traders_funds, all_lots
    )
    full_profit, result_lots = get_best_lots_combination(
        accepted_lot_combinations, all_lots
    )
    pretty_print_result(full_profit, result_lots, all_lots)


if __name__ == '__main__':
    main()
