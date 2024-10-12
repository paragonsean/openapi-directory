

# VPCDerivedInfo

Information about the subnets and security groups for an Amazon OpenSearch Service domain provisioned within a virtual private cloud (VPC). For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html\">Launching your Amazon OpenSearch Service domains using a VPC</a>. This information only exists if the domain was created with <code>VPCOptions</code>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**vpCId** | [**String**](String.md) |  |  [optional] |
|**subnetIds** | [**List**](List.md) |  |  [optional] |
|**availabilityZones** | [**List**](List.md) |  |  [optional] |
|**securityGroupIds** | [**List**](List.md) |  |  [optional] |



