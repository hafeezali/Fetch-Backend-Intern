# README: Fetch Coding Exercise - Software Engineering Internship


## Points Spending Script

The points.py script reads a CSV file containing transactions with payer, points, and timestamp data and uses it to spend a specified number of points by spending points from the oldest transactions first while ensuring no payer's balance goes negative. 

The script prints the final payer point balances as a dictionary.


## Requirements & Installations

### 1. Python 3.x and Pip

- For MacOS ([Installation Steps](https://docs.python-guide.org/starting/install3/osx/))
    - Install Homebrew:
    ``` /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```
    - Set path variable for python by adding this in ~/.profile by using your favourite editor: 
    ```export PATH="/usr/local/opt/python/libexec/bin:$PATH"```
    - Install python using brew:
    ```brew install python ```
- For Windows ([Installation Steps](https://www.tomshardware.com/how-to/install-python-on-windows-10-and-11))
    - Download the official python installer from [python.org](https://www.python.org/)
    - Run the installer and make sure to add Python to PATH
    - After the installation is successful, make sure to disable path length limit

### 2. Install Pandas

- Run this from the terminal:
```
pip install pandas
```


## Usage

The script can be run from the command line with the following arguments:

```
python3 points.py -tf <filename> -ps <points_to_spend>
```

- `filename`: the path to the CSV file containing transactions.
- `points_to_spend`: the number of points to spend

Example usage:
```
python points.py -tf transactions.csv -ps 5000
```

This will spend 5000 points using the transactions from the `transactions.csv` file and print the final payer point balances as a dictionary.
