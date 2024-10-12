# BigQueryApi.VectorSearchStatistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexUnusedReasons** | [**[IndexUnusedReason]**](IndexUnusedReason.md) | When &#x60;indexUsageMode&#x60; is &#x60;UNUSED&#x60; or &#x60;PARTIALLY_USED&#x60;, this field explains why indexes were not used in all or part of the vector search query. If &#x60;indexUsageMode&#x60; is &#x60;FULLY_USED&#x60;, this field is not populated. | [optional] 
**indexUsageMode** | **String** | Specifies the index usage mode for the query. | [optional] 



## Enum: IndexUsageModeEnum


* `INDEX_USAGE_MODE_UNSPECIFIED` (value: `"INDEX_USAGE_MODE_UNSPECIFIED"`)

* `UNUSED` (value: `"UNUSED"`)

* `PARTIALLY_USED` (value: `"PARTIALLY_USED"`)

* `FULLY_USED` (value: `"FULLY_USED"`)




