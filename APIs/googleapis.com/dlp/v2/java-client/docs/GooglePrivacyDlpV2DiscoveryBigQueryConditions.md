

# GooglePrivacyDlpV2DiscoveryBigQueryConditions

Requirements that must be true before a table is scanned in discovery for the first time. There is an AND relationship between the top-level attributes. Additionally, minimum conditions with an OR relationship that must be met before Cloud DLP scans a table can be set (like a minimum row count or a minimum table age).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAfter** | **String** | BigQuery table must have been created after this date. Used to avoid backfilling. |  [optional] |
|**orConditions** | [**GooglePrivacyDlpV2OrConditions**](GooglePrivacyDlpV2OrConditions.md) |  |  [optional] |
|**typeCollection** | [**TypeCollectionEnum**](#TypeCollectionEnum) | Restrict discovery to categories of table types. |  [optional] |
|**types** | [**GooglePrivacyDlpV2BigQueryTableTypes**](GooglePrivacyDlpV2BigQueryTableTypes.md) |  |  [optional] |



## Enum: TypeCollectionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;BIG_QUERY_COLLECTION_UNSPECIFIED&quot; |
| ALL_TYPES | &quot;BIG_QUERY_COLLECTION_ALL_TYPES&quot; |
| ONLY_SUPPORTED_TYPES | &quot;BIG_QUERY_COLLECTION_ONLY_SUPPORTED_TYPES&quot; |



