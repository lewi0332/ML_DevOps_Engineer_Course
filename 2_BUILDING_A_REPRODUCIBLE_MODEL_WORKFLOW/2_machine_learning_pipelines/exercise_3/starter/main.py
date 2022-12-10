import mlflow
import os
import hydra
from omegaconf import DictConfig


# This automatically reads in the configuration
@hydra.main(config_name='config')
def go(config: DictConfig):

    # Setup the wandb experiment. All runs will be grouped under this name
    os.environ["WANDB_PROJECT"] = config["main"]["project_name"]
    os.environ["WANDB_RUN_GROUP"] = config["main"]["experiment_name"]

    # You can get the path at the root of the MLflow project with this:
    root_path = hydra.utils.get_original_cwd()

    _ = mlflow.run(
        uri=os.path.join(root_path, "download_data"),
        entry_point="main",
        parameters={
            "file_url": config["data"]["file_url"],
            "artifact_name": "iris.csv",
            "artifact_type": "raw_data",
            "artifact_description": "Input data"
        },
    )
    
    _ = mlflow.run(
        uri=os.path.join(root_path, "process_data"),
        entry_point='main',
        parameters={
            "input_artifact": "iris.csv:latest",
            "artifact_name": "cleaned_data",
            "artifact_type": "clean_data",
            "artifact_description": "2d tsne"
        }
    )

if __name__ == "__main__":
    go()
