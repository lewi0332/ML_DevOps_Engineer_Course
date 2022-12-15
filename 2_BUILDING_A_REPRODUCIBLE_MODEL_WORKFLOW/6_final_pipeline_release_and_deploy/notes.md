# Final Pipeline, Release and Deploy

Bringing together everything we learned and build an end-to-end ML pipeline. We are also going to see options for deploying our inference artifact.

You'll learn:

- How to bring everything together in a end-to-end ML pipeline
- How to release the code in GitHub, and how to assign version numbers using Semantic Versioning
- What is deployment, and how to deploy our inference artifact with MLflow and other tools for both online (real-time) and offline (batch) inference

MLflow pipelines are code, and the code needs to be versioned. We have two options:

1. Collect all our pipeline, including the main script, its `conda.yml`, and its `MLproject` file as well as all the components with their `conda.yml`, their code and their `MLproject` files in the same repository. This is simple and good to start with.
2. Have separate repositories: one for the pipeline (the main script as well as the relative `conda.yml` and `MLProject`) and a separate one for the components. This promotes reusability and discoverability, because all the components of different pipelines are collected together in the same place where can be discovered, modified, released and versioned. This is what you need when you are scaling up and you have several ML pipelines. It is also a preliminary step for Level 2 MLops.

In this class we are going to use `git` to track our code. This is a cheatsheet you can use (or see the more extensive version [here](https://about.gitlab.com/images/press/git-cheat-sheet.pdf)):

![git cheat sheet with common commands](./images/git-cheatsheet.png)

## Release for Reproducibility

A release is a static copy of the code that reflects the state of the code at a particular point in time. It has a version attached to it, and a tag. The tag can be used to restore the repository (or a local copy of the code in the repository) to the state it was when the release was cut.

A common schema for versioning release is called Semantic Versioning: a release is made of 3 numbers, like 1.3.8. The first number is called the major version. We only increment the major version when we are making changes that break backward compatibility (i.e., a code that was running with the previous version is likely to break with the new version). The second number is called minor. We increment it when we make a significant change that is backward-compatible, i.e., code that was running with the previous version is not expected to break with the new one. And finally, we have a path number. We increment it for bug fixes and small changes that do not significantly change the behavior of the code (excluding the bugs fixed).

![versioning explanation](./images/semantic-versioning.png)

## Deploy with MLflow

This is a schematic representation of the workflow that brings a model to production:

![Deployment dag](./images/deployment.png)

The ML pipeline produces the inference artifact. The inference artifact is stored in the Model Repository, which for us is the Artifact tracking solution of W&B. On the serving side, a manual or an automatic process fetches the inference artifact from the model repository and deploys it to the production system, alongside the other models that have been already deployed. From now on, the production system receives requests and the response includes the newly-deployed model. The deployment step is the point of contact between the development world, typically the responsibility of data scientists, and the serving world, typically the responsibility of software and platform engineers. It is also an interface where the focus changes from experimentation and performance to standardization, speed and reliability. Most of the production problems not related to model performance happen at this interface.

There are two ways of using a model in production: Real-time and Batch.

**Real-time (online)**

Here, we are interested in providing answers one at the time, typically through an API. Most of the time the performance metric that matters here is latency, i.e., the time needed to process one entity (from request to answer). An example of a real-time inference application is providing movie recommendations on a website: we want to provide the answer as quickly as possible, so that the user is not left hanging waiting for the page to load.

**Batch (offline)**

Here, we are receiving several requests at once (a batch), and we want to process the entire batch in the shortest possible time. Therefore, our metric of reference here is throughput, i.e., the amount of requests per unit time that we can process. We are willing to sacrifice latency if that means that we can process more requests, in say, a second. For example, when we have a deep learning model on a GPU, we might wait until we accumulate a certain number of requests, and then send the entire batch to the GPU. Therefore, the latency for the first request that we receive will be pretty large because this request will hang until other requests are received.

**Use MLflow for serving models**

Let's consider batch processing first. MLflow allows you to use any artifact exported with MLflow for batch processing.

**Demo: Offline Inference**

For example, let's fetch an inference artifact from one of the previous exercises using wandb:

```
> wandb artifact get genre_classification_prod/model_export:prod --root model
```

The `--root` option sets the directory where wandb will save the artifact. So after this command we have our MLflow model in the model directory. We can now use it for batch processing by using mlflow models predict:

```
> mlflow models predict -t json -i model/input_example.json -m model
```

where `input.csv` is a file containing a batch of requests, -t indicates the format of the file (csv in this case), and -m model specifies the directory containing the model.

**Online Inference**

We can serve a model for online inference by using `mlflow models serve` (we assume we already have our inference artifact in the `model` directory):

```
> mlflow models serve -m model --env-manager conda &
```

Mlflow will create a REST API for us that we can interrogate by sending requests to the endpoint (which by default is `http://localhost:5000/invocations`). For example, we can do this from python like this:

```
import requests
import json

with open("data_sample.json") as fp:
    data = json.load(fp)

results = requests.post("http://localhost:5000/invocations", json=data)

print(results.json())
```

## Other Options for Deployment

Inference artifacts in the "MLflow models" format can be used with several tools beyond MLflow itself. Some examples are:

- Spark for offline inference (see the [mlflow documentation](https://www.mlflow.org/docs/latest/models.html#export-a-python-function-model-as-an-apache-spark-udf))
- Online inference with [Seldon Core](https://docs.seldon.io/en/latest/), [Algorithmia](https://algorithmia.com/developers/clients/mlflow), and any tool that supports pure-python inference functions (like [BentoML](https://www.bentoml.ai/), [cnvrg.io](https://cnvrg.io/), [valohai](https://valohai.com/), [clearML](https://clear.ml/), and more). You can also [dockerize your MLflow](https://www.mlflow.org/docs/latest/cli.html#mlflow-models-build-docker) API and deploy it directly as a REST API, such as in Kubernetes.



## Glossary 

**Release**: A static copy of the code that reflects the state at a particular point in time. It has a version attached to it, and a tag. The tag can be used to restore the repository (or a local copy of the code in the repository) to the state it was when the release was cut.

**Semantic Versioning:** A common schema for versioning releases. A release version is made of 3 numbers, like 1.3.8, called respectively major, minor, and patch. The major number should be incremented for large, backward-incompatible changes. The minor number should be incremented when new features are added in a backward-compatible way. The patch number should be incremented for bug fixes and other small backward-compatible changes.

**Deployment**: The operation of taking an inference artifact and putting it into production, so it can serve results to stakeholders and customers.

![Full pipeline roadmap](./images/ml-devops-c2-outline.png)