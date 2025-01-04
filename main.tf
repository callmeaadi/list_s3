module "lambda" {
 source        = "terraform-aws-modules/lambda/aws"
 version       = "7.8.1"
 function_name = var.function_name
 description   = "LIST S3"
 handler       = "list_aws_S3.lambda_handler"
 runtime       = "python3.9"
 #lambda_role          = aws_iam_role.lambda_role.arn
 policies     = ["arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"]
 source_path = "./list_aws_S3.py"
 policy  = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
 attach_policies = true
 attach_policy  = true
 timeout       = 10
 environment_variables  = {
	BUCKET_NAME = var.bucket_name
 
 }
}


resource "aws_lambda_function_url" "test_latest" {
  function_name      = module.lambda.lambda_function_name
  authorization_type = "NONE"
}


resource "aws_s3_bucket" "example" {
  bucket = var.bucket_name
  force_destroy = true
}


output "url" {
	value = aws_lambda_function_url.test_latest.function_url
}



