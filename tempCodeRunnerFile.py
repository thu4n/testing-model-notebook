import pandas as pd

def fill_blank_cells_in_csv(csv_file_path, column_name, value_to_fill):
  """Fills any blank cell in the specified column of the specified CSV file with the specified value.

  Args:
    csv_file_path: The path to the CSV file.
    column_name: The name of the column to fill.
    value_to_fill: The value to fill the blank cells with.
  """

  # Load the CSV file into a Pandas DataFrame.
  df = pd.read_csv(csv_file_path)

  # Select the specific column to fill.
  column = df[column_name]

  # Fill the blank cells in the selected column with the specified value.
  column.fillna(value_to_fill, inplace=True)

  # Save the updated DataFrame to a new CSV file.
  df.to_csv(csv_file_path + '.updated.csv', index=False)


if __name__ == '__main__':
  # The path to the CSV file.
  csv_file_path = 'tch-pca-2.csv'

  # The name of the column to fill.
  column_name = 'Label'

  # The value to fill the blank cells with.
  value_to_fill = 'NA'

  # Fill the blank cells in the CSV file.
  fill_blank_cells_in_csv(csv_file_path, column_name, value_to_fill)

  # Print a message to the user.
  print('The CSV file has been updated.')