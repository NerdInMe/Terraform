output "s3_bucket_name" {
  value       = aws_s3_bucket.example.id
  description = "The NAME of the S3 bucket"
}

output "s3_bucket_arn" {
  value       = aws_s3_bucket.example.arn
  description = "The ARN of the S3 bucket"
}

# S3 bucket region is NOT a reliable attribute in provider v5
# Use the provider region instead
data "aws_region" "current" {}

output "s3_bucket_region" {
  value       = data.aws_region.current.name
  description = "The REGION of the S3 bucket"
}

output "dynamodb_table_name" {
  value       = aws_dynamodb_table.terraform_lock.name
  description = "The NAME of the DynamoDB table"
}

output "dynamodb_table_arn" {
  value       = aws_dynamodb_table.terraform_lock.arn
  description = "The ARN of the DynamoDB table"
}
