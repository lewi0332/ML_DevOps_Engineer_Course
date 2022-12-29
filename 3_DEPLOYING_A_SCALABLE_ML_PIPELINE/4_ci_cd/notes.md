# Continuous Integration/Continuous Deployment/Continuous Training

**Introduction**

There are nearly as many "principles" of software engineering as grains of sand on a beach. Many principles focus on the process of writing code (such as the Single Responsibility Principle that states that every module/class/function should serve a single purpose), but for our purposes here we will focus on principles that pertain to model deployment.

Specifically we will focus on automation, testing, and versioning. None of these are unique to deploying a model, but each one plays an important role as we will see in the following lectures.

These principles leads us into Continuous Integration and Continuous Delivery (CI/CD). To put CI/CD into practice we will leverage GitHub Actions and Heroku, respectively.

- Software Engineering Principle: Automation
- Software Engineering Principle: Testing
- Software Engineering Principle: Versioning
- Continuous Integration with GitHub Actions
- Continuous Deployment with Heroku

## Software Engineering Principle -- Automation

**Autmoation** is the principle where we set up processes to do rote tasks for us routinely, such as on a schedule or when another action happens.

Automation can take many forms. For instance:

- **Code formatters** such as Black which remove the need to fiddle with exact placement of spaces, parenthesis, etc. in code.
- **Editor features** which vary depending on the text editor or IDE you use. For example, I have Vim set to remove EOL whitespace when saving a file since that clutters Git diffs and can break things like line continuation characters in shell scripts.
- **Pre-Commit hooks** allow us to run code, like formatters, before we commit a change. Since we're going to commit our code, this saves us from having to run a formatter separately.

Collectively, using automation helps you save time and reduces the risk of errors.

A related principle to automation is **Don't Repeat Yourself (DRY)**. While not automation per se, it's a close cousin. We write functions instead of copy and pasting or rewriting code, and with automation, we set up processes instead of needing to retype or copy commands into the development environment.

**Further Reading**

To learn more about Git hooks see [here](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) and [here](https://pre-commit.com/).


## Software Engineering Principle -- Testing

When writing code we expect it to function as we planned, but often there can be unforeseen situations or edge cases. **Testing** is the principle we leverage to ensure our code functions as intended and is reproducible. A robust testing suite allows us to harden our code and make us more confident that, e.g., a function that does X actually does X instead of Y.

If we design our tests well, it can also help us catch edge cases that otherwise would have slipped through. Furthermore, if we tweak our code it ensures that we don't alter behavior unexpectedly.

**Tests build trust**. This trust is both for yourself but also for anyone you collaborate with. A robust testing suite should be developed alongside your code such that nearly every piece of functionality has a corresponding unit test.

As covered in a previous course, do not forget that machine learning models are inherently stochastic and built on data. The approach to testing these may be different and rely on tools such as Great Expectations.

Tests are like seat belts and safety bags. Their presence is not a guarantee that harm will not befall your code, but it is a best practice that mitigates harm in case something goes awry.

