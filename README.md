# AWS Lambda CI/CD Deployment with GitHub Actions

This project automates the deployment of an AWS Lambda function using GitHub Actions. Every push to the main branch will trigger a pipeline that zips the code and deploys it to AWS Lambda.

## Steps to Set Up

### 1. Create a New Lambda Function in AWS Console
- In the AWS Management Console, navigate to Lambda and create a new Lambda function.
- Use Python as the runtime and copy the default code.

### 2. Set Up the Project Locally
- Create a folder for your project.
- Inside the folder, create a file named `lambda_function.py` and paste the code you used in the AWS Console.

### 3. Initialize a Git Repository
```bash
git init
git remote add origin <your-repo-url>