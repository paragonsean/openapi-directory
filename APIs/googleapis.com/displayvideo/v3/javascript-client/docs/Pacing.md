# DisplayVideo360Api.Pacing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dailyMaxImpressions** | **String** | Maximum number of impressions to serve every day. Applicable when the budget is impression based. Must be greater than 0. | [optional] 
**dailyMaxMicros** | **String** | Maximum currency amount to spend every day in micros of advertiser&#39;s currency. Applicable when the budget is currency based. Must be greater than 0. For example, for 1.5 standard unit of the currency, set this field to 1500000. The value assigned will be rounded to whole billable units for the relevant currency by the following rules: any positive value less than a single billable unit will be rounded up to one billable unit and any value larger than a single billable unit will be rounded down to the nearest billable value. For example, if the currency&#39;s billable unit is 0.01, and this field is set to 10257770, it will round down to 10250000, a value of 10.25. If set to 505, it will round up to 10000, a value of 0.01. | [optional] 
**pacingPeriod** | **String** | Required. The time period in which the pacing budget will be spent. When automatic budget allocation is enabled at the insertion order via automationType, this field is output only and defaults to &#x60;PACING_PERIOD_FLIGHT&#x60;. | [optional] 
**pacingType** | **String** | Required. The type of pacing that defines how the budget amount will be spent across the pacing_period. | [optional] 



## Enum: PacingPeriodEnum


* `UNSPECIFIED` (value: `"PACING_PERIOD_UNSPECIFIED"`)

* `DAILY` (value: `"PACING_PERIOD_DAILY"`)

* `FLIGHT` (value: `"PACING_PERIOD_FLIGHT"`)





## Enum: PacingTypeEnum


* `UNSPECIFIED` (value: `"PACING_TYPE_UNSPECIFIED"`)

* `AHEAD` (value: `"PACING_TYPE_AHEAD"`)

* `ASAP` (value: `"PACING_TYPE_ASAP"`)

* `EVEN` (value: `"PACING_TYPE_EVEN"`)




