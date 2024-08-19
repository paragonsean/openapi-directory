# FormRecognizerClient.AnalyzeResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[FormOperationError]**](FormOperationError.md) | List of errors reported during the analyze  operation. | [optional] 
**pages** | [**[ExtractedPage]**](ExtractedPage.md) | Page level information extracted in the analyzed  document. | [optional] 
**status** | **String** | Status of the analyze operation. | [optional] 



## Enum: StatusEnum


* `success` (value: `"success"`)

* `partialSuccess` (value: `"partialSuccess"`)

* `failure` (value: `"failure"`)




