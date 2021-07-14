resource "aws_codebuild_project" "codebuild" {
  name           = var.codebuild_project_name
  description    = var.project_description

  service_role = var.code_build_service_role_arn

  artifacts {
    type = "NO_ARTIFACTS"
  }

  environment {
    compute_type                = "BUILD_GENERAL1_SMALL"
    image                       = "aws/codebuild/amazonlinux2-x86_64-standard:2.0"
    type                        = "LINUX_CONTAINER"
    image_pull_credentials_type = "CODEBUILD"
    privileged_mode             = true
  }


  logs_config {
    cloudwatch_logs {
      status = "ENABLED"
    }
  }

  source {
    type            = "GITHUB_ENTERPRISE"
    location        = var.github_repository
    buildspec       = var.buildspec_file
    git_clone_depth = 1
  }

  source_version = var.branch_name

  tags = var.tags

}

resource "aws_codebuild_webhook" "codebuild" {
  count = var.create_webhook ? 1 : 0
  project_name = aws_codebuild_project.codebuild.name
  branch_filter = var.branch_name
}
