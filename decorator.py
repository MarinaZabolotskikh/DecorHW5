from datetime import datetime

def decorator(old_func):
    def write_info(*args, **kwargs):
        dt_now = datetime.now()
        name_func = old_func.__name__
        result = old_func(*args, **kwargs)
        with open("info.txt", "a", encoding="utf-8") as f:
            f.write(f'Дата и время: {dt_now}\n'
                    f'Имя функции: {name_func}\n'
                    f'Аргументы функции: {args}, {kwargs}\n'
                    f'Результат функции: {result}\n')
        return result
    return write_info

@decorator
def summ(a, b):
    result = a + b
    return result

if __name__ == '__main__':
    summ(2, 6)