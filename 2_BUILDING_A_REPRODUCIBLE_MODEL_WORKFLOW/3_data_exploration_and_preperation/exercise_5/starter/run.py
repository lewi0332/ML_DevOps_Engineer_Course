#!/usr/bin/env python
import argparse
import logging
import pandas as pd
import wandb

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    with wandb.init(project="exercise_5", job_type="process_data") as run:
        logger.info("Importing parquet file from W&B")
        artifact = run.use_artifact(args.input_artifact)
        df = pd.read_parquet(artifact.file())
        
        logger.info("Dropping duplicates")
        df.drop_duplicates().reset_index(drop=True)
        
        logger.info("Creating text feature")
        df['title'].fillna(value='', inplace=True)
        df['song_name'].fillna(value='', inplace=True)
        df['text_feature'] = df['title'] + ' ' + df['song_name']
        
        logger.info("Storing artifact locally")

        df.to_csv("clean_data.csv")

        logger.info("Adding Artifact to Run")
        artifact = wandb.Artifact(
            name=args.artifact_name,
            type=args.artifact_type,
            description=args.artifact_description,
        )
        artifact.add_file("clean_data.csv")

        logger.info("Logging artifact with W&B")
        run.log_artifact(artifact)
        




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Preprocess a dataset",
        fromfile_prefix_chars="@",
    )

    parser.add_argument(
        "--input_artifact",
        type=str,
        help="Fully-qualified name for the input artifact",
        required=True,
    )

    parser.add_argument(
        "--artifact_name", type=str, help="Name for the artifact", required=True
    )

    parser.add_argument(
        "--artifact_type", type=str, help="Type for the artifact", required=True
    )

    parser.add_argument(
        "--artifact_description",
        type=str,
        help="Description for the artifact",
        required=True,
    )

    args = parser.parse_args()

    go(args)
