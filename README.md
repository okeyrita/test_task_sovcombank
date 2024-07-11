## Тестовое задание на позицию Python разработчика в Совкомбанк.

* Тестовое задание включает 2 задачи. Полное описание тестового задания находится в файле __tasks_software_engineer.pdf__
* Решение задач находится в папке __solution__
* Тестовые данные и код для их генерации содержится в папке test_inputs
* Файлы вызова алгоритмов на тестовых данных с подсчетом времени лежат в корне `time_estimation_megatrader.py` и `time_estimation_share_building.py`


__Содержание__:
- [Тестовое задание на позицию Python разработчика в Совкомбанк.](#тестовое-задание-на-позицию-python-разработчика-в-совкомбанк)
- [Долевое строительство ](#долевое-строительство-)
  - [Описание алгоритма ](#описание-алгоритма-)
  - [Корректность алгоритма ](#корректность-алгоритма-)
  - [Вычислительная сложность алгоритма ](#вычислительная-сложность-алгоритма-)
  - [Ограничения на размер входных параметров ](#ограничения-на-размер-входных-параметров-)
  - [Cубъективная оценка сложности задачи ](#cубъективная-оценка-сложности-задачи-)
- [Мегатрейдер ](#мегатрейдер-)
  - [Описание алгоритма ](#описание-алгоритма--1)
  - [Корректность алгоритма ](#корректность-алгоритма--1)
  - [Вычислительная сложность алгоритма ](#вычислительная-сложность-алгоритма--1)
  - [Ограничения на размер входных параметров ](#ограничения-на-размер-входных-параметров--1)
  - [Cубъективная оценка сложности задачи ](#cубъективная-оценка-сложности-задачи--1)

## Долевое строительство <a name="paragraph1"></a>

### Описание алгоритма <a name="paragraph11"></a>

Изначальная задача делится на несколько частей:
* Считывание данных
    В момент считывания данных мы кладем количество долей в одну переменную, и далее проходим циклом длиной в количество долей и считываем наши доли в лист долей. В момент считывания долей мы их также суммируем и кладем ответ в отдельную переменную общего количества долей.
* Обработка + вывод данных
    Алгоритм достаточно простой, поэтому обработку и вывод данных можно произвести в одном цикле.
    Мы проходим циклом по каждой доле и вычисляем ее долю от общего количества долей. При выводе нам необходимо округлить __строго__ до трех знаков после запятой. Нам не сообщается, как именно мы должны округлять, поэтому берется классический метод в питоне `round(n, m)`.
    В случае, когда в нашем числе до или после округления было меньше 3х знаков после запятой - мы добавляем нули в выводе числа. Делается это таким образом: нам известно, что у нас доли , поэтому наше число имеет формат __X.XXX__, целая часть числа может быть равна 0 или 1(при условии, что у нас всего одна доля). Далее идет точка, разделяющая целую и дробную часть числа. После идут три знака дробной части. В сумме длина строки числа имеют длину 5 = 1 символ целой части + 1 разделяющий символ + 3 символа после запятой. Соответственно, для корректного вывода числа мы можем привести его к строке, вычислить его длину методом `len()` и добавить в конце количество нулей, равное 5 - len(число).

### Корректность алгоритма <a name="paragraph12"></a>

Докажем корректность алгоритма с помощью математической индукции.

Рассмотрим случай , когда доля одна. Код вернет ответ 1.000 , так как при разделении целого на 1 мы получим 100% , что равняется 1.000.
Рассмотрим случай, когда долей x. Общая стоимость целого равна сумме стоимости долей, и каждая доля равняется `стоимость доли/стоимость целого`
n - количеcтво долей
```math
<доля_x> = {a_x \over a_1+ a_2 + a_3 ...+a_n}
```
Сумма всех долей должна равняться исходному целому, то есть
```math
1 = <доля_1> + <доля_2> + ... + <доля_n> = {a_1 \over a_1+ a_2 + a_3 ...+ a_n} + {a_2 \over a_1+ a_2 + a_3 ...+ a_n} + ... = {a_1+ a_2 + a_3 ...+ a_n \over a_1+ a_2 + a_3 ...+ a_n} = 1
```

По мат. индукции количества долей n + 1 = m

```math
<доля_x> = {a_x \over a_1+ a_2 + a_3 ...+a_m}
```
Сумма всех долей должна равняться исходному целому, то есть
```math
1 = <доля_1> + <доля_2> + ...+ <доля_n> + <доля_m> = {a_1 \over a_1+ a_2 + a_3 ...+ a_n + a_m} + {a_2 \over a_1+ a_2 + a_3 ...+ a_n + a_m} + ... = {a_1+ a_2 + a_3 ...+ a_n + a_m \over a_1+ a_2 + a_3 ...+ a_n + a_m} = 1
```
Корректность доказана.

### Вычислительная сложность алгоритма <a name="paragraph13"></a>

Разберем сложность алгоритма в О нотации.

* По времени:

Алгоритм состоит из двух последовательных циклов по количеству долей __n__. Считывание данных O(n) и Вывод данных O(n).

```math
O(n + n)  -> O(n)
```

* По памяти:

В Алгоритме записывается в память переменная - количество долей O(1) и лист долей O(n)

```math
O(1 + n)  -> O(n)
```

### Ограничения на размер входных параметров <a name="paragraph14"></a>

В данном случае ограничение на размер входных данных может быть как по времени выполнения алгоритма, так и по условию в 3 знака после запятой.
* Эмпирически вычислено, что код достигает достаточно долгого времени работы (5 сек) при размере входных данных около 2000000 долей.
* При относительно равномерном распределении долей ограничение на работу возникает при количестве долей более 1000, так как мы вычисляем точность доли до тысячной (до третьего знака после запятой). При относительно равномерном распределении получается, что значение уходит за пределы точности доли
```math
доля = {1\over >1000} = <0.001
```

Запуск кода с тестами (из корня репозитория):
```bash
python3 solution/share_building.py < test_inputs/share_building_big_input.txt
python3 solution/share_building.py < test_inputs/share_building_default_input.txt
```

Запуск кода для подсчета времени работы:
```bash
python3  time_estimation_share_building.py
```

### Cубъективная оценка сложности задачи <a name="paragraph15"></a>

Я оцениваю задачу на 1 из 10, так как в данной задаче нет сложной обработки и построения структур данных, здесь необходимо обработать входные данных исходя из простейших математических формул. Затраченное время - на написание и тестирование алгоритма ушло ~ 10 мин. Далее было потрачено время на доказательство, корректность, сложность и ограничения.


## Мегатрейдер <a name="paragraph2"></a>

### Описание алгоритма <a name="paragraph21"></a>

Изначальная задача делится на несколько частей:
* Считывание данных (read_input)
* Обработка (get_all_accepted_combinations, get_best_lots_combination)
* Вывод данных (pretty_print_result)

Основной каркас алгоритма работает по данной цепочке:
```
read_input -> get_all_accepted_combinations -> get_best_lots_combination -> pretty_print_result
```

1. Метод __read_input__. Алгоритм начинается со считывания данных. В данном методе мы в первой строке считываем переменные N, M и S, где N - в ближайшие N дней, M - предельное количество лотов в день, S - денежные средства, которыми располагает трейдер.
Далее у нас может быть __не более__ N*M строк, содержащих лоты. В конце идет пустая строка.
Строки с лотами имеют формат: "<день> <название облигации в виде строки без пробелов> <цена> <количество >"
При считывании лотов мы сразу может отфильтровать и не учитывать лоты, которые имеют отрицательный финальный доход, который мы можем рассчитать формуле:
```
<Финальный доход лота> = <чистая прибыль> - <погашениe акции> , где 
<чистая прибыль> = <количество облигаций лота> * (30 + <количество дней, на которые известные предложения N> - <день предложения>)
<погашениe акции> = 10 * <цена облигации> * <количество облигаций лота> - 1000 * <количество облигаций лота>
```
Если финальный доход лота равен 0 или меньше 0, то нам нет смысла рассматривать этот лот и учитывать его дальше. В список возможных лотов такой лот записываться не будет.

2. Метод __get_all_accepted_combinations__. Одно из возможных решений - это перебор всех возможных комбинаций лотов. Для набора вообще всех возможных комбинаций длины от 1 до длины количества лотов проходим по циклу for len_combination от 1 до количества лотов. Внутри цикл по уникальным комбинациям лотов длины len_combination. для данного циклы используется метод `combinations` стандартной python библиотеки itertools. Данный метод имеет сложность O(n!), где n - длина списка лотов. Внутри цикла мы проходим по лотам в данной комбинации лотов и подсчитываем сумму закупки этих лотов. Если сумма превышает сумму денежных средств трейдера, то мы не включаем эту комбинацию в список возможных комбинаций лотов, подходящих для покупки.
В данном месте при прохождении цикла по `combinations` мы используем итератор, а не готовый лист, что позволяет экономить на памяти, храня в памяти только одну комбинацию лотов за раз. Здесь мы сразу же отсеиваем варианты, где суммарная стоимость лотов больше денежной суммы трейдера.

3. Метод __get_best_lots_combination__. Проходим по комбинациям лотов из get_all_accepted_combinations и выбираем наилучшее решение, где сумма дохода со всех лотов будет максимальной. Если сумма доходов для разных комбинаций равна, но у первой закупочная стоимость ниже, то мы выберем первую из соображений логики (данного условия не озвучивалось в задаче.) Если сумма доходов для разных комбинаций равна закупочная стоимость равна, то мы выберем первую комбинацию, исходя из упрощения логики алгоритма в данном месте. Возвращаем лучшую комбинацию лотов и доход с данных лотов.

4. Метод __pretty_print_result__. Мы выбрали лучшую комбинацию в предыдущем методе и посчитали доход. В первой строке выводим доход. В следующих строках выводим лоты для покупки в формате:
"<день> <название облигации в виде строки без пробелов> <цена> <количество >"
Возвращаем последнюю пустую строку.

### Корректность алгоритма <a name="paragraph22"></a>

Для данной задачи не подойдет подход доказательства с помощью математической индукции, как в первой задаче.

Данная задача имеет комплексное решение из нескольких последовательных блоков, поэтому логично было бы разобрать корректность каждой части кода. 

На статическом анализе кода с помощью тестовых данных мы видим, что код возвращает ожидаемый результат из примера в условии задачи.

Разберем текущий пример из задачи на нашем коде.

Входные данные:
```
2 2 8000
1 alfa-05 100.2 2
2 alfa-05 101.5 5
2 gazprom-17 100.0 2

```

Работа метода __read_input__ подсчитывает, что  доход первого лота равен 58.0, доход второго лота равен 75.0, доход третьего лота равен 60.0. Все три лота имеют неотрицательный доход и будут добавлены в лист возможных лотов. __read_input__ возвращает все три лота. -- Корректно

Метод __get_all_accepted_combinations__ собирает все возможные комбинации лотов с суммой закупки не более суммы денежных средств трейдера. Если мы пронумеруем наши лоты как 1, 2, 3 , то метод вернет итератор по следующим комбинациям:
```
[1], [2], [3], [1,2], [1,3], [2,3]
```
Комбинацию `[1,2,3]` метод не вернет, так как ее стоимость превышает сумму денежных средств трейдера. -- корректно

Метод __get_best_lots_combination__ выбирает наилучшую комбинацию лотов. Для комбинаций из прошлого метода доход и стоимость лотов будут такими:
```
комбинация лотов, суммарный доход, суммарная стоимость
[1], 58.0, 2004.0
[2], 75.0, 5075.0
[3], 60.0, 2000.0
[1,2], 133.0, 7079.0
[1,3], 118.0, 4004.0
[2,3], 135.0, 7075.0
```
Наибольший доход 135.0 у комбинации [2,3]. Метод вернул его. -- корректно

Метод __pretty_print_result__ вывел доход 135.0 и комбинацию 2го и 3го лота + пустая последняя строка. -- корректно

```
135.0
2 alfa-05 101.5 5
2 gazprom-17 100.0 2

```

Данный подход разобрал локлаьнф
ый пример, но не доказал корректность кода на любых данных, на локальном примере задача является корректной исходя и разобранного примера, приведенного выше.

### Вычислительная сложность алгоритма <a name="paragraph23"></a>

Основной каркас алгоритма работает по данной цепочке:
```
read_input -> get_all_accepted_combinations -> get_best_lots_combination -> pretty_print_result
```
* Метод __read_input__ имеет сложность по времени O(n), где n - общее количество лотов, сложность по памяти равна O(n).
* Метод __get_all_accepted_combinations__ имеет сложность по времени O(n*n!*n), что равно O(n!). Сложность по памяти равно O(n), так как на выходе мы получаем итератор комбинации лотов. Для снижения затрат на память используется итератор combinations , чтобы в хранить в памяти полный список всех возможных комбинаций. Также для снижения затрат на память в листах возможных комбинаций лотов используются не сами лоты, которые хранят комплексную информацию, а id лотов во входном листе лотов. Сам метод также возвращает итератор, чтобы не хранить в памяти все комбинации лотов.
* Метод __get_best_lots_combination__ имеет сложность по времени O(n!) так в нем мы перебираем все комбинации из итератора get_all_accepted_combinations. Сложность по памяти равна O(n), так как мы храним и возвращаем только итоговую лучшую комбинацию лотов , которая имеет длину не более n.
* Метод __pretty_print_result__ имеет сложность по времени O(n) так как мы единожды проходим по итоговому листу лотов. Сложность по памяти равна O(1) так как в данном методы мы ничего не храним.

Итого:

* По времени:

```math
O(n + n! + n! + n)  -> O(n!)
```

* По памяти:

```math
O(n + n + n + 1)  -> O(n)
```

### Ограничения на размер входных параметров <a name="paragraph24"></a>

Одним из факторов ограничения по времени является] количество лотов представленных трейдеру, для работы со скоростью не более ~ 5 сек предельное количество представленных лотов ~ 40, при учете, что большая часть лотов имеет положительный доход и будет включена в дальнейшую обработку алгоритма.

Еще одним фактором можно считать сумму денежных средств трейдера относительно стоимости лотов. При возрастании суммы денежных средств падает скорость обработки, так как возрастает количество возможных подходящих комбинаций лотов для закупки. Аналогично стоимость лотов может отсекать часть лотов и увеличивать скорость алгоритма.

Запуск кода с тестами (из корня репозитория):
```bash
python3 solution/megatrader.py < test_inputs/megatrader_big_input.txt
python3 solution/megatrader.py < test_inputs/megatrader_default_input.txt
```

Запуск кода для подсчета времени работы:
```bash
python3  time_estimation_megatrader.py
```

### Cубъективная оценка сложности задачи <a name="paragraph25"></a>

Я оцениваю задачу на 6 из 10. Данная задача имеет не самое очевидное описание и возможно избыточные отвлекающие условия. Cубъективная сложность 6/10 , так как у задачи есть очевидное решение с помощью "грубой силы", что позволяет решить задачу быстро, хоть и не оптимально. Потенциально задача имеет более элегантное и оптимальное решение.
Затраченное время на разработку алгоритма и написание кода ~ 3-4 часа.
