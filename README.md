# EMLOv3 | Data Version Control


This repo is based on the [ELMO Lightning](https://github.com/Shreyans92/ELMO_lightening) repo with additional feature of data version control. The package created is named as dummypackage.

Here are the instructions to use it with added DVC.

## DVC Setup

1. Make a data folder and put all your data in Data folder.

2. Add DVC to Data:

```bash
 dvc add data
```
> Note: If the data is getting tracked by git, run the following commands:
```bash
   git rm -r --cached 'data'
   git commit -m "stop tracking data"
```

3. Using Local Storage to add data, run the following command:

```bash
dvc remote add -d local <local-path>
```

4. Push the data to remote, run the following command:

```bash
dvc push -r local
```

5. Pull the data from remote storage, run the following command:

```bash
dvc pull -r local
```

## Prediction

To predict model outcome on a single image, run the following command:

```bash
dummy_infer
```

> Note: Keep the single image in respective class folder as Imagefolder package from toch has been used.

The output of above command is class probability, in this case classes are {Cat,Dog}.The output is shown below:

```bash
{'Cat': 0.6777524352073669, 'Dog': 0.32224759459495544}
```
