# Test-Driven Development Kata Starter Project
This project is intended to give developers a simple starting point to practice Test-Driven Development (TDD) using katas. Learning to practice TDD is not like learning a framework or a library. When learning to use a library, you read the docs and sample code and then you're either able to use the library successfully, or you're not. TDD, on the other hand, is a practice:  it is not about *what you're doing* as much as it is about *how you're doing it*.

## What is Test-Driven Development? 
Though TDD can apply to a number of different types of tests, this project focuses on applying TDD to writing unit tests. While unit testing often involves writing tests *after* the software complete, TDD involves writing tests *before* writing the software that is to be tested. Another way of explaining this approach would be to say that unit tests and software are developed together, but the unit tests are often a step ahead of the software itself. If you're unfamiliar with TDD, the idea of writing tests *before* writing software might seem odd. [Uncle Bob's "Three Rules of TDD"](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd) captures the workflow very succinctly:  

> 1. You are not allowed to write any production code unless it is to make a failing unit test pass.
> 1. You are not allowed to write any more of a unit test than is sufficient to fail; and compilation failures are failures.
> 1. You are not allowed to write any more production code than is sufficient to pass the one failing unit test.

## Introductory Reading
These are short. You should read them; I'll wait:
- [Kata - the Only Way to Learn TDD](http://www.peterprovost.org/blog/2012/05/02/kata-the-only-way-to-learn-tdd/)  The author lists a number of TDD katas in addition to discussing the practice.
- [Uncle Bob's "Three Rules of TDD"](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd)
- [TDD Test-driven development cycle from Wikipedia](https://en.wikipedia.org/wiki/Test-driven_development#Test-driven_development_cycle) for another perspective on the "Three Rules"

## What's in This Project
The project features a minimal setup to allow you to quickly start practicing TDD katas using Python and [`pytest`](https://docs.pytest.org/). 

- `reqiurements.txt`:  Install the project's requirements/dependencies with `pip install -r requirements.txt`.
- `pytest.ini`:  This configuration tells `pytest` where to find both source and test files so.
- `src/string_calculator.py` and `test/string_calculator_test.py`:  Starter files for the [String Calculator kata](https://osherove.com/tdd-kata-1/)
  
### Commands
All of these commands can be run at the root of the project.
- `pytest`:  run all tests
- `pytest --cov=src`:  run all tests and produce a test coverage report. This is certainly not necessary for learning TDD, but it can be interesting to understand how complete your unit tests are.
- `ptw`:  starts [pytest-watch](https://pypi.org/project/pytest-watch/) which will automatically run all tests any time a file in the project has changed. While this is not necessary for learning TDD, I have found that tools like this add to the enjoyment of practicing TDD. 

## What's Not in This Project
Mocking libraries like `mockito` have been intentionally excluded. While learning to leverage powerful mocking libraries is an important part of learning to write properly-isolated unit tests, that is not the goal of this project.

## What Should I Do Now?
Clone or fork this project and make it your own! You can complete the starter String Calculator files, or you can delete them and create your own. Obviously, you can add files and start practicing other katas. If you're looking for more, [this blog post](https://www.programmingwithwolfgang.com/tdd-kata/) contains a nice list; Google will help you find plenty more.
