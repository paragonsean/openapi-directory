# CloudSearchApi.ProcessingError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Error code indicating the nature of the error. | [optional] 
**errorMessage** | **String** | The description of the error. | [optional] 
**fieldViolations** | [**[FieldViolation]**](FieldViolation.md) | In case the item fields are invalid, this field contains the details about the validation errors. | [optional] 



## Enum: CodeEnum


* `PROCESSING_ERROR_CODE_UNSPECIFIED` (value: `"PROCESSING_ERROR_CODE_UNSPECIFIED"`)

* `MALFORMED_REQUEST` (value: `"MALFORMED_REQUEST"`)

* `UNSUPPORTED_CONTENT_FORMAT` (value: `"UNSUPPORTED_CONTENT_FORMAT"`)

* `INDIRECT_BROKEN_ACL` (value: `"INDIRECT_BROKEN_ACL"`)

* `ACL_CYCLE` (value: `"ACL_CYCLE"`)




