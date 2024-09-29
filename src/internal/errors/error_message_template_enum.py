from strenum import StrEnum


class ErrorMessageTemplateEnum(StrEnum):
    """Перечисление шаблонов сообщений об ошибках приложения."""

    NON_STRING_PARAM = "Параметр [{0}] не является строкой"
    EMPTY_STRING_PARAM = "Параметр [{0}] пуст"
    NOT_LIST_ROW = "Строка [{0}] в матрице не является списком"
    MISMATCH_VALUE_TYPE = "Тип данных для значения не соответствует типу [{0}]"
    MISMATCH_LIST_VALUE_TYPE = (
        "Тип данных элемента списка с индексом [{0}] не соответствует типу [{1}]"
    )
    MISMATCH_MATRIX_VALUE_TYPE = (
        "Тип данных элемента с индексом [{0}] в строке матрицы с индексом [{1}] "
        "не соответствует типу [{2}]"
    )
    PARAM_EXISTS = "Элемент входных данных с именем [{0}] уже существует"
    OUTPUT_EXISTS = "Элемент выходных данных с именем [{0}] уже существует"
    ADDING_METHOD_FAILED = "В процессе добавления метода произошла ошибка: [{0}]"
    UNEXPECTED_OUTPUT = (
        "фактический результат [{0}] для элемента "
        "выходных данных [{1}] не соответствует ожидаемому "
        "значению [{2}]"
    )
    TIME_OVER = "Время для выполнения алгоритма ({0} с) истекло. Входные данные: {1}"
    EXECUTION_FAILED = (
        "Во время выполнения алгоритма произошла ошибка: {0}. Входные данные: {1}"
    )
    REDUNDANT_PARAMETER = (
        "Переданный элемент [{0}] отсутствует в структуре входных данных алгоритма"
    )
    MISSED_PARAMETER = "Не указано значение для элемента входных данных [{0}]"
    REDUNDANT_OUTPUT = (
        "Алгоритм вернул элемент [{0}], не указанный в структуре выходных данных"
    )
    MISSED_OUTPUT = "Алгоритм не вернул значение для элемента выходных данных [{0}]"
    ALGORITHM_NOT_EXISTS = "Алгоритм с именем [{0}] не существует"
