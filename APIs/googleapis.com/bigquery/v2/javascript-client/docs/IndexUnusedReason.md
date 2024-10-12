# BigQueryApi.IndexUnusedReason

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseTable** | [**TableReference**](TableReference.md) |  | [optional] 
**code** | **String** | Specifies the high-level reason for the scenario when no search index was used. | [optional] 
**indexName** | **String** | Specifies the name of the unused search index, if available. | [optional] 
**message** | **String** | Free form human-readable reason for the scenario when no search index was used. | [optional] 



## Enum: CodeEnum


* `CODE_UNSPECIFIED` (value: `"CODE_UNSPECIFIED"`)

* `INDEX_CONFIG_NOT_AVAILABLE` (value: `"INDEX_CONFIG_NOT_AVAILABLE"`)

* `PENDING_INDEX_CREATION` (value: `"PENDING_INDEX_CREATION"`)

* `BASE_TABLE_TRUNCATED` (value: `"BASE_TABLE_TRUNCATED"`)

* `INDEX_CONFIG_MODIFIED` (value: `"INDEX_CONFIG_MODIFIED"`)

* `TIME_TRAVEL_QUERY` (value: `"TIME_TRAVEL_QUERY"`)

* `NO_PRUNING_POWER` (value: `"NO_PRUNING_POWER"`)

* `UNINDEXED_SEARCH_FIELDS` (value: `"UNINDEXED_SEARCH_FIELDS"`)

* `UNSUPPORTED_SEARCH_PATTERN` (value: `"UNSUPPORTED_SEARCH_PATTERN"`)

* `OPTIMIZED_WITH_MATERIALIZED_VIEW` (value: `"OPTIMIZED_WITH_MATERIALIZED_VIEW"`)

* `SECURED_BY_DATA_MASKING` (value: `"SECURED_BY_DATA_MASKING"`)

* `MISMATCHED_TEXT_ANALYZER` (value: `"MISMATCHED_TEXT_ANALYZER"`)

* `BASE_TABLE_TOO_SMALL` (value: `"BASE_TABLE_TOO_SMALL"`)

* `BASE_TABLE_TOO_LARGE` (value: `"BASE_TABLE_TOO_LARGE"`)

* `ESTIMATED_PERFORMANCE_GAIN_TOO_LOW` (value: `"ESTIMATED_PERFORMANCE_GAIN_TOO_LOW"`)

* `NOT_SUPPORTED_IN_STANDARD_EDITION` (value: `"NOT_SUPPORTED_IN_STANDARD_EDITION"`)

* `INDEX_SUPPRESSED_BY_FUNCTION_OPTION` (value: `"INDEX_SUPPRESSED_BY_FUNCTION_OPTION"`)

* `QUERY_CACHE_HIT` (value: `"QUERY_CACHE_HIT"`)

* `INTERNAL_ERROR` (value: `"INTERNAL_ERROR"`)

* `OTHER_REASON` (value: `"OTHER_REASON"`)




