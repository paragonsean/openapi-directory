

# VpcConfigOutput

If this canary is to test an endpoint in a VPC, this structure contains information about the subnets and security groups of the VPC endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html\"> Running a Canary in a VPC</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**vpcId** | [**String**](String.md) |  |  [optional] |
|**subnetIds** | [**List**](List.md) |  |  [optional] |
|**securityGroupIds** | [**List**](List.md) |  |  [optional] |



