# Machine Learning Pipelines

**Introduction**

In this lesson, we concern ouseleves with machine Learning Pipleins, including:
- What is a ML pipeline and why it is useful
- The thress levels of MLops
- A refression on using `argparse`
- Versioning data and artifacts with Weights and Biases
- ML pipeline Components in MLflow
- Linking togethere the components into a pipeline
- Conda vs Docker

A Machin Learning pipeline is made of:

- Components (or steps): independent, reusabel and modular pieces of software that receive one or more imputes and produce one or more output. The cand be scripts, notebooks or other executables.
- Artifacts: the product of components. They can become the inputs of one or more subesquent components, thereby linking together the steps of the pipeline. Artifacts must be tracked and versioned. 

This is a example of a simple ML pipeline (in this case, an ETL pipeline):

![ETL pipeline](./images/etl-pipeline.png)

### Why Use ML Pipelines: The 3 Levels of MLops

We will see now the 3 levels of MLops and their use. The basics of the classification is taken from this document by Google Cloud. We will be adding some context and several details to make clearer its application in practice.

**Level 0**

This is the level where there is no MLops process. It is ok for personal projects, when learning something new, or for demos and MVPs. In all these cases the overhead of a proper MLops process might be sacrificed because of deadlines and time budget. The main features of this stage are:

- The code is monolithic - one or few scripts or Jupyter notebooks, with limited reusability
- The target of the development is a model, and not a ML pipeline (we will see later what this means)
- There is limited concern for production during development, hence the model needs to be reimplemented for production, maybe by a different team
- No awareness of the need for model monitoring and retraining

### Levels 1 & 2

**Level 1**

As soon as you are past the proof of concept stage and you are targeting production, you should consider a more mature process, starting with level 1. These are its features:

- The target of the development is a ML pipeline that can produce a model at any time. This makes it easy to re-train on new data, for example.
- The pipeline is made with reusable components
- You are tracking code, artifacts and experiments for reproducibility and transparency
- The output of the ML pipeline is an inference artifact that contains the pre-processing steps, so these do not need to be reimplemented for production (more on this later)
- The model is monitored in production

With respect to level 0, level 1 produces the following advantages:

- Process standardization
- Rapid prototyping
- Faster go-to-market with new products
- Avoid model drift

**Level 2**

This is the process for mature, large scale ML companies. Here we shift our focus from developing ML pipelines to improving the pipeline components. This assumes we already have several ML pipelines in production. The automation at this level is much higher, and we have processes for:

- Continuous integration: every time a component is changed integration tests are run to ensure that the component works as expected
- Continuous deployment: each component passing the tests is automatically deployed and starts running as part of the ML pipelines in production
- Continuous Training: when a component changes or when new data arrives the ML pipelines are triggered and new models are trained, tested and deployed automatically

With respect to level 1, level 2 features:

- Rapid iteration on prod pipelines and models
- Easy A/B testing of changes
- Easy collaboration and improvements across large teams
- Continuous improvements in production. The customer sees a continuously-improving product

![feature grid of level of mlops](./images/level-comparison.png)

