# Architecture:
Here I am using AWS functional url to access S3 bucket using python boto3. It is compatible with error handling also like bucket or path not exist then it will create an exceptional and send the response to the user like "bucket does not exist or path not found". Using of the terraform to create AWS Lambda, S3, all the required permissions.

![image](https://github.com/user-attachments/assets/6969b951-0e63-4e07-83b5-0db469203ea1)



# Tools Used:
1. Terraform 
2. AWS Lambda
3. AWS S3
4. Python boto3

# Features:
1. Error Handling
2. Serverless
3. Cost Optimized

# Required Terraform Variables (variables.tf):
   variable "function_name" {
    default = "<your-function-name>" 
   }
   
   variable "bucket_name" {
    default = "<your-bucket-name>"
   }
   
   variable "access_key" {
    default = "<your-access-key>"
   }
   
   variable "secret_key" {
    default = "<your-secret-key>"
   }
   
   variable "region" {
    default = "ap-south-1"
   }

# Deploy using Terraform (Kindly follow the below video link):
https://drive.google.com/file/d/1vQ41Z8x3UgCRsbGBNnef7yOs0EVhbVws/view?usp=sharing


# Delete Resources using Terraform (Kindly follow the below video link):
https://drive.google.com/file/d/1N-WfnjTu3hkRZmTdWoJDAjvDJh38D1j4/view?usp=sharing


# Screenshots:
1. # Terraform
   <img width="1428" alt="image" src="https://github.com/user-attachments/assets/59a6a7ca-cd89-4768-bd95-a6e75b9c923b" />
   <img width="1422" alt="image" src="https://github.com/user-attachments/assets/2560ff5c-4513-45d5-a0d1-eae792ecd102" />
   
3. # S3
   <img width="1440" alt="image" src="https://github.com/user-attachments/assets/b0eb025e-7c5c-4c3c-b716-292b937a1b8c" />
   
4. # Lambda
   <img width="1426" alt="image" src="https://github.com/user-attachments/assets/38ae8821-9979-4b6a-a5cc-717a53d5111d" />
   <img width="1438" alt="image" src="https://github.com/user-attachments/assets/9891e699-1342-4a9e-9ae0-5215d527091f" />

5. # Response
   <img width="1189" alt="image" src="https://github.com/user-attachments/assets/6a837585-42bb-4432-b862-deb3c64b5d14" />
   <img width="1191" alt="image" src="https://github.com/user-attachments/assets/27763e78-664f-4323-a748-8336b8a850c2" />
   <img width="1207" alt="image" src="https://github.com/user-attachments/assets/747bbad4-256c-4dc6-8b32-6de7abfda496" />





   

