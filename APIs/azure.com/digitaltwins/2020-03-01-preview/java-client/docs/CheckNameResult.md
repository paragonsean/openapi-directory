

# CheckNameResult

The result returned from a check name availability request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | Message indicating an unavailable name due to a conflict, or a description of the naming rules that are violated. |  [optional] |
|**name** | **String** | The name that was checked. |  [optional] |
|**nameAvailable** | **Boolean** | Specifies a Boolean value that indicates if the name is available. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Message providing the reason why the given name is invalid. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| ALREADY_EXISTS | &quot;AlreadyExists&quot; |



