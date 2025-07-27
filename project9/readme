AWS Infrastructure Provisioning with Terraform
Overview
This project demonstrates how to provision a complete cloud infrastructure for a web application on AWS using Terraform. It covers the creation of a secure, scalable environment with networking, compute, database, domain management, storage, and serverless components.

Architecture
(You can add a diagram later)

The infrastructure includes:

VPC with public and private subnets.

EC2 Instance in a private subnet for the web application.

RDS PostgreSQL Database in the private subnet (with encryption).

Security Groups for secure traffic management (HTTP/SSH access + internal communication).

IAM Role for EC2 with read access to an encrypted S3 bucket.

Route 53 custom domain for the web application.

AWS Lambda function interacting with the RDS database.

API Gateway with REST API integrated with the Lambda function.

Terraform Resources
1. Networking
VPC, Internet Gateway, NAT Gateway

Two subnets:

Public subnet (web and internet-facing resources)

Private subnet (EC2, RDS, Lambda)

Route tables for proper routing between components

2. Compute & Database
EC2 instance deployed in the private subnet

RDS PostgreSQL instance with storage and backup encryption enabled

3. Security
Security groups allowing:

HTTP (80) and SSH (22) from anywhere

Internal communication between EC2, RDS, and Lambda

IAM role for EC2 with policy allowing S3 read access

4. Domain & Storage
S3 bucket for storage (with encryption enabled)

Route 53 custom domain pointing to the EC2 instance

5. Serverless Components
Lambda function interacting with the RDS database

API Gateway with REST API routing external requests to Lambda

How to Deploy
Prerequisites
AWS account with appropriate permissions

Terraform installed (v1.5+ recommended)

Configured AWS CLI credentials

Steps
Clone the repository:

bash
Copy
Edit
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
Initialize Terraform:

bash
Copy
Edit
terraform init
Preview the changes:

bash
Copy
Edit
terraform plan
Apply the configuration:

bash
Copy
Edit
terraform apply
Access the web application:

Once deployed, use the Route 53 custom domain to access the application.

Outputs
Terraform will output:

EC2 Private IP

RDS Endpoint

Route 53 domain name

API Gateway endpoint
