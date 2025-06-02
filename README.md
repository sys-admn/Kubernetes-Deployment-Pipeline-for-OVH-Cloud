# Kubernetes Deployment Pipeline for OVH Cloud

This project provides a CI/CD pipeline for deploying a Nginx web server on OVH Cloud's Kubernetes service. The pipeline uses GitHub Actions for automation, Ansible for configuration management, and Kubernetes for container orchestration.

## Project Overview

This pipeline automates the deployment of a Nginx web server with persistent storage on OVH Cloud Kubernetes. The deployment includes:

- GitHub Actions workflow for CI/CD
- Ansible for configuring the bastion host
- Kubernetes manifests for deploying Nginx with persistent storage
- Automatic health checks to verify deployment

## Repository Structure

```
Kubernetes-Deployment-Pipeline-for-OVH-Cloud/
├── .github/workflows/      # GitHub Actions workflow definitions
│   └── deploy.yml          # Main deployment workflow
├── ansible/                # Ansible configuration files
│   ├── generate_inventory.py  # Script to generate Ansible inventory
│   ├── inventory.ini       # Ansible inventory file
│   └── setup_kubectl.yml   # Ansible playbook for setting up kubectl
├── k8s/                    # Kubernetes manifests
│   └── nginx.yaml          # Nginx deployment with persistent volume
├── .gitignore              # Git ignore file
└── README.md               # Project documentation
```

Note: The `kubeconfig.yml` file will be generated during deployment.

## Deployment Process

1. When code is pushed to the main branch, the GitHub Actions workflow is triggered  
2. The workflow sets up SSH access to the bastion host  
3. Ansible configures the bastion host with kubectl and necessary dependencies  
4. Kubernetes manifests are applied to deploy Nginx with persistent storage  
5. Health checks verify the deployment is successful  

## Prerequisites

- OVH Cloud Kubernetes cluster  
- Bastion host with SSH access  
- GitHub repository with the following secrets configured:  
  - `SSH_PRIVATE_KEY`: SSH private key for accessing the bastion host  
  - `BASTION_IP`: IP address of the bastion host  
  - `KUBECONFIG_B64`: Base64-encoded kubeconfig file for the Kubernetes cluster  

## Deployment Components

### Nginx Deployment

The deployment includes:

- Nginx web server with a custom welcome page  
- Persistent Volume Claim using OVH's Cinder storage (1GB)  
- LoadBalancer service to expose the application  

### CI/CD Pipeline

The GitHub Actions workflow automates:

- Code checkout  
- Python environment setup  
- SSH configuration  
- Ansible inventory generation  
- Kubernetes configuration  
- Deployment verification  

## Usage

1. Clone this repository  
2. Configure the required GitHub secrets  
3. Push changes to the main branch to trigger the deployment  
4. Access the Nginx service using the LoadBalancer IP address  

## Monitoring and Verification

The deployment includes health checks to verify:

- Successful connection to the bastion host  
- Proper kubectl configuration  
- Nginx deployment availability  
- Service exposure via LoadBalancer  

## Contact

[Aly Sall – LinkedIn](https://fr.linkedin.com/in/aly-sall)


