# Working with Others Using Version Control

This lesson will prepare you to use version control with a team. First, there will be a short review of key commands for working with git and Github on your own:

1. `git add`
2. `git commit`
3. `git push`

Next, you will learn how to

1. Create branches
2. Use git and Github for different workflows
3. Perform code reviews

## Scenario #1

Let's walk through the Git commands that go along with each step in the scenario you just observed in the video.

**Step 1: You have a local version of this repository on your laptop, and to get the latest stable version, you pull from the develop branch.**

> Switch to the develop branch
> `git checkout develop`
> 
> Pull the latest changes in the develop branch
> `git pull`

**Step 2: When you start working on this demographic feature, you create a new branch called demographic, and start working on your code in this branch.**

> Create and switch to a new branch called demographic from the develop branch
> 
> `git checkout -b demographic`
> 
> Work on this new feature and commit as you go
> 
> `git commit -m 'added gender recommendations'`
> `git commit -m 'added location specific recommendations'`
> `...`

**Step 3: However, in the middle of your work, you need to work on another feature. So you commit your changes on this demographic branch, and switch back to the develop branch.**

> Commit your changes before switching
>
> `git commit -m 'refactored demographic gender and location recommendations '`
>
> Switch to the develop branch
>
> `git checkout develop`

**Step 4: From this stable develop branch, you create another branch for a new feature called friend_groups.**

> Create and switch to a new branch called friend_groups from the develop branch
>
> `git checkout -b friend_groups`

**Step 5: After you finish your work on the friend_groups branch, you commit your changes, switch back to the development branch, merge it back to the develop branch, and push this to the remote repository’s develop branch.**

> Commit your changes before switching
>
> `git commit -m 'finalized friend_groups recommendations '`
>
> Switch to the develop branch
>
> `git checkout develop`
>
> Merge the friend_groups branch into the develop branch
> 
> `git merge --no-ff friends_groups`
>
> Push to the remote repository
>
> `git push origin develop`

**Step 6: Now, you can switch back to the demographic branch to continue your progress on that feature.**

> Switch to the demographic branch
>
> `git checkout demographic`

## Branching

This is one of the most fundamental tools needed when working with teams using git and Github.

- `git branch` which shows all the branches you have available
- `git checkout -b` which both creates a branch as well as moves you onto it

- `git branch -d` to delete a branch

## Scenario #2

Let's walk through the Git commands that fo along with each step in the scenario you just observed in the video

**Step 1: Andrew commites his changes to the documentation brand, switches to the development branc, and pulls down the latest changes from the cloud on this development branch, including the change I meerged previously for the friends group feature.**

> Commit the changes on the documentation branch
> 
> `git commit -m "standardize all docstrings in process.py"`

> Switch to the develop branch
> 
> `git checkout develop`

> Pull the latest changes on the develop brand down
> 
>  `git pull`

**Step 2: Andrew merges his documentation branch int the develop brand on his local repository, and then pushes his changes up to the update the develop branch on the remote repository**

> Merge the documentation branch into the develop branch
> 
> `git merge --no-ff documentation`

> Push the changes up to the remote repository
> 
> `git push origin develop`

**Step 3: After the team reviews your work and Andrew's work, they merge the updates from the development branch into the master branch. Then, they push the changes to the master branch on the remote repository. These changes are not in production.

> Merge the develop branch into the master branch
> 
> `git merge --no-ff develop`

> Push the changes up to the remote repository
> 
> `git push origin master`

**Resources**

