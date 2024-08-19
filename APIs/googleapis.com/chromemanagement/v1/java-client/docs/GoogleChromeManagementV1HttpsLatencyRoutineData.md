

# GoogleChromeManagementV1HttpsLatencyRoutineData

Data that describes the result of the HTTPS latency diagnostics routine, with the HTTPS requests issued to Google websites.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**latency** | **String** | Output only. HTTPS latency if routine succeeded or failed because of HIGH_LATENCY or VERY_HIGH_LATENCY. |  [optional] [readonly] |
|**problem** | [**ProblemEnum**](#ProblemEnum) | Output only. HTTPS latency routine problem if a problem occurred. |  [optional] [readonly] |



## Enum: ProblemEnum

| Name | Value |
|---- | -----|
| HTTPS_LATENCY_PROBLEM_UNSPECIFIED | &quot;HTTPS_LATENCY_PROBLEM_UNSPECIFIED&quot; |
| FAILED_DNS_RESOLUTIONS | &quot;FAILED_DNS_RESOLUTIONS&quot; |
| FAILED_HTTPS_REQUESTS | &quot;FAILED_HTTPS_REQUESTS&quot; |
| HIGH_LATENCY | &quot;HIGH_LATENCY&quot; |
| VERY_HIGH_LATENCY | &quot;VERY_HIGH_LATENCY&quot; |



