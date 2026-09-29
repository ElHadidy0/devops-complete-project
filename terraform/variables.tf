variable "aws_region" {
  type        = string
  default     = "us-east-1"
  description = "The AWS Region where all infrastructure resources will be created"

}
variable "environment" {
  type        = string
  default     = "production"
  description = "Deployment environment name"
}