# MLOPS-DVC-PROJECT-IMPLEMENTATION
This project covers the end to end understanding for creating an ML pipeline  and  working it using DVC for experiment tracking and data versioning using AWS S3

# Pipeline Tracking & Versioning


- Create a Github repo and clone it in local. 
- add src floder along with all components like data_ingestion, preprocessing, model buliding etc. 
- Adding data, models, reports to .gitignore file. 

### Setting up dvc pipeline
- add params.yaml file
- add the params setup in yaml format for pipeline tracking configuraion. 

```bash
# To initialize the dvc
dvc init 
# pipeline reproducibility
dvc repro 

Then git add . and git commit, push. 
```
### Dvc exp run for experiment tracking 

```bash
pip install dvclive
```
- Add the dvclive code block 
```bash

## it will create a new dvc.yaml(if already not there) and dvclive directory (each run will be considered as an experiment by dvc))
dvc exp run 

# it shows all the experiment which perfomed previously
dvc exp show 

dvc exp remove {exp_name} to remove experiment from dvc

git add, commit, push. 
```

### Adding a remote S3 storage to DVC
- Login to AWS console. 
- create an IAM user 
- create s3 
```bash
pip install awscli

pip install dvc[s3]

aws configure (using access key)

dvc remote add -d dvcstore s3://bucketname (create default remote storage in Aws s3 bucket)

dvc commit 

dvc push (send all tracking versioning in s3 bucket)
```




