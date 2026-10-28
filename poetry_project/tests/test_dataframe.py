import pandas as pd
from plt_temp import process_temperature_data

def test_process_temperature_data():
    hours = ["2023-10-28T12:00:00", "2023-10-28T10:00:00"]
    temps = [15.5, 12.0]

    df = process_temperature_data(hours, temps)

    assert list(df.columns) == ["time", "temperature_c"], "Неверные названия столбцов"

    assert len(df) == 2, "Неверное количество строк"

    assert str(df.iloc[0]["time"]) == "2023-10-28 10:00:00", "Данные не отсортированы по времени"
    assert df.iloc[0]["temperature_c"] == 12.0, "Температура не соответствует времени после сортировки"
    
    assert str(df.iloc[1]["time"]) == "2023-10-28 12:00:00"
    assert df.iloc[1]["temperature_c"] == 15.5