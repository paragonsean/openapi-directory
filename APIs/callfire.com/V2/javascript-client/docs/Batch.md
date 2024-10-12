# CallFireApiDocumentation.Batch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broadcastId** | **Number** | An id of broadcast which batch belongs to | [optional] 
**created** | **Number** | A date and time when batch was created, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] [readonly] 
**enabled** | **Boolean** | An enabled batch. If batch is disabled its contacts remain undialed/untexted | [optional] 
**id** | **Number** | A id of a batch | [optional] 
**name** | **String** | A batch name | [optional] 
**remaining** | **Number** | A number of contacts remaining undialed/untexted | [optional] [readonly] 
**size** | **Number** | A total number of contacts in batch | [optional] [readonly] 
**status** | **String** | A status of batch (NEW, VALIDATING, ERRORS, SOURCE_ERROR, ACTIVE). NEW - batch is queued for validation; VALIDATING - batch is currently validating; ERRORS - batch is processed, some validation errors occurred; SOURCE_ERROR - if contact source is contact list in CallFire system and it has an error; ACTIVE - batch is processed and ready | [optional] 



## Enum: StatusEnum


* `NEW` (value: `"NEW"`)

* `VALIDATING` (value: `"VALIDATING"`)

* `ERRORS` (value: `"ERRORS"`)

* `SOURCE_ERROR` (value: `"SOURCE_ERROR"`)

* `ACTIVE` (value: `"ACTIVE"`)




