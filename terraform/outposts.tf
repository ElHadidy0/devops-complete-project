output "ecr_repository_url" {
  description = "URL of the Amazon ECR Repository for pushing Docker images"
  value       = aws_ecr_repository.app_ecr.repository_url
}

output "eks_cluster_name" {
  description = "Name of the Amazon EKS Cluster"
  value       = module.eks.cluster_name
}

output "eks_cluster_endpoint" {
  description = "Endpoint URL for Kubernetes API Server on EKS"
  value       = module.eks.cluster_endpoint
}

output "vpc_id" {
  description = "ID of the created AWS VPC"
  value       = module.vpc.vpc_id
}