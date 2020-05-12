from typing import Generator, Union, _T, List, Any, Optional


def chunks(data: Optional[list], size: int = 2) -> Generator[Union[list, _T, List[_T]], Any, None]:
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


if __name__ == '__main__':
    chunks('abc', 'abc')
