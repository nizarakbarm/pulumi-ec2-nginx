import os
import pulumi
import pulumi_aws as aws

env_file = os.getenv('GITHUB_ENV')

# user data for install dependency
user_data = """
#!/bin/bash
sudo yum update -y
sudo yum upgrade -y
sudo amazon-linux-extras install nginx1 -y
sudo systemctl enable nginx
sudo systemctl start nginx
"""

print("Create security group...")
# Create Security Group
security_group = aws.ec2.SecurityGroup("Security Group EC2",
        description="Security Group EC2",
        ingress=[
            aws.ec2.SecurityGroupIngressArgs(
            description="Allow port 80",
            from_port=80,
            to_port=80,
            protocol="tcp",
            cidr_blocks=['0.0.0.0/0']),
            aws.ec2.SecurityGroupIngressArgs(
            description="Allow port 22",
            from_port=22,
            to_port=22,
            protocol="tcp",
            cidr_blocks=['0.0.0.0/0']),
        ],
        egress=[
            aws.ec2.SecurityGroupIngressArgs(
            description="Allow port 80",
            from_port=80,
            to_port=80,
            protocol="tcp",
            cidr_blocks=['0.0.0.0/0']),
            aws.ec2.SecurityGroupIngressArgs(
            description="Allow port 443",
            from_port=443,
            to_port=443,
            protocol="tcp",
            cidr_blocks=['0.0.0.0/0']),
        ]
)
print("Security group creation complete...")

print("Create AWS EC2 KeyPair...")
key_pair = aws.ec2.KeyPair("key-pair",public_key=os.getenv('PUBLIC_KEY'))

print("Create EC2 Instance...")
# Create EC2 Instance
server = aws.ec2.Instance("nginx",
        ami="ami-0ebcd68de1afe59cd",
        instance_type="t2.micro",
        user_data=user_data,
        vpc_security_group_ids=[security_group.id],
        key_name=key_pair.key_name,                  
)
print("EC2 Instance Creation Complete...")

#Write ip to GITHUB_ENV
ec2_ip=f'EC2_IP='{server.public_ip}
with open(env_file,"a") as f:
    f.write(ec2_ip)

pulumi.export('public_ip', server.public_ip)