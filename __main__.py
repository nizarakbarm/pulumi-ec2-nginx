import pulumi
import pulumi_aws as aws


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
security_group = aws.ec2.SecurityGroup("http-port",
        description="Allow HTTP traffic",
        from_port=80,
        to_port=80,
        protocol="tcp",
        cidr_blocks=['0.0.0.0/0']
)
print("Security group creation complete...")

print("Create EC2 Instance...")
# Create EC2 Instance
server = aws.ec2.Instance("nginx",
        ami="ami-0ebcd68de1afe59cd",
        instance_type="t2.micro",
        user_data=user_data,
        vpc_security_group_ids=[security_group.id]                         
)
print("EC2 Instance Creation Complete...")


pulumi.export('public_ip', server.public_ip)