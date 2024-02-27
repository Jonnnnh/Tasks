from calendar import monthrange, weekday
import numpy as np

def generate_calendar(month, year):
    num_days = monthrange(year, month)[1]
    first_day_of_month = weekday(year, month, 1)

    days = list(range(1, num_days + 1))

    # корректировка начала месяца
    if first_day_of_month != 0:
        prev_month_days = monthrange(year, month - 1)[1] - first_day_of_month + 1
        days = list(range(prev_month_days, monthrange(year, month - 1)[1] + 1)) + days

    # корректировка конца месяца
    next_month_fill = 7 - len(days) % 7
    if next_month_fill != 7:
        days += list(range(1, next_month_fill + 1))

    calendar_array = np.array(days).reshape(-1, 7)

    # формирование имени выходного файла
    output_filename = f"calendar_{year}_{month}.txt"

    with open(output_filename, 'w') as f:
        for week in calendar_array:
            week_str = ' '.join(map(str, week))
            f.write(week_str + '\n')

    print(f"Календарь на {month}/{year} записан в файл: {output_filename}")

month = 8
year = 1998
generate_calendar(month, year)
