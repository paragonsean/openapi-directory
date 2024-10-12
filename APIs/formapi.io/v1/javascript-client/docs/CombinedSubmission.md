# ApiV1.CombinedSubmission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[CombinedSubmissionAction]**](CombinedSubmissionAction.md) |  | [optional] 
**downloadUrl** | **String** |  | [optional] 
**errorMessage** | **String** |  | [optional] 
**expired** | **Boolean** |  | 
**expiresAt** | **String** |  | [optional] 
**expiresIn** | **Number** |  | [optional] 
**id** | **String** |  | 
**metadata** | **Object** |  | [optional] 
**password** | **String** |  | [optional] 
**pdfHash** | **String** |  | [optional] 
**sourcePdfs** | [**[CombinedSubmissionSourcePdfsInner]**](CombinedSubmissionSourcePdfsInner.md) |  | 
**state** | **String** |  | 
**submissionIds** | **[String]** |  | 



## Enum: StateEnum


* `pending` (value: `"pending"`)

* `processed` (value: `"processed"`)

* `error` (value: `"error"`)




