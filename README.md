# AWS Lambda CI/CD Deployment with GitHub Actions

This project automates the deployment of an AWS Lambda function using GitHub Actions. Every push to the main branch will trigger a pipeline that zips the code and deploys it to AWS Lambda.
if successful, the pipeline will trigger an email notification via AWS SNS.

## Steps to Set Up

### 1. Create a New Lambda Function in AWS Console
- In the AWS Management Console, navigate to Lambda and create a new Lambda function.
- Use Python as the runtime and copy the default code.
- Replace the default code with the code you want to deploy.
- Save the function and make a note of the function name.
- Create an IAM role with the necessary permissions for the Lambda function.
- Attach the IAM role to the Lambda function.
- Create an SNS topic and subscribe to it using your email address.
- Copy the ARN of the SNS topic.
- Create an environment variable in the Lambda function with the key `SNS_TOPIC_ARN` and the value as the ARN of the SNS topic.
- Test the Lambda function to make sure it works.
- make sure you set up all repository secrets as shown in .env_example file:
```bash
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_LAMBDA_ARN=your_lambda_arn
AWS_SNS_ARN=your_sns_arn
AWS_REGION=your_lamda_region
```

### 2. Set Up the Project Locally
- Create a folder for your project.
- Inside the folder, create a file named `lambda_function.py` and paste the code you used in the AWS Console.

### 3. Initialize a Git Repository
```bash
git init
git remote add origin <your-repo-url>