def chunks(data=None, size=2):
    """
    split data into chunk of size
    :param data: list
    :param size: size of chunk, default 2
    :return:
    """
    if data is None:
        data = []
    for i in range(0, len(data), size):
        yield data[i:i + size]
