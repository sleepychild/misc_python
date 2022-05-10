from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict


@dataclass
class QuestionSkell:
    question: str
    question_prompt: str
    answer: str
    points: int
    options: Dict

    answered: bool
    given_answer: str


class Question(ABC, QuestionSkell):
    def __init__(self, object_dict: Dict) -> None:
        for key, val in object_dict.items():
            setattr(self, key, val)

    def ask(self) -> None:
        print(self.question)
        for k, v in self.options.items():
            print(f"{k}) {v}")
        self.given_answer = input(self.question_prompt).strip().lower()
        self.answered = True

    def result(self) -> int:
        if not self.answered:
            print(f"You have not answered the question")

        print(
            f"The question was: {self.question}",
            f"\nThe correct answer was: {self.answer} {None if len(self.options) == 0 else self.options[self.answer]}",
            f"\nThe given answer was: {self.given_answer} {None if len(self.options) == 0 else self.options.get(self.given_answer, 'Undefined')}",
        )

        if self._correct():
            print(f"You answered correctly and get {self.points} points.")
            return self.points
        else:
            print("You answered incorrectly and get no points.")
            return int()

    def _correct(self) -> bool:
        return self.given_answer == self.answer if self.answered else False

    @abstractmethod
    def _correct(self) -> bool:
        raise NotImplementedError("The _correct method must be implemented.")


class Yorn(Question):
    def _correct(self) -> bool:
        return self.given_answer[0] == self.answer[0] if self.answered else False


class Closed(Question):
    def _correct(self) -> bool:
        return self.given_answer[0] == self.answer[0] if self.answered else False


class Open(Question):
    def _correct(self) -> bool:
        return self.given_answer.find(self.answer) != -1 if self.answered else False
