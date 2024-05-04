# Terminal-based-banking-application
A simple terminal app for basic banking operations. Users can view balance, deposit, withdraw, and perform currency exchange. Implements logging for transactions. Currency rates are fetched from an external API.

This repository houses a terminal-based banking application designed to offer basic account operations and currency exchange functionalities. Built with simplicity and functionality in mind, the application provides an intuitive terminal interface, allowing users to interact with the system using commands.

Key Features:

Terminal Interface:
Implements an intuitive terminal interface with prompts for available commands.
Users can select actions by entering corresponding command numbers.
Basic Account Operations:
Supports essential account operations, including:
Viewing balance
Depositing funds
Withdrawing funds
Viewing transaction history
Currency exchange
Implements validation checks for deposit and withdrawal operations to ensure correctness of provided amounts.
Displays appropriate error messages for incorrectly specified values during deposit and withdrawal attempts.
Reads transaction history from a JSON file and displays it line by line in the terminal.
Performs currency exchange by sending an HTTP request to a server to retrieve the latest exchange rates.
Logging Transaction History:
Logs transaction history for deposit, withdrawal, and currency exchange operations.
Logs are stored in a "history.json" file.
Each type of operation is structured with relevant details, including operation type, status (success/failure), amount, total balance, currency from, and currency to.
Classes:
Includes classes for the account and currency exchange functionalities.
The account class manages account properties (balance, transaction history) and methods (deposit, withdrawal, get balance).
The currency exchange class handles currency rates and methods for currency exchange and rate updates using network requests.
Usage:

Clone the repository and run the application in a terminal environment.
Follow the prompts to perform account operations and currency exchange.
Contributions:

Contributions to improve functionality, add features, or fix bugs are welcome. Please submit pull requests with clear descriptions of the changes.
