from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_employees
from google_search.search import search_google

if __name__ == '__main__':
    current_time = str(datetime.today()).split(".")[0]
    print(current_time)
    print()

    calculate_salary()
    get_employees()
    print()

    search_google('utc')