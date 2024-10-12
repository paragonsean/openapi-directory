

# ProcessingError


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Error code indicating the nature of the error. |  [optional] |
|**errorMessage** | **String** | The description of the error. |  [optional] |
|**fieldViolations** | [**List&lt;FieldViolation&gt;**](FieldViolation.md) | In case the item fields are invalid, this field contains the details about the validation errors. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| PROCESSING_ERROR_CODE_UNSPECIFIED | &quot;PROCESSING_ERROR_CODE_UNSPECIFIED&quot; |
| MALFORMED_REQUEST | &quot;MALFORMED_REQUEST&quot; |
| UNSUPPORTED_CONTENT_FORMAT | &quot;UNSUPPORTED_CONTENT_FORMAT&quot; |
| INDIRECT_BROKEN_ACL | &quot;INDIRECT_BROKEN_ACL&quot; |
| ACL_CYCLE | &quot;ACL_CYCLE&quot; |



