def calculate_salary_before_tax(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

def calculate_salary_after_AM(hours_worked, hourly_rate):
    return calculate_salary_before_tax(hours_worked, hourly_rate) * 0.92 # 8% tax

def calculate_salary_after_tax(hours_worked, hourly_rate):
    return calculate_salary_after_AM(hours_worked, hourly_rate) * 0.62 # 38% tax


def main():
    try:
        hours_worked = float(input("Indtast totale mængde timer arbejdet: "))
        hourly_rate = float(input("Indtast din timeløn: "))
        total_salary = calculate_salary_before_tax(hours_worked, hourly_rate)
        
        am_bidrag = calculate_salary_after_AM(hours_worked, hourly_rate)
        tax = calculate_salary_after_tax(hours_worked, hourly_rate)
        
        print(f"Din løn før skat er: {total_salary:.2f} dkk")
        print(f"Din løn efter Arbejdsmarkedebidrag er: {am_bidrag:.2f} dkk")
        print(f"Din løn efter skat er: {tax:.2f} dkk")
        
    except ValueError:
        print("Indtast et validt tal og timeløn")

if __name__ == "__main__":
    main()