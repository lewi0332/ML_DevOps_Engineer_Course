# Clean Code Principles

- Maintainability
- Depenability
- Efficiency
- Usability

Clean code is essential for all tech. 

1. Writing clean and modular code
2. Refactoring code
3. Optimizing code to be more efficient
4. Writing documentation
5. Following PEP8 & Linting

Clean and modular code.

*Production Code*: Software running on production servers to handle live users and data of the intended audience. Note that this id different from Production Quality Code, which describes code that meets expectations for production in reliability, efficiency, and other aspects. Ideally, all code in rduction meets these expectations, but this is not aleays the case.

*Clean Code*: Code that is readable, simple, and concise. Clean productin-quality code is crucial for collaboration and maintainability in software development. 

*Modular* code: Code that is logically broke up into functions and modules. Modular production-quality code that makes your code more organized, efficient, and reusable.

*Module*: A file. Modules allow code to be reused by encapsulating them into files that can be imported into other files.

*Writing Clean Code: Meaningful Names*

Use meaningful names.

- Be descriptive and imply type: For booleans, you can prefix with `is_` or `has_` to make it clear it is a condition. You can also use parts of speech to imply types, like using verbs for functions and nouns for variables.
- Be consistent but clearly differentiate: `age_list` and `age` is easier to differentiate than `ages` and `age`.
- Avoid abbreviations and single letters: You can determine when to make these exceptions based on the audience for your code. If you work with other data scientists, certain variables may be common knowledge. While if you work with full stack engineers, it might be necessary to provide more descriptive names in these cases as well. (Exceptions include counters and common math variables.)
- Long names aren't the same as descriptive names: You should be descriptive, but only with relevant information. For example, good function names describe what they do well without including details about implementation or highly specific uses.

Try testing how effective your names are by asking a fellow programmer to guess the purpose of a function or variable based on its name, without looking at your code. Coming up with meaningful names often requires effort to get it right.

*Writing Clean Code: Nice Whitespace*

Use whitespace properly.

- Organize your code with consistent indentation: the standard is to use four spaces for each indent. You can make this a default in your text editor.
- Separate sections with blank lines to keep your code well organized and readable.
- Try to limit your lines to around 79 characters, which is the guideline given in the PEP 8 style guide. In many good text editors, there is a setting to display a subtle line that indicates where the 79 character limit is.

For more guidelines, check out the code layout section of PEP 8 in the following notes.

