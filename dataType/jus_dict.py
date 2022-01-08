import pytest

def test_dict():
    stock = {
        'name' : 'Samsung', 
        'code' : '005930', 
        'price' : 70000,
    }

    assert isinstance(stock, dict)

    # You may access set elements by keys.
    assert stock['name'] == 'Samsung'
    assert stock['code'] == '005930'
    assert stock['price'] == 70000

    assert list(stock) == ['name', 'code', 'price']

    stock['price'] = 80000
    assert stock['price'] == 80000

    stock['end_price'] = 78000
    assert list(stock) == ['name', 'code', 'price', 'end_price']

    del stock['end_price']
    assert list(stock) == ['name', 'code', 'price']

if __name__ == "__main__":
    test_dict()
