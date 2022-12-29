# Introduction to Deploying a Scalable ML Pipeline in Production

### Course Overview

**Lesson 1: Introduction to Deploying a Scalable ML Pipeline in Production**

This is the lesson you're in right now! In this lesson, we introduce you to:

- The big picture – what is this course about and why does it matter?
- The project you'll build at the end of the course.
- The prerequisites you'll need to have before you take this course.
- The business stakeholders you'll interact with as a professional in this field.
- The tools and environment you'll need for the course.

By the end of this lesson, you'll have context on what this course is about and what you'll need to have to succeed in the course.

**Lesson 2: Performance Testing and Preparing a Model for Production**

In this lesson we'll learn:

- How to finalize preparing a model for production by analyzing performance on slices.
- Some of the different types of bias and how to probe a model for bias using Aequitas.
- Write a model card which encapsulates the purpose, provenance, and pitfalls of your model.

By the end of this lesson, you'll be able to thoroughly audit and document a model before deploying it into production.

**Lesson 3: Data and Model Versioning**

In this lesson we'll learn:

- How to version control data and models using Data Version Control (DVC).
- Set up and connect remote storage with DVC.
- Create pipelines and track experiments using DVC.

By the end of this lesson, you'll be able to use all the core functionality of DVC which, despite the name, includes both version controlling data and models, but also creating reproducible pipelines and experimentation frameworks.

**Lesson 4: CI/CD**

In this lesson we'll learn:

- A few key software engineering principles including automating, testing, and versioning.
- How to use GitHub Actions for Continuous Integration (CI).
- How to use Heroku for app hosting and Continuous Deployment (CD).

By the end of this lesson, you'll be able to set up the entire infrastructure necessary to create a robust web app including CI/CD.

**Lesson 5: API Deployment with FastAPI**

In this lesson we'll learn:

- How to write an API using FastAPI including path, query, and body parameters.
- The principles behind Heroku and how to deploy an API using both the CLI and the GUI.
- How to test the live app using the requests module.

By the end of this lesson, you'll be able to write and deploy an API to Heroku and test it both locally and in production.

**How It All Comes Together**

This course not only gives you the skills and tools to write and deploy an API, but teaches the framework and techniques necessary to both trust what you deploy and trust the process by which you deploy. This is accomplished by techniques such as model slicing and writing a model card, but also frameworks such as DVC/GitHub (i.e. version control absolutely everything), and CI/CD.

**What You Should Know Before Taking This Course**

To succeed in this course, you should already be able to:

- Write intermediate Python such as documented functions, decorators, and creating a package.
- Unit tests using the pytest module.
- Git particularly using the CLI.
- Train and validate a ML model using scikit-learn, PyTorch, etc. No particular framework will be used here, but all the examples leverage scikit-learn.
- Basics of REST APIs such as an understanding of the common methods like GET, and POST.

If all of those sound familiar and comfortable, you should be ready for this course!

**Resources**

If you do feel unsure about any of the above skills and want to spend time strengthening them, here are some resources that you may find helpful:

- [pytest documentation](https://docs.pytest.org/en/6.2.x/contents.html)
- [Git cheat sheet made by GitHub](https://education.github.com/git-cheat-sheet-education.pdf)
- [REST API Tutorial](https://www.restapitutorial.com/) and [Understanding the basics of RESTful APIs by Pusher](https://pusher.com/tutorials/understanding-rest-api/)

## What You'll Build

At the end of the course you will build your very own API using FastAPI and deploy it using Heroku. The API will run machine learning inference, in this case a prediction on the Census Income Data Set. In the process of building this model and API you will check performance on slices, write a model card, track your data and models using DVC, and use GitHub Actions and Heroku for CI/CD.

The project on its own can stand as a portfolio piece since it leverages so many different technologies. Additionally, the various technologies can easily be incorporated into other projects be it portfolio, school, or work projects. These tools and techniques are versatile.

## The Key Stakeholders

There are many different stakeholders when it comes to a successful deployment.

- Users - the most important stakeholder, your model needs to do what they expect and be easy and clear for them to use.
- Business Leaders - their stake is driven by the value derived from your model.
- DevOps Engineers - not always present depending on the size of company/team, but you may need to work with them to deploy your model and their stake is in a successful (and smooth!) deployment.
- Colleagues - if you worked in collaboration with other data scientists or machine learning engineers than they are as invested as you in successful deployment.
- Yourself - you're a stakeholder in both the success of the deployment but also in the process. Sometimes doing things properly takes extra time, but your future self will thank you.

## History of Deploying an ML Pipeline

Machine Learning Operations (MLOps) is the marriage between machine learning and the tools and techniques necessary to deploy and maintain machine learning products, i.e. the combination of machine learning and DevOps. MLOps had its genesis within the past decade and is still a rapidly emerging discipline with growing importance.

Additional Resources

- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) published in 2015.

## When to Deploy an ML Pipeline

When to deploy a model is easy. You deploy it once it is done which includes testing the performance, checking for bias, and writing a model card. The challenge is in how to deploy. The specific approach will depend on the tools available to you and the problem at hand. Some task are naturally suited for batch deployment, whereas others need to be live.

To make your life easy, always write your code with an eye towards deployment.

### Pre Deployment Checklist

Checklists are a powerful tool in the data scientists arsenal. Here is a checklist of some steps you should follow before deploying a model.

1. Test performance overall
2. Test performance on key slices
3. Check for bias
4. Write a model card

