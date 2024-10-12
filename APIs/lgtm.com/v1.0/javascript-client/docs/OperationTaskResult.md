# LgtmApiSpecification.OperationTaskResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitId** | **String** | The commit identifier. The commit identifier is included only if the same commit was successfully analyzed for all languages. A detailed breakdown of which commit was analyzed for each language is provided in the &#x60;languages&#x60; property.  | [optional] 
**id** | **String** | The identifier for the QueryJob. | [optional] 
**languages** | [**[CodereviewLanguages]**](CodereviewLanguages.md) | Detailed information for each language analyzed. | [optional] 
**logUrl** | **String** | A page on LGTM to view the logs for this analysis. | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**resultsUrl** | **String** | A page on LGTM to view the status and results of this code review. | [optional] 
**status** | **String** | The status of the code review. | [optional] 
**statusMessage** | **String** | A summary of the current status of the code review. | [optional] 
**resultUrl** | **String** | URL to view the result of the query job. | [optional] 
**stats** | [**QueryjobStats**](QueryjobStats.md) |  | [optional] 



## Enum: StatusEnum


* `pending` (value: `"pending"`)

* `failure` (value: `"failure"`)

* `success` (value: `"success"`)




