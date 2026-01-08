terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example_ec2" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t3.micro"

  tags = {
    Name = "terraform-ec2"
  }
}

resource "aws_s3_bucket" "example_bucket" {
  bucket = "my-simple-terraform-bucket-terraform"

  tags = {
    Name = "terraform-s3"
  }
}
