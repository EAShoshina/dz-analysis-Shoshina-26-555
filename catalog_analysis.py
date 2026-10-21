import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies: list[dict]) -> float:
    """Возвращает среднюю оценку по каталогу, округлённую до одного знака."""
    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(movies: list[dict], current_year: int = 2026) -> tuple[int, int, int]:
    """Возвращает (возраст самого старого, возраст самого нового, средний возраст)."""
    ages = [current_year - movie["year"] for movie in movies]
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes: int) -> str:
    """Переводит минуты в формат '2ч 35м'."""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


def rating_tier(rating: float) -> str:
    """Возвращает категорию оценки: шедевр / хорошо / средне / слабо."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year: int) -> str:
    """Возвращает метку десятилетия: новые / недавние / старые."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


def main() -> None:
    print("Средняя оценка:", average_rating(movies))
    print("Статистика возраста:", catalog_age_stats(movies))
    print("155 минут =", duration_in_hours(155))
    print("89 минут =", duration_in_hours(89))

    print("\n--- Этап 2 ---")
    print("rating_tier(9.5) =", rating_tier(9.5))
    print("rating_tier(7.0) =", rating_tier(7.0))
    print("rating_tier(5.5) =", rating_tier(5.5))
    print("rating_tier(4.9) =", rating_tier(4.9))
    print("rating_tier(9.0) =", rating_tier(9.0))
    print("rating_tier(8.9) =", rating_tier(8.9))

    print("decade_label(2024) =", decade_label(2024))
    print("decade_label(2020) =", decade_label(2020))
    print("decade_label(2015) =", decade_label(2015))
    print("decade_label(2014) =", decade_label(2014))
    print("decade_label(2021) =", decade_label(2021))


if __name__ == "__main__":
    main()