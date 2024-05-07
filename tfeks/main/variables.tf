# Module: tfeks
# variables definition
variable region {
    description = "Region to work on"
    type = string
    default = "us-east-1"
}

variable environment {
    description = "Environment of the solution"
    type = string
    default = "prd"
}

variable owner {
    description = "Owner of the solution"
    type = string
    default = "HerranCorp"
}

variable "application" {
    description = "Application name"
    type = string
    default = "tfeks"
}