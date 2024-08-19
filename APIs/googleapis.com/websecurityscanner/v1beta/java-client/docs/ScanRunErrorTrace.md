

# ScanRunErrorTrace

Output only. Defines an error trace message for a ScanRun.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Indicates the error reason code. |  [optional] |
|**mostCommonHttpErrorCode** | **Integer** | If the scan encounters TOO_MANY_HTTP_ERRORS, this field indicates the most common HTTP error code, if such is available. For example, if this code is 404, the scan has encountered too many NOT_FOUND responses. |  [optional] |
|**scanConfigError** | [**ScanConfigError**](ScanConfigError.md) |  |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| INTERNAL_ERROR | &quot;INTERNAL_ERROR&quot; |
| SCAN_CONFIG_ISSUE | &quot;SCAN_CONFIG_ISSUE&quot; |
| AUTHENTICATION_CONFIG_ISSUE | &quot;AUTHENTICATION_CONFIG_ISSUE&quot; |
| TIMED_OUT_WHILE_SCANNING | &quot;TIMED_OUT_WHILE_SCANNING&quot; |
| TOO_MANY_REDIRECTS | &quot;TOO_MANY_REDIRECTS&quot; |
| TOO_MANY_HTTP_ERRORS | &quot;TOO_MANY_HTTP_ERRORS&quot; |
| STARTING_URLS_CRAWL_HTTP_ERRORS | &quot;STARTING_URLS_CRAWL_HTTP_ERRORS&quot; |



