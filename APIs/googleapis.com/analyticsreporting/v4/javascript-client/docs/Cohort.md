# AnalyticsReportingApi.Cohort

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateRange** | [**DateRange**](DateRange.md) |  | [optional] 
**name** | **String** | A unique name for the cohort. If not defined name will be auto-generated with values cohort_[1234...]. | [optional] 
**type** | **String** | Type of the cohort. The only supported type as of now is &#x60;FIRST_VISIT_DATE&#x60;. If this field is unspecified the cohort is treated as &#x60;FIRST_VISIT_DATE&#x60; type cohort. | [optional] 



## Enum: TypeEnum


* `UNSPECIFIED_COHORT_TYPE` (value: `"UNSPECIFIED_COHORT_TYPE"`)

* `FIRST_VISIT_DATE` (value: `"FIRST_VISIT_DATE"`)




