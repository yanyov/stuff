terraform {
  backend "s3" {
    # Replace this with your bucket name!
    bucket         = "my-tfstate"
    key            = "dev/cicd/cicd.tfstate"
    region         = "us-west-2"
#     Replace this with your DynamoDB table name!
    dynamodb_table = "my-terraform-locks"
    encrypt        = true
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-west-2"
}

#microservice_a codebuild project
module microservice_a {
  source                 = "../../../modules/codebuild"
  codebuild_project_name = "smart-search-geo-reader-dev"
  project_description    = "Deploy smart-search-geo-reader to ecs cluster cpq-smart-search-dev"
  github_repository      = "https://Microservice_A_Git_Repo"
  branch_name            = "develop"
  buildspec_file         = "buildspec/buildspec_dev.yaml"
  create_webhook         = true
  tags = {
    Service     = "smart-search-geo-reader"
    Environment = "dev"
    ECS_Cluster = "cpq-smart-search-dev"
  }
}