Read [this great article](http://nvie.com/posts/a-successful-git-branching-model/) on a successfull Git branching strategy.

**Note on merge conflicts**

For the most part, Git makes merging changes between branches really simple. However, there are some cases where Git can become confused about ho to combine tow changes, and asks you for help. This is called a merge conflict. 

Most commonly, this happens when two branches modify the same file.

For example, in this situation, let's say you deleted a line that Andrew modified on his branch. Git wouldn't know whether to delete the line or modify it. You need to tell Git which change to take, and some tools even allow you to edit the change manually. If it isn't straightforward, you may have to consult with the develooper of the other branch to handle a merge conflict. 

To learn more about merge conflicts and methods to handle them, see [About merge conflicts](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-merge-conflicts)


## Version Control Workflow
In the **two** videos on this page, we will add to the flow already introduced with branching earlier. This means:

- Pushing our branches to Github
- Opening pull requests
- Introducing code reviews

Otherwise, the above flow shows a great workflow to follow including:

- Creating a new branch
- Adding new features and code
- `add` , `commit`, and `push` your changes to the remote
- Open a pull request
- Have another team member review your changes and merge them in
- Delete the remote branch
- Delete the local branch
- Pull the new code on the remote master to your local machine

## Model Versioning
In the previous example, you may have noticed that each commit was documented with a score for that model. This is one simple way to help you keep track of model versions. Version control in data science can be tricky, because there are many pieces involved that can be hard to track, such as large amounts of data, model versions, seeds, and hyperparameters.

The following resources offer useful methods and tools for managing model versions and large amounts of data. These are here for you to explore, but are not necessary to know now as you start your journey as a data scientist. On the job, you’ll always be learning new skills, and many of them will be specific to the processes set in your company.

- [How to version control your production machine learning models](https://blog.algorithmia.com/how-to-version-control-your-production-machine-learning-models/)
- [Version Control ML Model](https://towardsdatascience.com/version-control-ml-model-4adb2db5f87c)

## Scenario #3


Let's walk through the Git commands that go along with each step in the scenario you just observed in the video.

**Step 1: You check your commit history, seeing messages about the changes you made and how well the code performed.**

> View the log history
> 
> `git log`

**Step 2: The model at this commit seemed to score the highest, so you decide to take a look.**

> Check out a commit
> 
> `git checkout bc90f2cbc9dc4e802b46e7a153aa106dc9a88560`

After inspecting your code, you realize what modifications made it perform well, and use those for your model.

**Step 3: Now, you're confident merging your changes back into the development branch and pushing the updated recommendation engine.**

> Switch to the develop branch
> 
> `git checkout develop`


> Merge the friend_groups branch into the develop branch
> 
> `git merge --no-ff friend_groups`


> Push your changes to the remote repository
> 
> `git push origin develop`

## Code Reviews

Code reviews benefit everyone in a team to promote best programming practies and prepare code for production. Let's go over what to look for in a code review and some tips on how to conduct one. 

**Resources** 
- [Guidelines for Code Reivews](https://github.com/lyst/MakingLyst/tree/master/code-reviews)
- [Code Review Best Practices](https://www.kevinlondon.com/2015/05/05/code-review-best-practices.html)

**Questions to Ask Yourself when Conducting a Code Review**

First, let's look over some of the questions we might ask ourselves while reviewing code. These are drawn from the concepts covered throughout this course.

**Is the code clean and modular?**
- Can I understand the code easily?
- Does it use meaningful names and whitespace?
- Is there duplicated code?
- Can I provide another layer of abstraction?
- Is each function and module necessary?
- Is each function or module too long?
  
**Is the code efficient?**
- Can I use better data structures to optimize any steps?
- Can I shorten the number of calculations needed for any steps?
- Are there loops or other steps I can vectorize?
- Can I use generators or multiprocessing to optimize any steps?
- 
**Is the documentation effective?**
- Are inline comments concise and meaningful?
- Is there complex code that's missing documentation?
- Do functions use effective docstrings?
- Is the necessary project documentation provided?

**Is the code well tested?**
- Does the code high test coverage?
- Do tests check for interesting cases?
- Are the tests readable?
- Can the tests be made more efficient?

**Is the logging effective?**
- Do they include all relevant and useful information?
- Are log messages clear, concise, and professional?
- Do they use the appropriate logging level?

 ## Tips for Conducting a Code Review
Now that we know what we're looking for, let's go over some tips on how to actually write your code review. When your coworker finishes up some code that they want to merge to the team's code base, they might send it to you for review. You provide feedback and suggestions, and then they may make changes and send it back to you. When you are happy with the code, you approve it and it gets merged to the team's code base.

As you may have noticed, with code reviews you are now dealing with people, not just computers. So it's important to be thoughtful of their ideas and efforts. You are in a team and there will be differences in preferences. The goal of code review isn't to make all code follow your personal preferences, but to ensure it meets a standard of quality for the whole team.

**Tip: Use a code linter**

This isn't really a tip for code review, but it can save you lots of time in a code review. Using a Python code linter like pylint can automatically check for coding standards and PEP 8 guidelines for you. It's also a good idea to agree on a style guide as a team to handle disagreements on code style, whether that's an existing style guide or one you create together incrementally as a team.

**Tip: Explain issues and make suggestions**

Rather than commanding people to change their code a specific way because it's better, it will go a long way to explain to them the consequences of the current code and suggest changes to improve it. They will be much more receptive to your feedback if they understand your thought process and are accepting recommendations, rather than following commands. They also may have done it a certain way intentionally, and framing it as a suggestion promotes a constructive discussion, rather than opposition.

```
BAD: Make model evaluation code its own module - too repetitive.

BETTER: Make the model evaluation code its own module. This will simplify models.py to be less repetitive and focus primarily on building models.

GOOD: How about we consider making the model evaluation code its own module? This would simplify models.py to only include code for building models. Organizing these evaluations methods into separate functions would also allow us to reuse them with different models without repeating code.
```

**Tip: Keep your comments objective**

Try to avoid using the words "I" and "you" in your comments. You want to avoid comments that sound personal to bring the attention of the review to the code and not to themselves.

```
BAD: I wouldn't groupby genre twice like you did here... Just compute it once and use that for your aggregations.

BAD: You create this groupby dataframe twice here. Just compute it once, save it as groupby_genre and then use that to get your average prices and views.

GOOD: Can we group by genre at the beginning of the function and then save that as a groupby object? We could then reference that object to get the average prices and views without computing groupby twice.
```

**Tip: Provide code examples**

When providing a code review, you can save the author time and make it easy for them to act on your feedback by writing out your code suggestions. This shows you are willing to spend some extra time to review their code and help them out. It can also just be much quicker for you to demonstrate concepts through code rather than explanations.

Let's say you were reviewing code that included the following lines:

```
first_names = []
last_names = []

for name in enumerate(df.name):
    first, last = name.split(' ')
    first_names.append(first)
    last_names.append(last)

df['first_name'] = first_names
df['last_names'] = last_names

```
```
BAD: You can do this all in one step by using the pandas str.split method.
GOOD: We can actually simplify this step to the line below using the pandas str.split method. Found this on this stack overflow post: https://stackoverflow.com/questions/14745022/how-to-split-a-column-into-two-columns
```
```
df['first_name'], df['last_name'] = df['name'].str.split(' ', 1).str
```