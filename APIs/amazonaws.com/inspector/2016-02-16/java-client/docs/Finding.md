

# Finding

Contains information about an Amazon Inspector finding. This data type is used as the response element in the <a>DescribeFindings</a> action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | [**String**](String.md) |  |  |
|**schemaVersion** | [**Integer**](Integer.md) |  |  [optional] |
|**service** | [**String**](String.md) |  |  [optional] |
|**serviceAttributes** | [**FindingServiceAttributes**](FindingServiceAttributes.md) |  |  [optional] |
|**assetType** | [**AssetType**](AssetType.md) |  |  [optional] |
|**assetAttributes** | [**FindingAssetAttributes**](FindingAssetAttributes.md) |  |  [optional] |
|**id** | [**String**](String.md) |  |  [optional] |
|**title** | [**String**](String.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**recommendation** | [**String**](String.md) |  |  [optional] |
|**severity** | [**Severity**](Severity.md) |  |  [optional] |
|**numericSeverity** | [**Double**](Double.md) |  |  [optional] |
|**confidence** | [**Integer**](Integer.md) |  |  [optional] |
|**indicatorOfCompromise** | [**Boolean**](Boolean.md) |  |  [optional] |
|**attributes** | [**List**](List.md) |  |  |
|**userAttributes** | [**List**](List.md) |  |  |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**updatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |



