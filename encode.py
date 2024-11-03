import xml.etree.ElementTree as ET

def parse_currency(xml_file):
    """Парсит XML и извлекает данные Name - Value"""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        currency_dict = {}

        for currency in root.findall('.//Valute'):
            name_elem = currency.find('Name')
            value_elem = currency.find('Value')

            if name_elem is not None and value_elem is not None:
                name = name_elem.text
                value = value_elem.text.replace(',', '.')
                currency_dict[name] = float(value)
            else:
                print("Элемент Name или Value не найден в одном из блоков Valute")

        return currency_dict

    except ET.ParseError as e:
        print(f"Ошибка парсинга XML: {e}")

# Пример вызова
currency_data = parse_currency('currency.xml')
if currency_data:
    print("Словарь Name - Value:")
    print(currency_data)
else:
    print("Данные не были извлечены.")