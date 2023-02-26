Udacity Machine Learning DevOps Engineering Course
===============

[Nanodegree Program - Machine Learning DevOps Engineer](https://www.udacity.com/course/machine-learning-dev-ops-engineer-nanodegree--nd0821)

This repository covers the coursework building DevOps skills required to automate the various aspects and stages of machine learning model building and monitoring.

The course covered 4 core topics to prepare machine learning code for production in a scalable real-world environments.

<img src=certificate.png width="350">

---

## Module 1. - Clean Code Principles

Document skills that are essential for deploying production machine learning models. First, set coding best practices by utilizing PyLint and AutoPEP8. Further, expand git and Github skills to work with teams. Finally, explore best practices associated with testing and logging used in production settings in order to ensure models can stand the test of time.

[Notes and Lessons - Clean Code Prinicipals and Logging](1_CLEAN_CODE_PRINCIPLES)

>### Project 1 - Project Predict Customer Churn with Clean Code
>
>In this project, you will implement your learnings to identify credit card customers that are most likely to churn. The completed project will 
>include a Python package for a machine learning project that follows coding (PEP8) and engineering best practices for implementing software 
>(modular, documented, and tested). The package will also have the flexibility of being run interactively or from the command-line interface 
>(CLI). This project will give you practice using your skills for testing, logging, and coding best practices from the lessons. It will also 
>introduce you to a problem data scientists across companies face all the time: How do we identify (and later intervene with) customers who are >likely to churn?
>
>[PROJECT REPOSITORY - Clean Code Project](https://github.com/lewi0332/ML_DevOps_Clean_Code_Principles)

---

 ## Module 2. - Building a Reproducible Model Workflow

This course empowers the students to be more efficient, effective, and productive in modern, real-world ML projects by adopting best practices around reproducible workflows. In particular, it teaches the fundamentals of MLops and how to: a) create a clean, organized, reproducible, end-to-end machine learning pipeline from scratch using MLflow b) clean and validate the data using pytest c) track experiments, code, and results using GitHub and Weights & Biases d) select the best-performing model for production and e) deploy a model using MLflow. Along the way, it also touches on other technologies like Kubernetes, Kubeflow, and Great Expectations and how they relate to the content of the class.

[Notes and Lessons - Tracking and Reproducing Model Workflow](2_BUILDING_A_REPRODUCIBLE_MODEL_WORKFLOW)

<p align="center">
<img src=2_BUILDING_A_REPRODUCIBLE_MODEL_WORKFLOW/5_training_validaion_and_experiment_tracking/images/flowchart.png width="550">
</p>

>### Project 2 - Build an ML Pipeline for Short-term Rental Prices in NYC
>
>Students will write a Machine Learning Pipeline to solve the following problem: a property management company is renting rooms and properties in >New York for short periods on various rental platforms. They need to estimate the typical price for a given property based on the price of 
>similar properties. The company receives new data in bulk every week, so the model needs to be retrained with the same cadence, necessitating a >reusable pipeline. The students will write an end-to-end pipeline covering data fetching, validation, segregation, train and validation, test, >and release. They will run it on an initial data sample, and then re-run it on a new data sample simulating a new data delivery.
>
>[PROJECT REPOSITORY - Short Term Rental Prices Project](https://github.com/lewi0332/ML_DevOps_build_ml_pipeline_for_short_term_rental_prices)

---

## Module 3. - Deploying a Scalable ML Pipeline in Production

This course teaches students how to robustly deploy a machine learning model into production. En route to that goal students will learn how to put the finishing touches on a model by taking a fine grained approach to model performance, checking bias, and ultimately writing a model card. Students will also learn how to version control their data and models using Data Version Control (DVC). The last piece in preparation for deployment will be learning Continuous Integration and Continuous Deployment which will be accomplished using GitHub Actions and Heroku, respectively. Finally, students will learn how to write a fast, type-checked, and auto-documented API using FastAPI.

[Notes and Lessons - Deploying a Scalable ML Pipeline in Production](3_DEPLOYING_A_SCALABLE_ML_PIPELINE)

>### Project 3 - Deploying a Machine Learning Model on Heroku with FastAPI
>
>In this project, students will deploy a machine learning model on Heroku. The students will use Git and DVC to track their code, data, and model >while developing a simple classification model on the Census Income Data Set. After developing the model the students will finalize the model >for production by checking its performance on slices and writing a model card encapsulating key knowledge about the model. Students will put >together a Continuous Integration and Continuous Deployment framework and ensure their pipeline passes a series of unit tests before deployment. >Lastly, an API will be written using FastAPI and will be tested locally. After successful deployment the API will be tested live using the >requests module.
>
>After completion, the student will have a working API that is live in production, a set of tests, model card, and full CI/CD framework. On its 
>own, this project can be used as a portfolio piece, but also any of the constituent pieces can be applied to other projects, e.g. continuous i
>integration, to further flesh them out.
>
>[PROJECT REPOSITORY - Continuous Integration and Continuous Deployment with Github Actions and Heroku](https://github.com/lewi0332/ML_DevOps_Deploying_a_Machine_Learning_Model)

---

## Module 4. - Automated Model Scoring and Monitoring

This course will help students automate the devops processes required to score and re-deploy ML models. Students will automate model training and deployment. They will set up regular scoring processes to be performed after model deployment, and also learn to reason carefully about model drift, and whether models need to be retrained and re-deployed. Students will learn to diagnose operational issues with models, including data integrity and stability problems, timing problems, and dependency issues. Finally, students will learn to set up automated reporting with API’s.

[Notes and Lessons - Automated Model Scoring and Monitoring](4_MODEL_SCORING_AND_MONITORING)

>### Project 4 - Client Attrition Risk Assessment
>
>In this project, students will make predictions about attrition risk in a fabricated dataset. They’ll set up automated processes to ingest data >and score, re-train, and re-deploy ML models that predict attrition risk. They’ll write scripts to automatically check for new data and check >for model drift. They’ll also set up API’s that allow users to access model results, metrics, and diagnostics. After completing this project, >students will have a full end-to-end, automated ML project that performs risk assessments. This project can be a useful addition to students’ 
>portfolios, and the concepts they apply in the project can be applied to business problems across a variety of industries.

>[PROJECT REPOSITORY - Automated Model Scoring and Monitoring](https://github.com/lewi0332/ML_DevOps_ML_Model_Scoring_and_Monitoring)

---

