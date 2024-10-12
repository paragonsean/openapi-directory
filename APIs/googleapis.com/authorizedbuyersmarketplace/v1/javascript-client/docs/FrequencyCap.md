# AuthorizedBuyersMarketplaceApi.FrequencyCap

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxImpressions** | **Number** | The maximum number of impressions that can be served to a user within the specified time period. | [optional] 
**timeUnitType** | **String** | The time unit. Along with num_time_units defines the amount of time over which impressions per user are counted and capped. | [optional] 
**timeUnitsCount** | **Number** | The amount of time, in the units specified by time_unit_type. Defines the amount of time over which impressions per user are counted and capped. | [optional] 



## Enum: TimeUnitTypeEnum


* `TIME_UNIT_TYPE_UNSPECIFIED` (value: `"TIME_UNIT_TYPE_UNSPECIFIED"`)

* `MINUTE` (value: `"MINUTE"`)

* `HOUR` (value: `"HOUR"`)

* `DAY` (value: `"DAY"`)

* `WEEK` (value: `"WEEK"`)

* `MONTH` (value: `"MONTH"`)

* `LIFETIME` (value: `"LIFETIME"`)

* `POD` (value: `"POD"`)

* `STREAM` (value: `"STREAM"`)




