module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "${var.project_name}-cluster"
  cluster_version = "1.28"
  subnets         = module.vpc.public_subnets
  vpc_id          = module.vpc.vpc_id

  manage_aws_auth = true

  eks_managed_node_groups = {
    default = {
      desired_size = 2
      max_size     = 3
      min_size     = 1
      instance_types = ["t3.medium"]
    }
  }

  tags = {
    Project = var.project_name
  }
}
