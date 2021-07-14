terraform {
  backend "s3" {
#    # Replace this with your bucket name!
    bucket         = "my-tfstate"
    key            = "global/ecr/ecr.tfstate"
    region         = "us-west-2"
#    # Replace this with your DynamoDB table name!
    dynamodb_table = "my-terraform-locks"
    encrypt        = true
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-west-2"
}

module microservice_a {
  source                  = "../../../modules/ecr_repository"
  repository_name         = "Microservice_A"
  attach_lifecycle_policy = true
}