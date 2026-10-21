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


def count_long_movies(movies: list[dict], threshold: int = 120) -> int:
    """Считает количество фильмов длиннее threshold минут (без sum() по списку)."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title: str) -> str:
    """Приводит строку к Title Case без str.title()."""
    words = title.split()
    normalized = []
    for word in words:
        normalized.append(word[0].upper() + word[1:])
    return " ".join(normalized)


def make_slug(title: str) -> str:
    """Превращает нормализованное название в слаг вида the-quiet-algorithm."""
    normalized = normalize_title(title)
    return normalized.lower().replace(" ", "-")


def format_report_line(movie: dict) -> str:
    """Возвращает строку отчёта о фильме."""
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{title}" ({movie["year"]}) — '
        f'{movie["rating"]}/10, {duration}, жанры: {genres}'
    )


def titles_sorted_by_rating(movies: list[dict]) -> list[str]:
    """Возвращает список названий фильмов, отсортированных по убыванию рейтинга."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [m["title"] for m in sorted_movies]


def top_n_by_rating(movies: list[dict], n: int = 3) -> list[tuple[str, float]]:
    """Возвращает топ-n фильмов по рейтингу в виде списка кортежей (title, rating)."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(m["title"], m["rating"]) for m in sorted_movies[:n]]


def count_by_genre(movies: list[dict]) -> dict[str, int]:
    """Возвращает словарь {жанр: количество фильмов}."""
    result: dict[str, int] = {}
    for movie in movies:
        for genre in movie["genres"]:
            result[genre] = result.get(genre, 0) + 1
    return result


def actor_filmography(movies: list[dict]) -> dict[str, list[str]]:
    """Возвращает словарь {актер: [список названий фильмов]}."""
    result: dict[str, list[str]] = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in result:
                result[actor] = []
            result[actor].append(movie["title"])
    return result


def above_average_ratings(movies: list[dict]) -> dict[str, float]:
    """Возвращает {title: rating} только для фильмов с рейтингом выше среднего."""
    avg = average_rating(movies)
    return {m["title"]: m["rating"] for m in movies if m["rating"] > avg}


def main() -> None:
    # Этап 1
    print("Этап 1")
    print("Средняя оценка:", average_rating(movies))
    print("Статистика возраста:", catalog_age_stats(movies))
    print("155 минут =", duration_in_hours(155))
    print("89 минут =", duration_in_hours(89))

    # Этап 2
    print("\nЭтап 2")
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

    # Этап 3
    print("\nЭтап 3: фильмы не комедии (for + continue) которые НЕ относятся к жанру 'comedy'")
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

    print("\nПервый фильм с рейтингом > 9.0 (while + break + else)")
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            print("Найден:", movies[index]["title"], "— рейтинг", movies[index]["rating"])
            break
        index += 1
    else:
        print("Шедевров не найдено")

    print("\nПроверка ветки else (список без шедевров)")
    movies_without_masterpieces = [m for m in movies if m["rating"] <= 9.0]
    index = 0
    while index < len(movies_without_masterpieces):
        if movies_without_masterpieces[index]["rating"] > 9.0:
            print("Найден:", movies_without_masterpieces[index]["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")

    print("\nКоличество фильмов длиннее 120 минут")
    print("count_long_movies(movies) =", count_long_movies(movies))
    print("count_long_movies(movies, 100) =", count_long_movies(movies, 100))

    # Этап 4
    print("\nЭтап 4: строки")
    print('normalize_title("silent hours") =', normalize_title("silent hours"))
    print('normalize_title("midnight in oslo") =', normalize_title("midnight in oslo"))
    print('make_slug("Silent Hours") =', make_slug("Silent Hours"))
    print('make_slug("midnight in oslo") =', make_slug("midnight in oslo"))
    print('format_report_line(movies[7]) =', format_report_line(movies[7]))
    print('format_report_line(movies[2]) =', format_report_line(movies[2]))

    # Этап 5
    print("\nЭтап 5: списки")
    print("titles_sorted_by_rating(movies):")
    for title in titles_sorted_by_rating(movies):
        print(" ", title)

    print("\ntop_n_by_rating(movies, 3):")
    for item in top_n_by_rating(movies, 3):
        print(" ", item)

    print("\ntop_n_by_rating(movies, 5):")
    for item in top_n_by_rating(movies, 5):
        print(" ", item)

    print("\nПроверка: исходный movies не изменён")
    print('movies[0]["title"] =', movies[0]["title"])

    # Этап 6
    print("\nЭтап 6: словари")
    print("count_by_genre(movies):")
    for genre, count in sorted(count_by_genre(movies).items()):
        print(f"  {genre}: {count}")

    print("\nactor_filmography(movies):")
    for actor, films in sorted(actor_filmography(movies).items()):
        print(f"  {actor}: {films}")

    print("\nabove_average_ratings(movies):")
    for title, rating in above_average_ratings(movies).items():
        print(f"  {title!r}: {rating}")


if __name__ == "__main__":
    main()