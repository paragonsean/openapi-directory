

# ExportAssetsRequest

Export asset request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetTypes** | **List&lt;String&gt;** | A list of asset types of which to take a snapshot for. For example: \&quot;google.compute.Disk\&quot;. If specified, only matching assets will be returned. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview) for all supported asset types. |  [optional] |
|**contentType** | [**ContentTypeEnum**](#ContentTypeEnum) | Asset content type. If not specified, no content but the asset name will be returned. |  [optional] |
|**outputConfig** | [**OutputConfig**](OutputConfig.md) |  |  [optional] |
|**readTime** | **String** | Timestamp to take an asset snapshot. This can only be set to a timestamp between 2018-10-02 UTC (inclusive) and the current time. If not specified, the current time will be used. Due to delays in resource data collection and indexing, there is a volatile window during which running the same query may get different results. |  [optional] |



## Enum: ContentTypeEnum

| Name | Value |
|---- | -----|
| CONTENT_TYPE_UNSPECIFIED | &quot;CONTENT_TYPE_UNSPECIFIED&quot; |
| RESOURCE | &quot;RESOURCE&quot; |
| IAM_POLICY | &quot;IAM_POLICY&quot; |



