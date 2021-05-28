import utils
# Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.


def main(argv):
    program, *args = argv
    utils.currency_rates(*args)


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
# Честно скатано из методички, надеюсь я правильно поняла этот квест.
