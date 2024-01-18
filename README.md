# csv-diff

CSV-Diff is a Python tool that enables you to compare two CSV files and identify the differences between them. The tool generates JSON objects summarizing the changes, making it easy to track modifications, additions, and deletions between the two files.

## Installation

Clone the repository:

```bash
git clone https://github.com/amir-iskander/csv-diff.git
```

Navigate to the project directory:

```
cd csv-diff
```

## Usage/Examples

The script is expecting 2 files to be stored at the same level of the `csv-diff.py` script. To compare two CSV files, run the following command:

```
python3 csv-diff.py
```

The tool will then generate a JSON file (`diff_messages.json`) containing the differences between the two CSV files and will print those JSON messages to the console output.

## Further Development

- Futher development would be needed to provide file names instead of having them statically as `old_data.csv` and `new_data.csv`
- Update the script to add JSON messages in an array instead of just printing them into a file.
