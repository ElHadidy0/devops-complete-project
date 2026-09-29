resource "aws_ecr_repository" "app_ecr" {
  name                 = "devops-ecom-app-repo"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Environment = var.environment
    Project     = "DevOps-Enterprise-Pipeline"
  }
}