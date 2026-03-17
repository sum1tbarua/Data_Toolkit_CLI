class DatasetToolkit:
    def __init__(self, data):
        self.data = data

    def row_count(self) -> int:
        return len(self.data)

    def columns(self) -> list:
        if self.data is None:
            return []
        return list(self.data[0].keys())

    def head(self, n) -> list:
        return self.data[:n]

    def unique_values(self, column) -> list:
        unique_column_set = set()
        for item in self.data:
            unique_column_set.add(item[column])
        return sorted(unique_column_set)

    def filter_rows(self, column, value) -> list:
        return [row for row in self.data if row[column] == value]

    def sort_rows(self, column, reverse=False) -> list:
        return sorted(self.data, key=lambda x: x[column], reverse=reverse)

    def top_n(self, column, n):
        return sorted(self.data, key=lambda item: item[column], reverse=True)

    def summary(self) -> dict:
        summary_dict = dict()
        for column in self.columns():
            values = {row[column] for row in self.data}
            summary_dict[column] = {
                'unique_values': len(values)
            }
        return summary_dict
        