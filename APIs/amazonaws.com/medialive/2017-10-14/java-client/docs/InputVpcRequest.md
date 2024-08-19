

# InputVpcRequest

Settings for a private VPC Input. When this property is specified, the input destination addresses will be created in a VPC rather than with public Internet addresses. This property requires setting the roleArn property on Input creation. Not compatible with the inputSecurityGroups property. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**securityGroupIds** | [**List**](List.md) |  |  [optional] |
|**subnetIds** | [**List**](List.md) |  |  |



