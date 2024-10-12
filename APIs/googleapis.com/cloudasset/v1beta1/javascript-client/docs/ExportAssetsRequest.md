# CloudAssetApi.ExportAssetsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetTypes** | **[String]** | A list of asset types of which to take a snapshot for. For example: \&quot;google.compute.Disk\&quot;. If specified, only matching assets will be returned. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview) for all supported asset types. | [optional] 
**contentType** | **String** | Asset content type. If not specified, no content but the asset name will be returned. | [optional] 
**outputConfig** | [**OutputConfig**](OutputConfig.md) |  | [optional] 
**readTime** | **String** | Timestamp to take an asset snapshot. This can only be set to a timestamp between 2018-10-02 UTC (inclusive) and the current time. If not specified, the current time will be used. Due to delays in resource data collection and indexing, there is a volatile window during which running the same query may get different results. | [optional] 



## Enum: ContentTypeEnum


* `CONTENT_TYPE_UNSPECIFIED` (value: `"CONTENT_TYPE_UNSPECIFIED"`)

* `RESOURCE` (value: `"RESOURCE"`)

* `IAM_POLICY` (value: `"IAM_POLICY"`)




