# Library Management System

This project is a simple Library Management System implemented in Python. It allows users to perform various operations such as adding books, listing books, deleting books, updating books, and more.

## Code Structure

The project consists of the following files:

1. **main.py**: This is the main entry point of the application. It obtains input from the user using the command-line interface (CLI) and invokes corresponding functions to perform library management operations.

2. **check.py**: This file contains functions for checking the availability of books and user eligibility for borrowing books.

3. **book.py**: This file defines the `Book` class, which represents individual books in the library. It includes functionalities related to adding, listing, deleting, and updating books.

4. **user.py**: This file defines the `User` class, which represents library users. It includes functionalities related to adding users, listing users, deleting users, and updating user information.

5. **models.py**: This file contains complex operations and logic for managing books, users, and their interactions. It provides an abstraction layer for performing operations on books and users.

6. **storage.py**: This file provides functionality for storing data in different formats, such as JSON, CSV, or databases. It abstracts away the details of data storage and retrieval from the rest of the application.

## Usage

To run the Library Management System:

1. Ensure that you have Python installed on your system.

2. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/shashidharvy/library_management_system.git
   ```

3. Navigate to the project directory:

   ```bash
   cd library_management_system
   ```

4. Run the main.py file:

   ```bash
   python main.py
   ```

5. Follow the instructions provided in the command-line interface to perform various library management operations.

## Dependencies

The project has no external dependencies and only uses Python's built-in libraries.

