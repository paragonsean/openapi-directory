# ApiV1.Submission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[SubmissionAction]**](SubmissionAction.md) |  | [optional] 
**batchId** | **String** |  | [optional] 
**data** | **Object** |  | [optional] 
**dataRequests** | [**[SubmissionDataRequest]**](SubmissionDataRequest.md) |  | [optional] 
**downloadUrl** | **String** |  | [optional] 
**editable** | **Boolean** |  | [optional] 
**expired** | **Boolean** |  | 
**expiresAt** | **String** |  | [optional] 
**id** | **String** |  | 
**metadata** | **Object** |  | [optional] 
**pdfHash** | **String** |  | [optional] 
**permanentDownloadUrl** | **String** |  | [optional] 
**processedAt** | **String** |  | [optional] 
**referrer** | **String** |  | [optional] 
**source** | **String** |  | [optional] 
**state** | **String** |  | 
**templateId** | **String** |  | [optional] 
**test** | **Boolean** |  | 
**truncatedText** | **Object** |  | [optional] 



## Enum: StateEnum


* `pending` (value: `"pending"`)

* `processed` (value: `"processed"`)

* `invalid_data` (value: `"invalid_data"`)

* `error` (value: `"error"`)

* `image_download_failed` (value: `"image_download_failed"`)

* `image_processing_failed` (value: `"image_processing_failed"`)

* `waiting_for_data_requests` (value: `"waiting_for_data_requests"`)

* `syntax_error` (value: `"syntax_error"`)

* `account_suspended` (value: `"account_suspended"`)

* `license_revoked` (value: `"license_revoked"`)

* `accidental` (value: `"accidental"`)




