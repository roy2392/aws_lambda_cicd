# AWS Lambda CI/CD with GitHub Actions

[![CI/CD Status](https://github.com/your-username/your-repo/actions/workflows/Deploy%20Lambda.yml/badge.svg)](https://github.com/your-username/your-repo/actions)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)

## Overview

This project provides a seamless, automated CI/CD pipeline for deploying a Python-based AWS Lambda function using GitHub Actions. With every push to the `main` branch, the pipeline is triggered, which automatically zips your code and deploys it to AWS Lambda. Upon a successful deployment, an email notification is sent via AWS SNS to keep you informed.

This setup is designed to be straightforward, reliable, and efficient, allowing you to focus on writing code while the deployment process is handled for you.

## Why Star This Repo?

- **Automated Deployments**: Set up once and let GitHub Actions handle the rest.
- **Easy to Configure**: A few simple steps are all it takes to get up and running.
- **Reliable and Fast**: Built on industry-standard tools to ensure a smooth workflow.
- **Notifications**: Stay updated on your deployment status with SNS notifications.
- **Beginner-Friendly**: Ideal for developers new to CI/CD or AWS Lambda.

## Setup Instructions

### 1. AWS Setup

- **Create a Lambda Function**: In the AWS Management Console, create a new Lambda function with a Python runtime.
- **IAM Role**: Create an IAM role with permissions for Lambda and SNS, and attach it to your function.
- **SNS Topic**: Create an SNS topic and subscribe your email to receive notifications.
- **Environment Variable**: In your Lambda function's configuration, add an environment variable `SNS_TOPIC_ARN` with the ARN of your SNS topic.

### 2. GitHub Repository Secrets

To allow GitHub Actions to deploy to your AWS account, you need to configure the following secrets in your repository settings:

- `AWS_ACCESS_KEY_ID`: Your AWS access key ID.
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.
- `AWS_LAMBDA_ARN`: The ARN of your Lambda function.
- `AWS_SNS_ARN`: The ARN of your SNS topic.
- `AWS_REGION`: The AWS region where your resources are located (e.g., `us-east-1`).

You can find a template for these secrets in the `.env_example` file.

### 3. Local Project Setup

- **Clone the Repository**: 
  ```bash
  git clone https://github.com/your-username/your-repo.git
  cd your-repo
  ```
- **Customize the Lambda Function**:
  - Open `src/lambda_function.py` and add your desired logic.

### 4. Push to Deploy

Once your changes are ready, commit them and push to the `main` branch:

```bash
git add .
git commit -m "Update Lambda function"
git push origin main
```

Your deployment will be automatically triggered.
