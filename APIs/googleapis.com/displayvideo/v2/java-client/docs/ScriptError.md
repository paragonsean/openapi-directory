

# ScriptError

An error message for a custom bidding script.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**column** | **String** | The column number in the script where the error was thrown. |  [optional] |
|**errorCode** | [**ErrorCodeEnum**](#ErrorCodeEnum) | The type of error. |  [optional] |
|**errorMessage** | **String** | The detailed error message. |  [optional] |
|**line** | **String** | The line number in the script where the error was thrown. |  [optional] |



## Enum: ErrorCodeEnum

| Name | Value |
|---- | -----|
| ERROR_CODE_UNSPECIFIED | &quot;ERROR_CODE_UNSPECIFIED&quot; |
| SYNTAX_ERROR | &quot;SYNTAX_ERROR&quot; |
| DEPRECATED_SYNTAX | &quot;DEPRECATED_SYNTAX&quot; |
| INTERNAL_ERROR | &quot;INTERNAL_ERROR&quot; |



