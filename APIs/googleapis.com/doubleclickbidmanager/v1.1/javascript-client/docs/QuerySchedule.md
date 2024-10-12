# DoubleClickBidManagerApi.QuerySchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTimeMs** | **String** | Datetime to periodically run the query until. | [optional] 
**frequency** | **String** | How often the query is run. | [optional] 
**nextRunMinuteOfDay** | **Number** | Time of day at which a new report will be generated, represented as minutes past midnight. Range is 0 to 1439. Only applies to scheduled reports. | [optional] 
**nextRunTimezoneCode** | **String** | Canonical timezone code for report generation time. Defaults to America/New_York. | [optional] 
**startTimeMs** | **String** | When to start running the query. Not applicable to &#x60;ONE_TIME&#x60; frequency. | [optional] 



## Enum: FrequencyEnum


* `ONE_TIME` (value: `"ONE_TIME"`)

* `DAILY` (value: `"DAILY"`)

* `WEEKLY` (value: `"WEEKLY"`)

* `SEMI_MONTHLY` (value: `"SEMI_MONTHLY"`)

* `MONTHLY` (value: `"MONTHLY"`)

* `QUARTERLY` (value: `"QUARTERLY"`)

* `YEARLY` (value: `"YEARLY"`)




