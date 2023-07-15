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
## Result

### AIM Run
![multirun for patch size ]
