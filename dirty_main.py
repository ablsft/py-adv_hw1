from datetime import *

from application.salary import *
from application.db.people import *
from google_search.search import *

if __name__ == '__main__':
    current_time = str(datetime.today()).split(".")[0]
    print(current_time)
    print()

    calculate_salary()
    get_employees()
    print()

    search_google('utc')