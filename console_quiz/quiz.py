from functools import reduce
from os import path
import json

from typing import Any, Dict, List

import question

class Quiz:

    def __init__(self, name: str, description: str, questions: List[Dict]) -> None:
        self.name: str = name
        self.description: str = description
        self.questions: List = list()
        for q in questions:
            self.questions.append(getattr(question, q.pop("question_type"))(q))

    def _max_score(self) -> int:
        return sum([q.points for q in self.questions])

    def run(self) -> None:
        print(f"Welcome to {self.name}\n{self.description}")
        score: int = int()
        for question in self.questions:
            question.ask()
        for question in self.questions:
            score += question.result()
        print(f"Total score: {score}/{self._max_score()}")

    @classmethod
    def from_file_path_str(cls, file_path_str: str) -> "Quiz":
        file_path = path.abspath(file_path_str)
        print(f"Loading quiz file from {file_path}")
        with open(file_path, "r") as f:
            quiz_dict: Dict[str, Any] = json.load(f)
        return cls(*quiz_dict.values())