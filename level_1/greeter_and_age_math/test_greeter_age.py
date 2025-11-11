from datetime import date
from greeter_and_age_math import compute_age_years, approx_age_days

def test_age_years():
    assert compute_age_years(date(2000,1,1), date(2025,1,1)) == 25

def test_days():
    assert approx_age_days(date(1994,4,25), date(2025,11,11)) == 11523