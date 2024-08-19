

# AwsVpcConfiguration

This structure specifies the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the <code>awsvpc</code> network mode.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**subnets** | [**List**](List.md) |  |  |
|**securityGroups** | [**List**](List.md) |  |  [optional] |
|**assignPublicIp** | [**AssignPublicIp**](AssignPublicIp.md) |  |  [optional] |



