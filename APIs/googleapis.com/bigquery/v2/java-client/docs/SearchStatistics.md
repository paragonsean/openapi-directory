

# SearchStatistics

Statistics for a search query. Populated as part of JobStatistics2.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**indexUnusedReasons** | [**List&lt;IndexUnusedReason&gt;**](IndexUnusedReason.md) | When &#x60;indexUsageMode&#x60; is &#x60;UNUSED&#x60; or &#x60;PARTIALLY_USED&#x60;, this field explains why indexes were not used in all or part of the search query. If &#x60;indexUsageMode&#x60; is &#x60;FULLY_USED&#x60;, this field is not populated. |  [optional] |
|**indexUsageMode** | [**IndexUsageModeEnum**](#IndexUsageModeEnum) | Specifies the index usage mode for the query. |  [optional] |



## Enum: IndexUsageModeEnum

| Name | Value |
|---- | -----|
| INDEX_USAGE_MODE_UNSPECIFIED | &quot;INDEX_USAGE_MODE_UNSPECIFIED&quot; |
| UNUSED | &quot;UNUSED&quot; |
| PARTIALLY_USED | &quot;PARTIALLY_USED&quot; |
| FULLY_USED | &quot;FULLY_USED&quot; |



