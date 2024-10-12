

# VpcConnector

<p>Describes an App Runner VPC connector resource. A VPC connector describes the Amazon Virtual Private Cloud (Amazon VPC) that an App Runner service is associated with, and the subnets and security group that are used.</p> <p>Multiple revisions of a connector might have the same <code>Name</code> and different <code>Revision</code> values.</p> <note> <p>At this time, App Runner supports only one revision per name.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**vpcConnectorName** | [**String**](String.md) |  |  [optional] |
|**vpcConnectorArn** | [**String**](String.md) |  |  [optional] |
|**vpcConnectorRevision** | [**Integer**](Integer.md) |  |  [optional] |
|**subnets** | [**List**](List.md) |  |  [optional] |
|**securityGroups** | [**List**](List.md) |  |  [optional] |
|**status** | [**VpcConnectorStatus**](VpcConnectorStatus.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**deletedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



