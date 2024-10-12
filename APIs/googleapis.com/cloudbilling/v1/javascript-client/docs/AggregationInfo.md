# CloudBillingApi.AggregationInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregationCount** | **Number** | The number of intervals to aggregate over. Example: If aggregation_level is \&quot;DAILY\&quot; and aggregation_count is 14, aggregation will be over 14 days. | [optional] 
**aggregationInterval** | **String** |  | [optional] 
**aggregationLevel** | **String** |  | [optional] 



## Enum: AggregationIntervalEnum


* `AGGREGATION_INTERVAL_UNSPECIFIED` (value: `"AGGREGATION_INTERVAL_UNSPECIFIED"`)

* `DAILY` (value: `"DAILY"`)

* `MONTHLY` (value: `"MONTHLY"`)





## Enum: AggregationLevelEnum


* `AGGREGATION_LEVEL_UNSPECIFIED` (value: `"AGGREGATION_LEVEL_UNSPECIFIED"`)

* `ACCOUNT` (value: `"ACCOUNT"`)

* `PROJECT` (value: `"PROJECT"`)




