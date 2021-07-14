output codebuild_id {
  value       = aws_codebuild_project.codebuild.id
  description = "Codebuild project id"
}

output codebuild_arn {
  value       = aws_codebuild_project.codebuild.arn
  description = "Codebuild project arn"
}

output codebuild_payload_url {
  value       = aws_codebuild_webhook.codebuild.*.payload_url
  description = "URL used from Gidhub for webhooks"
}

output codebuild_secret {
  value       = aws_codebuild_webhook.codebuild.*.secret
  description = "Secret ket for Github settings"
}