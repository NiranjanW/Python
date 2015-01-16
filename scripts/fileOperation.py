import sys
import sum
#generators

def read_forever(fobj):
    counter =0
    while True:
        line = fileobj.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def filter_comments(lines):
    for line in lines:
        if not line.strip().startswith('#'):
            yield line

def get_number():
    for line in lines:
        yield int(line.split()[-1])
#generator pull

def show_sum(file_name='out.txt'):
    lines = read_foreever(open(file_name))
    filtered_lines = filter_comments(lines)
    numbers = get_number(filtered_lines)
    sum =0

    try:
        for number in numbers:
            sum += number
            sys.stdout.write('sum %d\r' + %sum)
            sys.stdout.flush()
    except KeyBoardInterrupt:
        print 'sum' , sum

def init_coroutine(func):
    functools.wrap(func)
    def init (*args, **kwargs):
        gen = func(*args, *kwargs)
        next(gen)
        return gen
    return init


