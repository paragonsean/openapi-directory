# Superset.ChartDataResponseResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotationData** | **[{String: String}]** | All requested annotation data | [optional] 
**appliedFilters** | **[Object]** | A list with applied filters | [optional] 
**cacheKey** | **String** | Unique cache key for query object | 
**cacheTimeout** | **Number** | Cache timeout in following order: custom timeout, datasource timeout, default config timeout. | 
**cachedDttm** | **String** | Cache timestamp | 
**data** | **[Object]** | A list with results | [optional] 
**error** | **String** | Error | [optional] 
**isCached** | **Boolean** | Is the result cached | 
**query** | **String** | The executed query statement | 
**rejectedFilters** | **[Object]** | A list with rejected filters | [optional] 
**rowcount** | **Number** | Amount of rows in result set | [optional] 
**stacktrace** | **String** |  | [optional] 
**status** | **String** | Status of the query | [optional] 



## Enum: StatusEnum


* `stopped` (value: `"stopped"`)

* `failed` (value: `"failed"`)

* `pending` (value: `"pending"`)

* `running` (value: `"running"`)

* `scheduled` (value: `"scheduled"`)

* `success` (value: `"success"`)

* `timed_out` (value: `"timed_out"`)




