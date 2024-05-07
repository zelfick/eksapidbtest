terraform {
  backend "s3" {
# If you want to make the bucket varible from input parameters
# bucket         = "jhaws-prd-tfstate"
    bucket         = "tfstate-jahescobar"
    key            = "us-east-1/tfeks/prd/terraform.tfstate"
# As best practice the bucket should be located in another region or account than resources in this case no
    region         = "us-east-1"
    dynamodb_table = "jhaws-prd-tfstate"
    encrypt        = true
  }
}

provider "aws" {
  region = "us-east-1"  # aws region were the resources will be created
  profile = "jhaws" #Local profile with the credentials to aws cli
  # default tags to apply to all created resources
  default_tags {
    tags = {
      Environment = "prd"
      Owner       = "HerranCorp"
      Project     = "tfeks"
    }
  }
}