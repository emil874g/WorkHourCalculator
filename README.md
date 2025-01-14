Salary Calculator

This Python script calculates a person's salary based on the number of hours worked and their hourly rate. It provides the salary before tax, after the Danish Labour Market Contribution (AM-bidrag), and after income tax.

Functions

calculate_salary_before_tax(hours_worked, hourly_rate)

Calculates the total salary before any taxes.

Parameters:

hours_worked (float): The number of hours worked.

hourly_rate (float): The hourly wage.

Returns:

(float): The total salary before tax.

calculate_salary_after_AM(hours_worked, hourly_rate)

Calculates the salary after an 8% Labour Market Contribution (AM-bidrag).

Parameters:

hours_worked (float): The number of hours worked.

hourly_rate (float): The hourly wage.

Returns:

(float): The salary after AM-bidrag.

calculate_salary_after_tax(hours_worked, hourly_rate)

Calculates the salary after AM-bidrag and an additional 38% income tax.

Parameters:

hours_worked (float): The number of hours worked.

hourly_rate (float): The hourly wage.

Returns:

(float): The salary after all taxes.

Usage

To use the script:

Run the script in a Python environment.

Enter the total number of hours worked when prompted.

Enter the hourly rate when prompted.

The script will output:

The salary before any taxes.

The salary after the 8% AM-bidrag.

The salary after both AM-bidrag and the 38% income tax.

Example

Indtast totale mængde timer arbejdet: 160
Indtast din timeløn: 200
Din løn før skat er: 32000.00 dkk
Din løn efter Arbejdsmarkedebidrag er: 29440.00 dkk
Din løn efter skat er: 18252.80 dkk

Error Handling

The script includes basic error handling:

If the input for hours worked or hourly rate is not a valid number, an error message will be displayed.

Requirements

Python 3.x

License

This project is licensed under the MIT License.

