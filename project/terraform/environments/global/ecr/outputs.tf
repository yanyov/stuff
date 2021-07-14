output "product-reader-registry-arn" {
  description = "Full ARN of the repository"
  value       = module.product_reader_registry.arn
}

output "product-reader-registry-name" {
  description = "Name of the product-reader-registry"
  value       = module.product_reader_registry.name
}

output "product-reader-registry-registry-id" {
  value       = module.product_reader_registry.registry_id
  description = "Registry ID where the repository was created"
}

output "product-reader-registry-repository-url" {
  value       = module.product_reader_registry.repository_url
  description = "URL of the repository"
}

####
output "product-writer-registry-arn" {
  description = "Full ARN of the repository"
  value       = module.product_writer_registry.arn
}

output "product-writer-registry-name" {
  description = "Name of the product-reader-registry"
  value       = module.product_writer_registry.name
}

output "product-writer-registry-registry-id" {
  value       = module.product_writer_registry.registry_id
  description = "Registry ID where the repository was created"
}

output "product-writer-registry-repository-url" {
  value       = module.product_writer_registry.repository_url
  description = "URL of the repository"
}

###

output "grpc-product-registry-arn" {
  description = "Full ARN of the repository"
  value       = module.grpc_product_registry.arn
}

output "grpc-product-registry-name" {
  description = "Name of the product-reader-registry"
  value       = module.grpc_product_registry.name
}

output "grpc-product-registry-id" {
  value       = module.grpc_product_registry.registry_id
  description = "Registry ID where the repository was created"
}

output "grpc-product-registry-url" {
  value       = module.grpc_product_registry.repository_url
  description = "URL of the repository"
}

##

output "oracle-registry-arn" {
  description = "Full ARN of the repository"
  value       = module.oracle_registry.arn
}

output "oracle-registry-name" {
  description = "Name of the oracle-registry"
  value       = module.oracle_registry.name
}

output "oracle-registry-id" {
  value       = module.oracle_registry.registry_id
  description = "Registry ID where the repository was created"
}

output "oracle-registry-url" {
  value       = module.oracle_registry.repository_url
  description = "URL of the repository"
}

##

output "geo_reader_registry-arn" {
  description = "Full ARN of the repository"
  value       = module.geo_reader_registry.arn
}

output "geo_reader_registry-name" {
  description = "Name of the geo-reader-registry"
  value       = module.geo_reader_registry.name
}

output "geo_reader_registry-id" {
  value       = module.geo_reader_registry.registry_id
  description = "Registry ID where the repository was created"
}

output "geo_reader_registry-url" {
  value       = module.geo_reader_registry.repository_url
  description = "URL of the repository"
}

##

output "product_prs-arn" {
  description = "Full ARN of the repository"
  value       = module.product_prs.arn
}

output "product_prs-name" {
  description = "Name of the product_prs"
  value       = module.product_prs.name
}

output "product_prs-id" {
  value       = module.product_prs.registry_id
  description = "Registry ID where the repository was created"
}

output "product_prs-url" {
  value       = module.product_prs.repository_url
  description = "URL of the repository"
}

##

output "product_delta_reader-arn" {
  description = "Full ARN of the repository"
  value       = module.product_delta_reader.arn
}

output "product_delta_reader-name" {
  description = "Name of the product_prs"
  value       = module.product_delta_reader.name
}

output "product_delta_reader-id" {
  value       = module.product_delta_reader.registry_id
  description = "Registry ID where the repository was created"
}

output "product_delta_reader-url" {
  value       = module.product_delta_reader.repository_url
  description = "URL of the repository"
}

## Product Stock

output "product_stock-arn" {
  description = "Full ARN of the repository"
  value       = module.product_stock.arn
}

output "product_stock-name" {
  description = "Name of the product_prs"
  value       = module.product_stock.name
}

output "product_stock-id" {
  value       = module.product_stock.registry_id
  description = "Registry ID where the repository was created"
}

output "product_stock-url" {
  value       = module.product_stock.repository_url
  description = "URL of the repository"
}
