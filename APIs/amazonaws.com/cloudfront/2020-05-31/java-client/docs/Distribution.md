

# Distribution

A distribution tells CloudFront where you want content to be delivered from, and the details about how to track and manage content delivery.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  |
|**ARN** | [**String**](String.md) |  |  |
|**status** | [**String**](String.md) |  |  |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**inProgressInvalidationBatches** | [**Integer**](Integer.md) |  |  |
|**domainName** | [**String**](String.md) |  |  |
|**activeTrustedSigners** | [**DistributionActiveTrustedSigners**](DistributionActiveTrustedSigners.md) |  |  [optional] |
|**activeTrustedKeyGroups** | [**DistributionActiveTrustedKeyGroups**](DistributionActiveTrustedKeyGroups.md) |  |  [optional] |
|**distributionConfig** | [**DistributionDistributionConfig**](DistributionDistributionConfig.md) |  |  |
|**aliasICPRecordals** | [**List**](List.md) |  |  [optional] |