*References*
- [PEP 8](https://www.python.org/dev/peps/pep-0008/?#code-lay-out)

Follow the tips below to write modular code.
**Tip: DRY (Don't Repeat Yourself)**
Don't repeat yourself! Modularization allows you to reuse parts of your code. Generalize and consolidate repeated code in functions or loops.

**Tip: Abstract out logic to improve readability**
Abstracting out code into a function not only makes it less repetitive, but also improves readability with descriptive function names. Although your code can become more readable when you abstract out logic into functions, it is possible to over-engineer this and have way too many modules, so use your judgement.

**Tip: Minimize the number of entities (functions, classes, modules, etc.)**
There are trade-offs to having function calls instead of inline logic. If you have broken up your code into an unnecessary amount of functions and modules, you'll have to jump around everywhere if you want to view the implementation details for something that may be too small to be worth it. Creating more modules doesn't necessarily result in effective modularization.

**Tip: Functions should do one thing**
Each function you write should be focused on doing one thing. If a function is doing multiple things, it becomes more difficult to generalize and reuse. Generally, if there's an "and" in your function name, consider refactoring.

**Tip: Arbitrary variable names can be more effective in certain functions**
Arbitrary variable names in general functions can actually make the code more readable.

**Tip: Try to use fewer than three arguments per function**
Try to use no more than three arguments when possible. This is not a hard rule and there are times when it is more appropriate to use many parameters. But in many cases, it's more effective to use fewer arguments. Remember we are modularizing to simplify our code and make it more efficient. If your function has a lot of parameters, you may want to rethink how you are splitting this up.

### Refactoring 

- *Refactoring*: Restructuring your code to improve its internal structure without changing its external functionality. This gives you a chance to clean and modularize your program after you've got it orking. 
- Since it isn't easy to write your best code while you're still triing to just get it working, allocation time to do this is essential to producing high-qualit code. Despite the initial time and effor required, this really pays off by speeding up your development time in the long run. 
- You become a much stronger programmer when you're constantly looking to improve your code. The more you refactor, the easier it will be to structure and write good code the first time.

### Efficient Code

Knowing how to write code that runs efficiently as another essential skill in software development. Optimiszing code to be more efficient can mean making it:

- Execute faster
- Take up less space in memory/storage

When you're performing lots of differnt transformations on large amounts of data this can make orders of magnitudes of differenc in performance.

### Documentation


- Documentation: Additional text or illustrated information that comes with or is embedded in the code of software.
- Documentation is helpful for clarifying complex parts of code, making your code easier to navigate, and quickly conveying how and why different components of your program are used.
- Several types of documentation can be added at different levels of your program:
  - **Inline comments** - line level
  - **Docstrings** - module and function level
  - **Project documentation** - project level

**Inline Comments**
- Inline comments are text following hash symbols (in the case of Python, anyway) throughout your code. They are used to explain parts of your code, and really help future contributors understand your work.
- Comments often document the major steps of complex code. Readers may not have to understand the code to follow what it does if the comments explain it. However, others would argue that this is using comments to justify bad code, and that if code requires comments to follow, it is a sign refactoring is needed.
- Comments are valuable for explaining where code cannot. For example, the history behind why a certain method was implemented a specific way. Sometimes an unconventional or seemingly arbitrary approach may be applied because of some obscure external variable causing side effects. These things are difficult to explain with code.

**Docstrings**
Docstrings, or documentation strings, are valuable pieces of documentation that explain the functionality of any function or module in your code. Ideally, each of your functions should always have a docstring.

Docstrings are surrounded by triple quotes. The first line of the docstring is a brief explanation of the function's purpose.

**One-line docstring**

```
def population_density(population, land_area):
    """Calculate the population density of an area."""
    return population / land_area
```

If you think that the function is complicated enough to warrant a longer description, you can add a more thorough paragraph after the one-line summary.

**Multi-line docstring**

```
def population_density(population, land_area):
    """Calculate the population density of an area.

    Args:
    population: int. The population of the area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms of square km or square miles the function will return a density in those units.

    Returns:
    population_density: population/land_area. The population density of a 
    particular area.
    """
    return population / land_area
```

The next element of a docstring is an explanation of the function's arguments. Here, you list the arguments, state their purpose, and state what types the arguments should be. Finally, it is common to provide some description of the output of the function. Every piece of the docstring is optional; however, doc strings are a part of good coding practice. 

**Resources**
- (PEP 257 - Docstring Conventions)[https://www.python.org/dev/peps/pep-0257/]
- (NumPy Docstring Guide)[https://numpydoc.readthedocs.io/en/latest/format.html]

**Project Documentation**

Project documentation is essential for getting others to understand why and how your code is relevant to them, whether they are potentials users of your project or developers who may contribute to your code. A great first step in project documentation is your README file. It will often be the first interaction most users will have with your project.

Whether it's an application or a package, your project should absolutely come with a README file. At a minimum, this should explain what it does, list its dependencies, and provide sufficiently detailed instructions on how to use it. Make it as simple as possible for others to understand the purpose of your project and quickly get something working.

Translating all your ideas and thoughts formally on paper can be a little difficult, but you'll get better over time, and doing so makes a significant difference in helping others realize the value of your project. Writing this documentation can also help you improve the design of your code, as you're forced to think through your design decisions more thoroughly. It also helps future contributors to follow your original intentions.

(There is a full Udacity course on this topic.)[https://www.udacity.com/course/writing-readmes--ud777]

Here are a few READMEs from some popular projects:

- (Bootstrap)[https://github.com/twbs/bootstrap]
- (Scikit-learn)[https://github.com/scikit-learn/scikit-learn]
- (Stack Overflow Blog)[https://github.com/jjrunner/stackoverflow]

## Conclusion
In this lesson, learned 5 key factors to coding best practices:

1. Writing clean and modular code
2. Refactoring code
3. Optimizing code to be more efficient
4. Writing documentation
5. Following PEP8 & Linting

With these skills, you are ready to take your coding to the next level! When you first start solving a problem, it is important to focus on getting to a solution. However, once you have a solution, these factors are the key to writing better code. Each of these should be top of mind when you are working with a team, writing code for production, or even just writing code for future you!