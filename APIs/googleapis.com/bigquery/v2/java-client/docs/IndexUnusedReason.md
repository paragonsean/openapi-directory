

# IndexUnusedReason

Reason about why no search index was used in the search query (or sub-query).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseTable** | [**TableReference**](TableReference.md) |  |  [optional] |
|**code** | [**CodeEnum**](#CodeEnum) | Specifies the high-level reason for the scenario when no search index was used. |  [optional] |
|**indexName** | **String** | Specifies the name of the unused search index, if available. |  [optional] |
|**message** | **String** | Free form human-readable reason for the scenario when no search index was used. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| INDEX_CONFIG_NOT_AVAILABLE | &quot;INDEX_CONFIG_NOT_AVAILABLE&quot; |
| PENDING_INDEX_CREATION | &quot;PENDING_INDEX_CREATION&quot; |
| BASE_TABLE_TRUNCATED | &quot;BASE_TABLE_TRUNCATED&quot; |
| INDEX_CONFIG_MODIFIED | &quot;INDEX_CONFIG_MODIFIED&quot; |
| TIME_TRAVEL_QUERY | &quot;TIME_TRAVEL_QUERY&quot; |
| NO_PRUNING_POWER | &quot;NO_PRUNING_POWER&quot; |
| UNINDEXED_SEARCH_FIELDS | &quot;UNINDEXED_SEARCH_FIELDS&quot; |
| UNSUPPORTED_SEARCH_PATTERN | &quot;UNSUPPORTED_SEARCH_PATTERN&quot; |
| OPTIMIZED_WITH_MATERIALIZED_VIEW | &quot;OPTIMIZED_WITH_MATERIALIZED_VIEW&quot; |
| SECURED_BY_DATA_MASKING | &quot;SECURED_BY_DATA_MASKING&quot; |
| MISMATCHED_TEXT_ANALYZER | &quot;MISMATCHED_TEXT_ANALYZER&quot; |
| BASE_TABLE_TOO_SMALL | &quot;BASE_TABLE_TOO_SMALL&quot; |
| BASE_TABLE_TOO_LARGE | &quot;BASE_TABLE_TOO_LARGE&quot; |
| ESTIMATED_PERFORMANCE_GAIN_TOO_LOW | &quot;ESTIMATED_PERFORMANCE_GAIN_TOO_LOW&quot; |
| NOT_SUPPORTED_IN_STANDARD_EDITION | &quot;NOT_SUPPORTED_IN_STANDARD_EDITION&quot; |
| INDEX_SUPPRESSED_BY_FUNCTION_OPTION | &quot;INDEX_SUPPRESSED_BY_FUNCTION_OPTION&quot; |
| QUERY_CACHE_HIT | &quot;QUERY_CACHE_HIT&quot; |
| INTERNAL_ERROR | &quot;INTERNAL_ERROR&quot; |
| OTHER_REASON | &quot;OTHER_REASON&quot; |



