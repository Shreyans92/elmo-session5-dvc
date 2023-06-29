# ELMO_session_4
# Lightning Template

```
copper_train --help
```

examples

- `copper_train data.num_workers=16`
- `copper_train data.num_workers=16 trainer.deterministic=True +trainer.fast_dev_run=True`

## Development

Install in dev mode

```
pip install -e .
```

# Run with docker

Build the image

```
docker build --tag cifar:latest .
```

Train the model with docker run

```
docker run -it cifar:latest python dummypackage/train.py +experiment=cifar10_example
```

Evalate model

```
docker run -it cifar:latest python dummypackage/eval.py +experiment=cifar10_example
```


# Run in DevContainer

### To train the model in devContainer

First, update PYTHONPATH for the environment
```
export PATH="$PATH:/workspaces/project-setup/dummypackage
export PATH="$PATH:/workspaces/project-setup
```
Now, train the model
```
python3 dummypackage/train.py 
```

### To evaluate the model in devContainer

```
python3 dummypackage/eval.py 
```
