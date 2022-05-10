from os import scandir, DirEntry
from typing import List

from quiz import Quiz

def select_quiz() -> str:
    quizes: List[DirEntry] = list(filter(lambda x: x.is_file(), scandir("console_quiz/quizes")))
    print("Select quiz")
    for k, q in enumerate(quizes):
        print(f"{k}: {q.name}")
    print("press any key to quit")
    try:
        return quizes[int(input("Enter quiz number: "))].path
    except (
        ValueError,
        KeyError,
    ) as _:
        exit(0)


if __name__ == "__main__":
    while True:
        quiz_path: str = select_quiz()
        quiz: Quiz = Quiz.from_file_path_str(quiz_path)
        quiz.run()