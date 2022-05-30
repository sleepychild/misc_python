# misc_python

Miscellaneous Python Stuff

## console_quiz

A question asked during a technical interview.

> How would you go about designing a quiz system that can handle Yes or No / Closed (a or b or c) / Open questions?

Add a quiz to the ```console_quiz/quizes``` folder. See the [example_quiz.json](console_quiz/quizes/example_quiz.json) file for reference.

Run with the following...

```bash
python3 console_quiz
```

Nearly the entire logic can be done by a single class. The only method required to handle special cases is ```_correct()```. The taken approach is to define different subclasses implementing a separate the method as they see fit. It could be handled with a control structure within the method itself. But where is the fun in that?

## infinite_cosmos

On kongregate I "play" (play in quotes because it can hardly be called gameplay) an idle / upgrades garbo game called [Infinite Cosmos](https://www.kongregate.com/games/GoldhurstGames/infinite-cosmos). It wastes my time and I want to automate it.

Run it with:
```bash
python infinite_cosmos
```

... Some more doc needed here