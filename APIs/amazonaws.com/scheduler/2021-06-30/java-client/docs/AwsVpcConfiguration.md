

# AwsVpcConfiguration

This structure specifies the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the awsvpc network mode.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignPublicIp** | [**AssignPublicIp**](AssignPublicIp.md) |  |  [optional] |
|**securityGroups** | [**List**](List.md) |  |  [optional] |
|**subnets** | [**List**](List.md) |  |  |



