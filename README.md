# 🎓 Student Registration Portal (Serverless Project)
### student-registration-aws-s3-lambda-api-dynamodb
A full-stack serverless application using Amazon S3 for static hosting, API Gateway for RESTful routing, and AWS Lambda to process and store student data into Amazon DynamoDB.

Click Here To Run this Project
👉http://student-registeration-form-aws-s3-lambda.s3-website-us-east-1.amazonaws.com 👈

---

## 📌 Introduction

The **Student Registration Portal** is a serverless web application designed to collect and store student registration data efficiently—without managing traditional servers.

The system automatically processes and saves student records in real time as soon as the registration form is submitted.

---

## 📖 About the Project

This project demonstrates a **cloud-native, serverless architecture** for handling student registrations.

Key features include:

* Real-time data submission from a web form
* Backend processing without a dedicated server
* Automatic data storage in a scalable NoSQL database

The application uses:

* **Amazon S3** for static frontend hosting
* **Amazon API Gateway** for RESTful API routing
* **AWS Lambda** for backend logic execution
* **Amazon DynamoDB** for persistent data storage

---

## 🛠️ Technologies Used

* **Frontend Hosting:** Amazon S3 (Static Website Hosting)
* **API Management:** Amazon API Gateway
* **Serverless Compute:** AWS Lambda
* **Database:** Amazon DynamoDB (NoSQL)
* **Security & Permissions:** AWS IAM (Identity and Access Management)

---

## 🚀 Step-by-Step Implementation

### 🗄️ Step 1: Create DynamoDB Table

* **Table Name:** `StudentRegister`
* **Partition Key:** `studentId` (String)

⚠️ **Important**

* Attribute names are **case-sensitive**
* The key name must match the frontend field exactly

Ensure the table status shows **Active** before proceeding.

---

### 🔐 Step 2: Configure IAM Permissions

* Created an **IAM execution role** for the Lambda function
* Attached the following policy:

  * `AmazonDynamoDBFullAccess`

This allows the Lambda function to write student records into the DynamoDB table.

---

### 🧠 Step 3: Create AWS Lambda Function

* **Function Name:** `studentRegisterFunction`
* **Runtime:** Node.js
* **Execution Role:** IAM role created in Step 2

#### Function Responsibility

The Lambda function:

* Receives student data (ID, Name, Email, Course)
* Validates the request payload
* Inserts a new item into the `StudentRegister` DynamoDB table

---

### 🌐 Step 4: Configure API Gateway & CORS

* **API Name:** `student-registration-api`
* **Method:** `POST`
* **Route Path:** `/register`

#### 🔑 CORS Configuration (CRITICAL)

To prevent **CORS** and **Connection Failed** errors:

* `Access-Control-Allow-Origin`: `*`
* `Access-Control-Allow-Methods`: `POST, OPTIONS`
* `Access-Control-Allow-Headers`: `Content-Type`

After configuration:

* Deployed the API to a stage named **`prod`**
* Copied the generated **Invoke URL**

---

### 🖥️ Step 5: Frontend Hosting on S3

* **Bucket Name:** `student-registration-form-aws-s3-lambda`
* Enabled **Static Website Hosting**
* Set `index.html` as the index document

#### Frontend Configuration

* Updated the `API_URL` inside `index.html`
* Appended `/register` to the API Gateway **prod** Invoke URL

Example:

```
https://xxxxx.execute-api.region.amazonaws.com/prod/register
```

* Uploaded the updated `index.html` file to the S3 bucket

---

## 🎉 Deployment Complete

Your **Serverless Student Registration Portal** is now live using AWS serverless services.

Click Here To Run this Project 👉http://student-registeration-form-aws-s3-lambda.s3-website-us-east-1.amazonaws.com 👈
---