## Versioning Data and Artifacts 
- Using Weights and Biases [wandb.ai](https://wandb.ai/site)

In Weights & Biases (and in many other tools) we have the following concepts:

- **Run**: the basic unit of computation, it usually corresponds to the execution of one script or of one Jupyter notebook, although multiple runs per script/notebook are possible. In W&B each run is assigned automatically a unique name (like `sunny-spring-21`), unless you force a specific name using the `name` keyword of `wandb.init` (we will only use automatic names in this class). You can attach to a run:
- - parameters
- - metrics
- - artifacts
- - images / plots
- **Experiment**: a group of one or more runs. For example, we can collect the execution of one entire pipeline into one experiment: each component will have its own run, but all the runs are grouped into one experiment. Experiments can be compared to each other in the W&B interface just like runs. All the metrics collected by all runs become metrics of the experiment. In W&B the experiment name is indicated by the optional `group` keyword of `wandb.init`. If you do not specify a group (i.e., an experiment name) the run will be ungrouped, i.e., will not belong to any experiment (but still belong to its project).
- **Project**: a heterogeneous collection of all runs, experiments, and artifacts related to a specific goal. A project collects all the work related to the same objective. W&B allows one to look at one project at a time.
- **Artifact**: any file or directory produced by our code during a run. Every artifact that is logged to a run is automatically versioned by W&B. For example, if two runs produce an artifact with the same name (say a file named `model.h5`) but the content of the file is different, W&B will generate two versions (for example v1 and v2). On the contrary, if two runs produce the exact same file (same name and same content), W&B will recognize this and will NOT generate a new version.

Optionally you can specify a `job_type` for each run. This is useful when visualizing your pipeline. Normally the job_type express the function of your script, for example `data_cleaning` or `preprocessing` or `model_training`.

When using W&B you can start a run in this way:

```
import wandb

wandb.init(
    project="my_project",
    group="experiment_1",
    job_type="data_cleaning"
)

```
Supporting Materials

> [Upload_And_Version_Artifacts.ipynb](https://video.udacity-data.com/topher/2021/June/60c30f1a_upload-and-version-artifacts/upload-and-version-artifacts.ipynb)


## Write a ML Pipeline Component with MLflow

An MLflow project is a package of data science code that is reusable and reproducible. Projects can be chained together into workflows. We are going to use MLflow projects to define our components and chain them together in ML pipelines.

An MLflow project is made of 3 parts:

1. Code: the code that we want to use
2. Environment definition: specifies the dependencies of our code
3. Project definition: it specifies what is contained in the project and how a user should interact with the project

**The code**

The code here can be anything we want. It can depend on other packages, which will be specified in the environment definition. It is important to note that the code can be in any language, not just Python. So for example we can write components in Julia, R, Bash, Go or anything else. When putting together pipelines, we can even mix and match components written in different languages.

**Environment definition (`conda.yml`)**

MLflow allows to define the dependencies of our code (i.e., the runtime environment) using either conda or Docker. In the class we will focus mainly on conda, although we will see at a high level how to use docker as well.

Conda is a language-agnostic package manager that supports Linux, Mac OSX and Windows. Its scope is much larger than pip, which is limited to Python. Indeed, Conda is much more similar to other package managers like apt, yum or brew, however it is multi-platform.

For more information see [this blog post](https://towardsdatascience.com/conda-essential-concepts-and-tricks-e478ed53b5b).

A conda environment for an MLflow project is defined by a YAML file (if you are not familiar with YAML, see the quick introduction at the bottom of the page). This file is typically called `conda.yml` and has the following structure:

```
name: download_data
channels:
  - conda-forge
  - defaults
dependencies:
  - requests=2.24.0
  - pip=20.3.3
  - mlflow=1.14.1
  - hydra-core=1.0.6
  - pip:
      - wandb==0.10.21
```

The `name` section specifies the environment name (this can be anything). The `channels` section lists the channels where the `dependencies` will be looked up (in order). Then the dependencies section lists the dependencies. You should always also indicate the full version you need, in order to ensure reproducibility. If you need packages that are not available in the conda channels, but are available in pip, you can add a `pip` section and list there the `pip` dependencies.

NOTE: for conda packages the version is indicated by one equal sign, like `=2.24.0`, while for `pip` packages you have to use two equal signs, like `==0.10.21`.

**Project definition (`MLproject`)**

The project definition is contained in a YAML file called `MLProject` (without `.yml` nor `.yaml` extension). This file has the following structure:

```
name: download_data
conda_env: conda.yml

entry_points:
  main:
    parameters:
      file_url:
        description: URL of the file to download
        type: uri
      artifact_name:
        description: Name for the W&B artifact that will be created
        type: str

    command: >-
      python download_data.py --file_url {file_url} \
                              --artifact_name {artifact_name}
  other_script:
    parameters:
        parameter_one:
          description: First parameter
          type: str
    command: julia other_script.jl {parameter_one}
```

The `name` section specifies the name for the environment in which this code will be executed. It is not really important. Then the `conda_env: conda.yml` section specifies that this is a conda-based project (as opposed to a Docker-based project). Finally, the most important section, the `entry_points` section. This lists all the available scripts and commands that the user can run. This section MUST always have a `main` key which specifies the default script to run, and can optionally have other entry points (in our example, the `other_script` entry point). For each entry point we have the `parameters` section and the `command` section, specifying respectively the parameters for the command and how to run the command.

**Running the Project**

Running a MLflow project is accomplished with the mlflow run command, followed by a location specifier. A location can be a local path:

```
mlflow run /path/to/the/local/folder
```

or a remote Git repository:

```
mlflow run git@github.com/my_username/my_repo.git
```

Paremeters are specified using `-P [parameter_name]=[paremeter value]`. You will need to specify one `-P` option for each parameter. For example, to specify a parameter `file_url` and a parameter `artifact_name` you can do:

```
mlflow run ./by_project -P file_rul=https://myurl.com -P artifact_name=my-artifact
```

When running from a remote Git repository, you can specify a release or branch by using the -v option. For example, to run version `1.2.3` you can do:

```
mlflow run git@github.com/myusername/my_repo.git -b 1.2.3
```
