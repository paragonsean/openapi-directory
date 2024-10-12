# RebillyRestApi.InvalidError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **String** | A URI reference [[RFC3986](https://tools.ietf.org/html/rfc3986)] that identifies the problem type. It should provide human-readable documentation for the problem type. When this member is not present, its value is assumed to be \&quot;about:blank\&quot;. | [optional] 
**status** | **Number** | The HTTP status code. | [optional] 
**title** | **String** | A short, human-readable summary of the problem type. It SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization. | [optional] 
**detail** | **String** | A human-readable explanation specific to this occurrence of the problem. | [optional] 
**error** | **String** |  | [optional] 
**invalidFields** | [**[ValidationErrorExtensionsInvalidFieldsInner]**](ValidationErrorExtensionsInvalidFieldsInner.md) |  | [optional] 


