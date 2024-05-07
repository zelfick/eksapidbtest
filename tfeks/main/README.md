# tfeks

[![terraform](https://img.shields.io/badge/terraform-v1.16.X-5C4EE5.svg)](https://www.terraform.io)

## This project is about
terraform code for ballastlane test

## To use this template  (Prerequisites)

## Prerequisites

You will need the following things properly installed on your computer.

* [awscli](https://aws.amazon.com/cli/)
* [Git](http://git-scm.com/)
* [kubectl]()
* [Terraform](https://www.terraform.io/downloads.html)
* [terraform-docs](https://terraform-docs.io/user-guide/installation/)

## Execution commands
This is organized as environment and using backend config for specific one, referring the same shared resources
We proceed to initialize and setup the backend:

```tf18 -chdir=./main init -backend-config=./env/prd.tf```

Then we can execute the other command and they would be referring the backend setted, we can for example execute the validation to check sintaxis is correct: 

```tf18 -chdir=./main validate```

and then you can execute the plan and store its output in a file for follow changes:

```tf18 -chdir=./main plan xversion_date```

Then proceed to create the eks cluster and wait between 10 to 15 min:

```tf18 -chdir=./main apply --auto-approve```

Tear down all solution resources when finished:

```tf18 -chdir=./main delete --auto-approve```

## Interact with the Cluster
Execute this command to add the context to your local kubeconfig:

```aws eks --region us-east-1 update-kubeconfig --name ballastlane-cluster```

Start executing kubectl commands:

```kubectl get nodes```

## Terraform-docs

<Execute terraform-docs and paste the output here>

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_eks"></a> [eks](#module\_eks) | terraform-aws-modules/eks/aws | 19.15.1 |
| <a name="module_vpc"></a> [vpc](#module\_vpc) | terraform-aws-modules/vpc/aws | ~> 4.0 |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_application"></a> [application](#input\_application) | Application name | `string` | `"tfeks"` | no |
| <a name="input_environment"></a> [environment](#input\_environment) | Environment of the solution | `string` | `"prd"` | no |
| <a name="input_owner"></a> [owner](#input\_owner) | Owner of the solution | `string` | `"HerranCorp"` | no |
| <a name="input_region"></a> [region](#input\_region) | Region to work on | `string` | `"us-east-1"` | no |

## Outputs

No outputs.



