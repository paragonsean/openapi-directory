# LgtmApiSpecification.LanguageStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | **Number** | The number of alerts for this language. | [optional] 
**analysisDate** | **Date** | The time the commit was analyzed. | [optional] 
**commitDate** | **Date** | The time of the commit. | [optional] 
**commitId** | **String** | The latest successfully analyzed commit for the language. All statistics refer to this commit. | [optional] 
**language** | **String** | The short name for the language. | [optional] 
**lines** | **Number** | The number of lines of code for this language. | [optional] 
**status** | **String** | The status of the analysis of this language. | [optional] 



## Enum: StatusEnum


* `success` (value: `"success"`)

* `failure` (value: `"failure"`)

* `pending` (value: `"pending"`)




