

# Endpoint

Amazon S3 on Outposts Access Points simplify managing data access at scale for shared datasets in S3 on Outposts. S3 on Outposts uses endpoints to connect to Outposts buckets so that you can perform actions within your virtual private cloud (VPC). For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/WorkingWithS3Outposts.html\"> Accessing S3 on Outposts using VPC-only access points</a> in the <i>Amazon Simple Storage Service User Guide</i>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpointArn** | [**String**](String.md) |  |  [optional] |
|**outpostsId** | [**String**](String.md) |  |  [optional] |
|**cidrBlock** | [**String**](String.md) |  |  [optional] |
|**status** | [**EndpointStatus**](EndpointStatus.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**networkInterfaces** | [**List**](List.md) |  |  [optional] |
|**vpcId** | [**String**](String.md) |  |  [optional] |
|**subnetId** | [**String**](String.md) |  |  [optional] |
|**securityGroupId** | [**String**](String.md) |  |  [optional] |
|**accessType** | [**EndpointAccessType**](EndpointAccessType.md) |  |  [optional] |
|**customerOwnedIpv4Pool** | [**String**](String.md) |  |  [optional] |
|**failedReason** | [**EndpointFailedReason**](EndpointFailedReason.md) |  |  [optional] |



