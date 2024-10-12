# TextAnalyticsClient.InnerError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Error code. | 
**details** | **{String: String}** | Error details. | [optional] 
**innerError** | [**InnerError**](InnerError.md) |  | [optional] 
**message** | **String** | Error message. | 
**target** | **String** | Error target. | [optional] 



## Enum: CodeEnum


* `invalidParameterValue` (value: `"invalidParameterValue"`)

* `invalidRequestBodyFormat` (value: `"invalidRequestBodyFormat"`)

* `emptyRequest` (value: `"emptyRequest"`)

* `missingInputRecords` (value: `"missingInputRecords"`)

* `invalidDocument` (value: `"invalidDocument"`)

* `modelVersionIncorrect` (value: `"modelVersionIncorrect"`)

* `invalidDocumentBatch` (value: `"invalidDocumentBatch"`)

* `unsupportedLanguageCode` (value: `"unsupportedLanguageCode"`)

* `invalidCountryHint` (value: `"invalidCountryHint"`)




