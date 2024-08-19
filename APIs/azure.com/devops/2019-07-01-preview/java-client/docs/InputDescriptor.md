

# InputDescriptor

Representation of a pipeline template input parameter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the input parameter. |  [optional] |
|**id** | **String** | Identifier of the input parameter. |  |
|**possibleValues** | [**List&lt;InputValue&gt;**](InputValue.md) | List of possible values for the input parameter. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Data type of the value of the input parameter. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| STRING | &quot;String&quot; |
| SECURE_STRING | &quot;SecureString&quot; |
| INT | &quot;Int&quot; |
| BOOL | &quot;Bool&quot; |
| AUTHORIZATION | &quot;Authorization&quot; |



