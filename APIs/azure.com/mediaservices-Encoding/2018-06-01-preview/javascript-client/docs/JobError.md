# AzureMediaServices.JobError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | Helps with categorization of errors. | [optional] [readonly] 
**code** | **String** | Error code describing the error. | [optional] [readonly] 
**details** | [**[JobErrorDetail]**](JobErrorDetail.md) | An array of details about specific errors that led to this reported error. | [optional] [readonly] 
**message** | **String** | A human-readable language-dependent representation of the error. | [optional] [readonly] 
**retry** | **String** | Indicates that it may be possible to retry the Job. If retry is unsuccessful, please contact Azure support via Azure Portal. | [optional] [readonly] 



## Enum: CategoryEnum


* `Service` (value: `"Service"`)

* `Download` (value: `"Download"`)

* `Upload` (value: `"Upload"`)

* `Configuration` (value: `"Configuration"`)

* `Content` (value: `"Content"`)





## Enum: CodeEnum


* `ServiceError` (value: `"ServiceError"`)

* `ServiceTransientError` (value: `"ServiceTransientError"`)

* `DownloadNotAccessible` (value: `"DownloadNotAccessible"`)

* `DownloadTransientError` (value: `"DownloadTransientError"`)

* `UploadNotAccessible` (value: `"UploadNotAccessible"`)

* `UploadTransientError` (value: `"UploadTransientError"`)

* `ConfigurationUnsupported` (value: `"ConfigurationUnsupported"`)

* `ContentMalformed` (value: `"ContentMalformed"`)

* `ContentUnsupported` (value: `"ContentUnsupported"`)





## Enum: RetryEnum


* `DoNotRetry` (value: `"DoNotRetry"`)

* `MayRetry` (value: `"MayRetry"`)




