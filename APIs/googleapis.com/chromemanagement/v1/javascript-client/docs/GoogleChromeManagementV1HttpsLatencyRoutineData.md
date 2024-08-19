# ChromeManagementApi.GoogleChromeManagementV1HttpsLatencyRoutineData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latency** | **String** | Output only. HTTPS latency if routine succeeded or failed because of HIGH_LATENCY or VERY_HIGH_LATENCY. | [optional] [readonly] 
**problem** | **String** | Output only. HTTPS latency routine problem if a problem occurred. | [optional] [readonly] 



## Enum: ProblemEnum


* `HTTPS_LATENCY_PROBLEM_UNSPECIFIED` (value: `"HTTPS_LATENCY_PROBLEM_UNSPECIFIED"`)

* `FAILED_DNS_RESOLUTIONS` (value: `"FAILED_DNS_RESOLUTIONS"`)

* `FAILED_HTTPS_REQUESTS` (value: `"FAILED_HTTPS_REQUESTS"`)

* `HIGH_LATENCY` (value: `"HIGH_LATENCY"`)

* `VERY_HIGH_LATENCY` (value: `"VERY_HIGH_LATENCY"`)




