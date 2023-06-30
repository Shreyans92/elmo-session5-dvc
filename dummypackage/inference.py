from typing import Tuple, Dict
import lightning as L
import torch
import hydra
from omegaconf import DictConfig

from dummypackage import utils

log = utils.get_pylogger(__name__)


#@utils.task_wrapper
def inference(cfg: DictConfig) -> Tuple[dict, dict]:
    # set seed for random number generators in pytorch, numpy and python.random
    if cfg.get("seed"):
        L.seed_everything(cfg.seed, workers=True)

    log.info(f"Instantiating datamodule <{cfg.data._target_}>")
    datamodule: LightningDataModule = hydra.utils.instantiate(cfg.data)

    log.info(f"Instantiating model <{cfg.model._target_}>")
    model: LightningModule = hydra.utils.instantiate(cfg.model)


    log.info(f"Instantiating trainer <{cfg.trainer._target_}>")
    trainer: Trainer = hydra.utils.instantiate(cfg.trainer)


    log.info("Starting Prediction!")
    preds = trainer.predict(model=model, datamodule=datamodule, return_predictions = True,  ckpt_path=cfg.ckpt_path)
    log.info(f"Prediction Values <{preds}>")
    return preds


@hydra.main(version_base="1.3", config_path="../configs", config_name="infer.yaml")
def main(cfg: DictConfig):
    # Run inference on the model
    predictions = inference(cfg)

    for i in predictions:
        cat_prob = i[0][0] 
        dog_prob = i[0][1]
    
    prob_json = {'Cat': cat_prob, 'Dog': dog_prob} 
    print(prob_json)


if __name__ == "__main__":
    main()