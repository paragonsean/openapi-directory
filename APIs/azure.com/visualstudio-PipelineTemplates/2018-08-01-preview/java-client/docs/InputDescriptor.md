

# InputDescriptor

Defines a pipeline template input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of what this input is used for. |  [optional] |
|**id** | **String** | Identifier for the input. |  |
|**possibleValues** | [**List&lt;InputValue&gt;**](InputValue.md) | Possible values that this input can take. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Data type of the input. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| STRING | &quot;String&quot; |
| SECURE_STRING | &quot;SecureString&quot; |
| INT | &quot;Int&quot; |
| BOOL | &quot;Bool&quot; |
| AUTHORIZATION | &quot;Authorization&quot; |



