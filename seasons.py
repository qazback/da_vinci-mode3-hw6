from datetime import date, datetime
import sys
import inflect


def main():
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        sys.exit(1)

    current_date = date.today()
    age_in_minutes = calculate_age_in_minutes(birth_date, current_date)
    print(convert_to_words(age_in_minutes))


def calculate_age_in_minutes(birth_date, current_date):
    minutes_per_day = 24 * 60
    days_per_year = 365

    if birth_date.month == 2 and birth_date.day == 29:
        leap_years = count_leap_years(birth_date, current_date)
        days_per_year = 366
        return (current_date.year - birth_date.year - leap_years) * days_per_year * minutes_per_day
    else:
        return (current_date - birth_date).days * minutes_per_day


def count_leap_years(start_date, end_date):
    leap_years = 0
    for year in range(start_date.year, end_date.year + 1):
        if is_leap_year(year):
            leap_years += 1
    return leap_years


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def convert_to_words(minutes):
    p = inflect.engine()

    hours = minutes // 60
    minutes %= 60
    days = hours // 24
    hours %= 24
    years = days // 365
    days %= 365

    age_words = []
    if years > 0:
        age_words.append(p.number_to_words(years) + " " + p.plural("year", years))
    if days > 0:
        age_words.append(p.number_to_words(days) + " " + p.plural("day", days))
    if hours > 0:
        age_words.append(p.number_to_words(hours) + " " + p.plural("hour", hours))
    if minutes > 0:
        age_words.append(p.number_to_words(minutes) + " " + p.plural("minute", minutes))

    return " ".join(age_words)


if __name__ == "__main__":
    main()
