# GoogleAnalyticsDataApi.CohortsRange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endOffset** | **Number** | Required. &#x60;endOffset&#x60; specifies the end date of the extended reporting date range for a cohort report. &#x60;endOffset&#x60; can be any positive integer but is commonly set to 5 to 10 so that reports contain data on the cohort for the next several granularity time periods. If &#x60;granularity&#x60; is &#x60;DAILY&#x60;, the &#x60;endDate&#x60; of the extended reporting date range is &#x60;endDate&#x60; of the cohort plus &#x60;endOffset&#x60; days. If &#x60;granularity&#x60; is &#x60;WEEKLY&#x60;, the &#x60;endDate&#x60; of the extended reporting date range is &#x60;endDate&#x60; of the cohort plus &#x60;endOffset * 7&#x60; days. If &#x60;granularity&#x60; is &#x60;MONTHLY&#x60;, the &#x60;endDate&#x60; of the extended reporting date range is &#x60;endDate&#x60; of the cohort plus &#x60;endOffset * 30&#x60; days. | [optional] 
**granularity** | **String** | Required. The granularity used to interpret the &#x60;startOffset&#x60; and &#x60;endOffset&#x60; for the extended reporting date range for a cohort report. | [optional] 
**startOffset** | **Number** | &#x60;startOffset&#x60; specifies the start date of the extended reporting date range for a cohort report. &#x60;startOffset&#x60; is commonly set to 0 so that reports contain data from the acquisition of the cohort forward. If &#x60;granularity&#x60; is &#x60;DAILY&#x60;, the &#x60;startDate&#x60; of the extended reporting date range is &#x60;startDate&#x60; of the cohort plus &#x60;startOffset&#x60; days. If &#x60;granularity&#x60; is &#x60;WEEKLY&#x60;, the &#x60;startDate&#x60; of the extended reporting date range is &#x60;startDate&#x60; of the cohort plus &#x60;startOffset * 7&#x60; days. If &#x60;granularity&#x60; is &#x60;MONTHLY&#x60;, the &#x60;startDate&#x60; of the extended reporting date range is &#x60;startDate&#x60; of the cohort plus &#x60;startOffset * 30&#x60; days. | [optional] 



## Enum: GranularityEnum


* `GRANULARITY_UNSPECIFIED` (value: `"GRANULARITY_UNSPECIFIED"`)

* `DAILY` (value: `"DAILY"`)

* `WEEKLY` (value: `"WEEKLY"`)

* `MONTHLY` (value: `"MONTHLY"`)




