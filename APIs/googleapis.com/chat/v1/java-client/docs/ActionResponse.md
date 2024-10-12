

# ActionResponse

Parameters that a Chat app can use to configure how its response is posted.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dialogAction** | [**DialogAction**](DialogAction.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Input only. The type of Chat app response. |  [optional] |
|**updatedWidget** | [**UpdatedWidget**](UpdatedWidget.md) |  |  [optional] |
|**url** | **String** | Input only. URL for users to authenticate or configure. (Only for &#x60;REQUEST_CONFIG&#x60; response types.) |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| NEW_MESSAGE | &quot;NEW_MESSAGE&quot; |
| UPDATE_MESSAGE | &quot;UPDATE_MESSAGE&quot; |
| UPDATE_USER_MESSAGE_CARDS | &quot;UPDATE_USER_MESSAGE_CARDS&quot; |
| REQUEST_CONFIG | &quot;REQUEST_CONFIG&quot; |
| DIALOG | &quot;DIALOG&quot; |
| UPDATE_WIDGET | &quot;UPDATE_WIDGET&quot; |



