
import csv

def get_csv_data(csv_path):
    """
    从csv文件中读取数据 将数据以列表的形式返回

    @type csv_path:string
    @param csv_path: csv file path
    @return list
    """
    rows = []
    csv_data = open(csv_path)
    content = csv.reader(csv_data)
    next(content,None)

    for row in content:
        rows.append(row)
    
    return rows
