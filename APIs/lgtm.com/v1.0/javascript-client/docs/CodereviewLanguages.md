# LgtmApiSpecification.CodereviewLanguages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**[CodereviewAlerts]**](CodereviewAlerts.md) | The list of added and fixed alerts per query for this language. | [optional] 
**fixed** | **Number** | The total number of alerts fixed by the patch for this language. | [optional] 
**language** | **String** | The language analyzed. | [optional] 
**_new** | **Number** | The total number of alerts introduced by the patch for this language. | [optional] 
**status** | **String** | The status for analysis of this language. | [optional] 
**statusMessage** | **String** | The current state of analysis of this langauge. When available, a summary of analysis results. | [optional] 



## Enum: StatusEnum


* `pending` (value: `"pending"`)

* `failure` (value: `"failure"`)

* `success` (value: `"success"`)




