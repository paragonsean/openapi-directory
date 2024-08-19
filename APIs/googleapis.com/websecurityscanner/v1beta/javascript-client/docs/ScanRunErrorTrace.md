# WebSecurityScannerApi.ScanRunErrorTrace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Indicates the error reason code. | [optional] 
**mostCommonHttpErrorCode** | **Number** | If the scan encounters TOO_MANY_HTTP_ERRORS, this field indicates the most common HTTP error code, if such is available. For example, if this code is 404, the scan has encountered too many NOT_FOUND responses. | [optional] 
**scanConfigError** | [**ScanConfigError**](ScanConfigError.md) |  | [optional] 



## Enum: CodeEnum


* `CODE_UNSPECIFIED` (value: `"CODE_UNSPECIFIED"`)

* `INTERNAL_ERROR` (value: `"INTERNAL_ERROR"`)

* `SCAN_CONFIG_ISSUE` (value: `"SCAN_CONFIG_ISSUE"`)

* `AUTHENTICATION_CONFIG_ISSUE` (value: `"AUTHENTICATION_CONFIG_ISSUE"`)

* `TIMED_OUT_WHILE_SCANNING` (value: `"TIMED_OUT_WHILE_SCANNING"`)

* `TOO_MANY_REDIRECTS` (value: `"TOO_MANY_REDIRECTS"`)

* `TOO_MANY_HTTP_ERRORS` (value: `"TOO_MANY_HTTP_ERRORS"`)

* `STARTING_URLS_CRAWL_HTTP_ERRORS` (value: `"STARTING_URLS_CRAWL_HTTP_ERRORS"`)




