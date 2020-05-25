from time import time
from traceback import print_exc


def compile_test(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            return False
        return True
    return wrapper


def timed_test(repeat=1):
    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                start_time = time()
                for _ in range(repeat):
                    function(*args, **kwargs)
                end_time = time()
            except:
                return -1
            return end_time - start_time
        return wrapper
    return decorator


def error_test(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print_exc()
    return wrapper


def log(target, tab=None, msg=None):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            log_styles = {
                'field'     : '======Test for {:19}======',
                'test'      : '------Test {:2}: {:19}------',
                'warn'      : '------Warn {:2}: {:19}------',
                'log'       : '------Log :{:23}------',
                'report'    : '======Report for {:17}======',
                'result'    : '|{:19}:{:18}|',
                'slimsep'   : '-'*40,
                'doublesep' : '='*40,
            }
            print(log_styles.get(target, '{} {}').format(tab, msg))
            return function(*args, **kwargs)
        return wrapper
    return real_decorator


def print_log(target, tab=None, msg=None):
    log_styles = {
        'field'     : '======Test for {:19}======',
        'test'      : '------Test {:2}: {:19}------',
        'warn'      : '------Warn {:2}: {:19}------',
        'log'       : '------Log :{:23}------',
        'report'    : '======Report for {:17}======',
        'result'    : '|{:19}:{:18}|',
        'slimsep'   : '-'*40,
        'doublesep' : '='*40,
    }
    print(log_styles.get(target, '{} {}').format(tab, msg))


def default_pass(*args, **kwargs):
    pass
