#  Provision Nginx inside EC2 AWS by using Pulumi and Github Action

This repository is used solely for learning pulumi and Github Action. This repo containing:

- pulumi python script for provisioning nginx at EC2 AWS

- .github/workflows/push_requests.yml that contain workflows to do pulumi up, test curl, and pulumi destroy

## Environment Secrets at Environment Development

You need to set some environment secrets at environment development, which are:

- ARN_ROLE contain arn of OIDC role which is created at AWS

- PUBLIC_KEY contain public key for debugging EC2 instance

## Repository Secrets

You need to set repository secrets, which is:

- PULUMI_ACCESS_TOKEN contain ACCESS TOKEN of pulumi

## Environment Variables at Environment Development

You need to set environment variables at environment development, which is:

- REGION contain region that you choose for AWS EC2

-

