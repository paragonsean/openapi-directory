

# HeaderAction

An action that can manipulate an http header.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**headerActionType** | [**HeaderActionTypeEnum**](#HeaderActionTypeEnum) | Which type of manipulation to apply to the header. |  |
|**headerName** | **String** | The name of the header this action will apply to. |  |
|**value** | **String** | The value to update the given header name with. This value is not used if the actionType is Delete. |  [optional] |



## Enum: HeaderActionTypeEnum

| Name | Value |
|---- | -----|
| APPEND | &quot;Append&quot; |
| DELETE | &quot;Delete&quot; |
| OVERWRITE | &quot;Overwrite&quot; |



