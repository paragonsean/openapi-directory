# CloudBillingApi.GoogleCloudBillingPricesV1betaAggregationInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **String** | Interval at which usage is aggregated to compute cost. Example: \&quot;MONTHLY\&quot; interval indicates that usage is aggregated every month. | [optional] 
**level** | **String** | Level at which usage is aggregated to compute cost. Example: \&quot;ACCOUNT\&quot; level indicates that usage is aggregated across all projects in a single account. | [optional] 



## Enum: IntervalEnum


* `UNSPECIFIED` (value: `"INTERVAL_UNSPECIFIED"`)

* `MONTHLY` (value: `"INTERVAL_MONTHLY"`)

* `DAILY` (value: `"INTERVAL_DAILY"`)





## Enum: LevelEnum


* `UNSPECIFIED` (value: `"LEVEL_UNSPECIFIED"`)

* `ACCOUNT` (value: `"LEVEL_ACCOUNT"`)

* `PROJECT` (value: `"LEVEL_PROJECT"`)




