# SensitiveDataProtectionDlp.GooglePrivacyDlpV2DiscoveryBigQueryConditions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAfter** | **String** | BigQuery table must have been created after this date. Used to avoid backfilling. | [optional] 
**orConditions** | [**GooglePrivacyDlpV2OrConditions**](GooglePrivacyDlpV2OrConditions.md) |  | [optional] 
**typeCollection** | **String** | Restrict discovery to categories of table types. | [optional] 
**types** | [**GooglePrivacyDlpV2BigQueryTableTypes**](GooglePrivacyDlpV2BigQueryTableTypes.md) |  | [optional] 



## Enum: TypeCollectionEnum


* `UNSPECIFIED` (value: `"BIG_QUERY_COLLECTION_UNSPECIFIED"`)

* `ALL_TYPES` (value: `"BIG_QUERY_COLLECTION_ALL_TYPES"`)

* `ONLY_SUPPORTED_TYPES` (value: `"BIG_QUERY_COLLECTION_ONLY_SUPPORTED_TYPES"`)




