from utils.settings import settings


def log(func):
    """
    Using @log wrapper allows you to log data whenever a function is called.
    :param func: The decorated function.
    :return: The return value of the func that's passed in as a parameter.
    """

    def get_log_kwargs(**kwargs):
        return (kwargs.pop("log_divider", settings['log']['DEF_DIVIDER']),
                kwargs.pop("log_before_call", ""),
                kwargs.pop("log_after_call", ""),
                kwargs)

    def wrapper(*args, **kwargs):

        log_divider, log_before_call, log_after_call, kwargs = get_log_kwargs(**kwargs)

        if settings["log"]["CLEAN_CONSOLE"]:
            return func(*args, **kwargs)

        print(log_divider)
        print(log_before_call)
        val = func(*args, **kwargs)
        print(log_after_call)
        return val

    return wrapper
