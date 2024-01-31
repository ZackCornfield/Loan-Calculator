# Loan Calculator with Python

This is the **Loan Calculator** project created by me.

Here's the link to the project: https://hyperskill.org/projects/90

Check out my profile: https://hyperskill.org/profile/606049336

## How to Run with Arguments

To run the Loan Calculator executable with arguments, follow these steps:

1. **Download the Executable**:
   - Download the executable file (`loan_calculator.exe` for Windows or without an extension for Unix-based systems) from the provided location.

2. **Open a Terminal or Command Prompt**:
   - Navigate to the directory containing the executable file.

3. **Run the Executable with Arguments**:
   - Execute the following command, replacing `[arguments]` with the desired parameters:
     ```
     ./loan_calculator [arguments]    # For Unix-based systems
     loan_calculator.exe [arguments]  # For Windows
     ```
   - For example:
     ```
     ./loan_calculator --type annuity --principal 100000 --periods 36 --interest 10    # For Unix-based systems
     loan_calculator.exe --type annuity --principal 100000 --periods 36 --interest 10  # For Windows
     ```

4. **View the Results**:
   - The program will process the provided arguments and output the calculated loan details based on the specified parameters.

## Parameters

- `--type`: Type of payment (`annuity` for fixed monthly payment or `diff` for differentiated payments).
- `--payment`: The annuity payment amount.
- `--principal`: The loan principal amount.
- `--periods`: The number of periods needed to repay the loan.
- `--interest`: The loan interest rate.

Ensure all parameters are provided with non-negative values.
