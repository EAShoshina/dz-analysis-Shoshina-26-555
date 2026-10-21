import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
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


def catalog_age_stats(
    movies: list[dict], current_year: int = 2026
) -> tuple[int, int, int]:
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


def print_non_comedy_titles(movies: list[dict]) -> None:
    """Этап 3: печатает названия не-комедий (демонстрация for + continue)."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_high_rated(movies: list[dict]) -> None:
    """Этап 3: ищет первый фильм с рейтингом > 9.0 (демо while + break + else)."""
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            movie = movies[index]
            print(f"Найден: {movie['title']} — рейтинг {movie['rating']}")
            break
        index += 1
    else:
        print("Шедевров не найдено")

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


def all_genres(movies: list[dict]) -> set[str]:
    """Возвращает множество всех уникальных жанров каталога."""
    result: set[str] = set()
    for movie in movies:
        result |= movie["genres"]
    return result


def common_actors(movie1: dict, movie2: dict) -> set[str]:
    """Возвращает множество актеров, снимавшихся в обоих фильмах."""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a: list[dict], movies_b: list[dict]) -> set[str]:
    """Возвращает жанры, встречающиеся в movies_a, но не встречающиеся в movies_b."""
    genres_a: set[str] = set()
    genres_b: set[str] = set()
    for movie in movies_a:
        genres_a |= movie["genres"]
    for movie in movies_b:
        genres_b |= movie["genres"]
    return genres_a - genres_b


def iter_high_rated(movies: list[dict], min_rating: float = 8.0):
    """Лениво отдаёт фильмы с рейтингом не ниже min_rating."""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def build_report(movies: list[dict]) -> None:
    """Собирает все этапы в единый консольный отчёт."""
    print("ОТЧЁТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")

    _, _, avg_age = catalog_age_stats(movies)
    print(f"Средний возраст фильмов: {avg_age} лет\n")

    print("Топ-3 фильма:")
    for title, _ in top_n_by_rating(movies, 3):
        movie = next(m for m in movies if m["title"] == title)
        print(" ", format_report_line(movie))
    print()

    print("Фильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    # Сначала по убыванию количества, при равенстве — по алфавиту
    for genre, count in sorted(genre_counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {genre} — {count}")
    print()

    print("Все жанры каталога:", ", ".join(sorted(all_genres(movies))))


if __name__ == "__main__":
    build_report(movies)