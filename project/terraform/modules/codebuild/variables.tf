variable codebuild_project_name {
  type        = string
  default     = ""
  description = "Name of your codebuild project"
}


variable project_description {
  type        = string
  default     = ""
  description = "Project description"
}

variable code_build_service_role_arn {
  type        = string
  default     = "arn:aws:iam::127298087018:role/service-role/codebuild-cpq-smart-search-role"
  description = "The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account."
}

variable github_repository {
  type        = string
  default     = ""
  description = "Your github repository"
}

variable branch_name {
  type        = string
  default     = ""
  description = "Branch name to use"
}

variable buildspec_file {
  type        = string
  default     = ""
  description = "Buildspec file path"
}

variable "tags" {
    type = map
    default = {}
}

variable create_webhook {
  default     = false
}


#codepipeline role - arn:aws:iam::127298087018:role/service-role/AWSCodePipelineServiceRole-us-west-2-smart-search-product-role