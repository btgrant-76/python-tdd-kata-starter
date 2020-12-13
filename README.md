# Test-Driven Development Kata Starter Project
This project is intended to give developers a simple starting point to practice Test-Driven Development (TDD) using katas. Learning to practice TDD is not like learning a framework or a library. When learning to use a library, you read the docs and sample code and then you're either able to use the library successfully, or you're not. TDD, on the other hand, is a practice:  it is not about *what you're doing* as much as it is about *how you're doing it*.

## What is Test-Driven Development? 

Though TDD can apply to a number of different types of tests, this project focuses on applying TDD to writing unit tests. While unit testing often involves writing tests *after* software is feature-complete, TDD involves writing tests *before* writing the software that is to be tested. Another way of explaining this approach would be to say that unit tests and software are developed together, but the unit tests are often a step ahead of the software itself. If you're unfamiliar with TDD, the idea of writing tests *before* writing software might seem odd. [Uncle Bob's "Three Rules of TDD"](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd) captures the workflow very succinctly:  

> 1. You are not allowed to write any production code unless it is to make a failing unit test pass.
> 1. You are not allowed to write any more of a unit test than is sufficient to fail; and compilation failures are failures.
> 1. You are not allowed to write any more production code than is sufficient to pass the one failing unit test.

## Introductory Reading
These are short. You should read them; I'll wait:
- [Kata - the Only Way to Learn TDD](http://www.peterprovost.org/blog/2012/05/02/kata-the-only-way-to-learn-tdd/). In addition to discussing the practice of TDD katas, the author lists a number of TDD katas.
- [Uncle Bob's "Three Rules of TDD"](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd)
- [TDD Test-driven development cycle from Wikipedia](https://en.wikipedia.org/wiki/Test-driven_development#Test-driven_development_cycle) for another perspective on the "Three Rules"

## What's in This Project

Fairly minimal setup that will help you install the necessary dependencies to use [`pytest`](https://docs.pytest.org/) to practice TDD katas. A couple of nice-to-haves have been included that I feel add to the enjoyment of practicing TDD. 
- a starter this project has everything you'll need to get started learning TDD with Python and `pytest`.

- `reqiurements.txt`:  Install the project's requirements with `pip install -r requirements.txt`.
- `pytest.ini`:  This configuration tells `pytest` where to find both source files and test files. 
- `src/string_calculator.py` and `test/string_calculator_test.py`:  Starter files for the [String Calculator kata](https://osherove.com/tdd-kata-1/)
  
### Commands
- `pytest`: run this command at the root of the project in order to run all tests
- `ptw`:  run this command at the root of the project and [pytest-watch](https://pypi.org/project/pytest-watch/) will automatically run the tests any time a file in the project changes 
- `pytest --cov=src` If you're interested in coverage



## What's not in this project?
mocking libraries like `mockito`. While learning to leverage powerful mocking libraries is an important part of learning to write properly-isolated unit tests, that is not the goal of this project and such resources have been intentionally excluded.

## What should I do now?
Fork this project and make it your own. There's a starter string calculator test file, but feel free to create your own. add other katas, etc. Don't like the string calculator starter files that I provided? Delete them and create your own!

If you're looking for more 
- project euler
- https://www.programmingwithwolfgang.com/tdd-kata/ 

# TODOs
- [ ] refer to the [Evernote](evernote:///view/3502671/s31/459a93bc-addb-f95e-dda1-366e126ec926/2a7e5e6a-a1aa-41f8-b569-20be26c040cb)
- [x] set up the `.gitignore` properly for a Python project
