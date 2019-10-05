lambda-mysql-runner
===================

A Python-based [AWS Lambda](https://aws.amazon.com/lambda/) function to run [MySQL](https://www.mysql.com/) commands given in input, mainly intended for performing database creation and similar administration tasks.

Deployment
----------

- Get the distribution package
  - from the [releases page](https://github.com/rrobby86/lambda-mysql-runner/releases)
  - building it in an Amazon Linux environment, e.g. an EC2 instance, Docker image or [CodeBuild](https://aws.amazon.com/codebuild/) (build specification is included in the repository)
- Use AWS console or CLI to create a Lambda function based on the package, setting
  - runtime: `python3.7`
  - handler function: `func.handler`
  - IAM execution role, VPC, ... appropriately for your use case

Usage
-----

The input `event` to the function must be an object with (at least) the following entries:
- `connection`: an object providing connection parameters passed to the `connect` function
- `commands`: either an array of single commands or a string with multiple semicolon-separated commands (run with `multi=True`)
- `parameters` (optional): an object with key-value mappings which can be referenced in commands using Python's [format string syntax](https://docs.python.org/3/library/string.html#formatstrings), useful to avoid repetitions and for easier integration with [AWS Step Functions](https://aws.amazon.com/step-functions/)

Example input:

    {
      "connection": {
        "host": "blah.blah.blah.rds.amazonaws.com",
        "database": "mysql",
        "user": "root",
        "password": "blah"
      },
      "commands": [
        "create database `{thedb}`",
        "grant all on `{thedb}`.* to theboss",
        "grant select on `{thedb}`.* to reader"
      ],
      "parameters": {
        "thedb": "your-db-here"
      }
    }
