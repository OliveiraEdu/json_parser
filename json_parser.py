import pandas as pd
import json

def json_to_dataframe(json_file):
  """Converts a JSON file to a Pandas DataFrame and presents it as a table.

  Args:
    json_file: The path to the JSON file.

  Returns:
    A Pandas DataFrame containing the JSON data.
  """

  # Open the JSON file
  with open(json_file, "r") as f:
    json_data = json.load(f)

  # Convert the JSON data to a Pandas DataFrame
  df = pd.DataFrame(json_data)

  # Present the DataFrame as a table
  print(df.to_string())

  return df
