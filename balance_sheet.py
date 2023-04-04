import pandas as pd

def generate_balance_sheet(filename):
    # Загрузка данных из Excel-файла
    data = pd.read_excel(filename)

    # Вычисление общей стоимости активов
    total_assets = data['Assets'].sum()

    # Вычисление общей суммы обязательств
    total_liabilities = data['Liabilities'].sum()

    # Вычисление собственного капитала
    equity = total_assets - total_liabilities

    # Вывод балансового отчета
    print(f"Assets: {total_assets}")
    print(f"Liabilities: {total_liabilities}")
    print(f"Equity: {equity}")
        
# Пример использования функции
generate_balance_sheet('financial_data.xlsx')
