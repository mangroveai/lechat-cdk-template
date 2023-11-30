# Databricks IaC

Project that provides the landing infrastructure for databricks workspace creation.

## Projet Setup

The python version of this project is 3.8 or further. To deploy the project you will just have to do:

1 - Install Poetry.

```
$ curl -sSL https://install.python-poetry.org | python3 -
```

For macOS ( using brew )

```
$ brew install poetry
```

2 - Install the required libraries.

```
$ poetry install
```

3 - Activate the virtual environment.

```
$ poetry shell
```


4 - At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk bootstrap
```


4 - At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

5 - To deploy the project

```
$ cdk deploy
```

## Useful commands

- `cdk ls` list all stacks in the app
- `cdk synth` emits the synthesized CloudFormation template
- `cdk deploy` deploy this stack to your default AWS account/region
- `cdk diff` compare deployed stack with current state
- `cdk docs` open CDK documentation
