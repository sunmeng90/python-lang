from typing import Optional, Generator


def chunks(data: Optional[list], size: int = 2) -> Generator:
    """
    split data into chunk of size
    :param data: list
    :param size: size of chunk, default 2
    :return:

    Usage:

    >>> from utils import collections
    >>> data = [1,2,3,4,5]
    >>> result = list(chunks(data, 2))
    >>> result == [[1,2],[3,4],[5]]
    True
    """
    if data is None:
        data = []
    for i in range(0, len(data), size):
        yield data[i:i + size]


if __name__ == '__main__':
    chunks('abc', 'abc')
