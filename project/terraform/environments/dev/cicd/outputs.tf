#Product reader
output product_reader_cicd_dev_id {
  value       = module.product_reader_cicd_dev.codebuild_id
  description = "Product reader project id"
}

output product_reader_cicd_dev_arn {
  value       = module.product_reader_cicd_dev.codebuild_arn
  description = "Product reader project arn"
}

output product_reader_cicd_dev_payload_url {
  value       = module.product_reader_cicd_dev.*.codebuild_payload_url
  description = "product_reader_cicd_dev webhook url"
}

output product_reader_cicd_dev_secret {
  value       = module.product_reader_cicd_dev.*.codebuild_secret
  description = "product_reader_cicd_dev secret for webhook"
}

#Geo reader
output geo_reader_cicd_dev_id {
  value       = module.geo_reader_cicd_dev.codebuild_id
  description = "Geo reader project id"
}

output geo_reader_cicd_dev_arn {
  value       = module.geo_reader_cicd_dev.codebuild_arn
  description = "Geo reader project arn"
}

output geo_reader_cicd_dev_payload_url {
  value       = module.geo_reader_cicd_dev.*.codebuild_payload_url
  description = "geo_reader_cicd_dev webhook url"
}

output geo_reader_cicd_dev_secret {
  value       = module.geo_reader_cicd_dev.*.codebuild_secret
  description = "geo_reader_cicd_dev secret for webhook"
}

#Product writer
output product_writer_cicd_dev_id {
  value       = module.product_writer_cicd_dev.codebuild_id
  description = "Product writer project id"
}

output product_writer_cicd_dev_arn {
  value       = module.product_writer_cicd_dev.codebuild_arn
  description = "Product writer project arn"
}

output product_writer_cicd_dev_payload_url {
  value       = module.product_writer_cicd_dev.*.codebuild_payload_url
  description = "product_writer_cicd_dev webhook url"
}

output product_writer_cicd_dev_secret {
  value       = module.product_writer_cicd_dev.*.codebuild_secret
  description = "product_writer_cicd_dev secret for webhook"
}

#Product delta reader
output product_delta_reader_cicd_dev_id {
  value       = module.product_delta_reader_cicd_dev.codebuild_id
  description = "Product delta reader project id"
}

output product_delta_reader_cicd_dev_arn {
  value       = module.product_delta_reader_cicd_dev.codebuild_arn
  description = "Product delta reader project arn"
}

output product_delta_reader_cicd_dev_payload_url {
  value       = module.product_delta_reader_cicd_dev.*.codebuild_payload_url
  description = "product_delta_reader_cicd_dev webhook url"
}

output product_delta_reader_cicd_dev_secret {
  value       = module.product_delta_reader_cicd_dev.*.codebuild_secret
  description = "product_delta_reader_cicd_dev secret for webhook"
}

#Prodcut grpc api
output product_grpc_api_dev_id {
  value       = module.product_grpc_api_dev.codebuild_id
  description = "Product grpc api project id"
}

output product_grpc_api_dev_arn {
  value       = module.product_grpc_api_dev.codebuild_arn
  description = "Product grpc api project arn"
}

output product_grpc_api_dev_payload_url {
  value       = module.product_grpc_api_dev.*.codebuild_payload_url
  description = "product_grpc_api_dev webhook url"
}

output product_grpc_api_dev_secret {
  value       = module.product_grpc_api_dev.*.codebuild_secret
  description = "product_grpc_api_dev secret for webhook"
}

#Produc prs
output product_prs_dev_id {
  value       = module.product_prs_cicd_dev.codebuild_id
  description = "product_prs_cicd_dev project id"
}

output product_prs_dev_arn {
  value       = module.product_prs_cicd_dev.codebuild_arn
  description = "product_prs_cicd_dev project arn"
}

output product_prs_dev_payload_url {
  value       = module.product_prs_cicd_dev.*.codebuild_payload_url
  description = "product_prs_cicd_dev webhook url"
}

output product_prs_dev_secret {
  value       = module.product_prs_cicd_dev.*.codebuild_secret
  description = "product_prs_cicd_dev secret for webhook"
}

#Produc Stock
output product_stock_dev_id {
  value       = module.product_stock_cicd_dev.codebuild_id
  description = "product_stock_cicd_dev project id"
}

output product_stock_dev_arn {
  value       = module.product_stock_cicd_dev.codebuild_arn
  description = "product_stock_cicd_dev project arn"
}

output product_stock_dev_payload_url {
  value       = module.product_stock_cicd_dev.*.codebuild_payload_url
  description = "product_stock_cicd_dev webhook url"
}

output product_stock_dev_secret {
  value       = module.product_stock_cicd_dev.*.codebuild_secret
  description = "product_stock_cicd_dev secret for webhook"
}
