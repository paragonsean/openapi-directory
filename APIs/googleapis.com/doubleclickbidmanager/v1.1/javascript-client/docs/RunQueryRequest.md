# DoubleClickBidManagerApi.RunQueryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataRange** | **String** | Report data range used to generate the report. | [optional] 
**reportDataEndTimeMs** | **String** | The ending time for the data that is shown in the report. Note, reportDataEndTimeMs is required if dataRange is CUSTOM_DATES and ignored otherwise. | [optional] 
**reportDataStartTimeMs** | **String** | The starting time for the data that is shown in the report. Note, reportDataStartTimeMs is required if dataRange is CUSTOM_DATES and ignored otherwise. | [optional] 
**timezoneCode** | **String** | Canonical timezone code for report data time. Defaults to America/New_York. | [optional] 



## Enum: DataRangeEnum


* `CUSTOM_DATES` (value: `"CUSTOM_DATES"`)

* `CURRENT_DAY` (value: `"CURRENT_DAY"`)

* `PREVIOUS_DAY` (value: `"PREVIOUS_DAY"`)

* `WEEK_TO_DATE` (value: `"WEEK_TO_DATE"`)

* `MONTH_TO_DATE` (value: `"MONTH_TO_DATE"`)

* `QUARTER_TO_DATE` (value: `"QUARTER_TO_DATE"`)

* `YEAR_TO_DATE` (value: `"YEAR_TO_DATE"`)

* `PREVIOUS_WEEK` (value: `"PREVIOUS_WEEK"`)

* `PREVIOUS_HALF_MONTH` (value: `"PREVIOUS_HALF_MONTH"`)

* `PREVIOUS_MONTH` (value: `"PREVIOUS_MONTH"`)

* `PREVIOUS_QUARTER` (value: `"PREVIOUS_QUARTER"`)

* `PREVIOUS_YEAR` (value: `"PREVIOUS_YEAR"`)

* `LAST_7_DAYS` (value: `"LAST_7_DAYS"`)

* `LAST_30_DAYS` (value: `"LAST_30_DAYS"`)

* `LAST_90_DAYS` (value: `"LAST_90_DAYS"`)

* `LAST_365_DAYS` (value: `"LAST_365_DAYS"`)

* `ALL_TIME` (value: `"ALL_TIME"`)

* `LAST_14_DAYS` (value: `"LAST_14_DAYS"`)

* `TYPE_NOT_SUPPORTED` (value: `"TYPE_NOT_SUPPORTED"`)

* `LAST_60_DAYS` (value: `"LAST_60_DAYS"`)




