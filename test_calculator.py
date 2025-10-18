import calculator
import pytest


# Параметризованный тест (это уже требует pytest)
@pytest.mark.parametrize("a,b,expected", [(2, 3, 5), (0, 0, 0), (-1, 1, 0)])
def test_add_parameterized(a, b, expected):
    """Что"""
    result = calculator.add(a, b)
    assert result == expected


# Тест на исключения (требует pytest)
def test_divide_by_zero():
    """Что"""
    with pytest.raises(ValueError):
        calculator.divide(10, 0)


@pytest.mark.parametrize("a,b,expected", [(2, 3, -1), (0, 0, 0), (-1, 1, -2)])
def test_subtract(a, b, expected):
    """Что"""
    result = calculator.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize("a,b,expected", [(2, 3, 6), (0, 0, 0), (-1, 1, -1)])
def test_multiply(a, b, expected):
    """Что"""
    result = calculator.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a,b,expected", [(6, 3, 2), (1, 1, 1), (-1, 1, -1)])
def test_divide(a, b, expected):
    """Что"""
    result = calculator.divide(a, b)
    assert result == expected


@pytest.mark.parametrize("a,b,expected", [(6, 1, 6), (1, 1, 1), (-1, 1, -1)])
def test_power(a, b, expected):
    """Что"""
    result = calculator.power(a, b)
    assert result == expected


@pytest.mark.parametrize("a,expected", [(8, True)])
def test_is_even(a, expected):
    """Что"""
    result = calculator.is_even(a)
    assert result == expected


@pytest.mark.parametrize("a,expected", [(2, 2)])
def test_factorial(a, expected):
    """Что"""
    result = calculator.factorial(a)
    assert result == expected


def main():
    pytest.main([__file__, "-v"])


if __name__ == "__main__":
    main()
