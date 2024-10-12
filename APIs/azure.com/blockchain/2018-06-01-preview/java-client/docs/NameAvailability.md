

# NameAvailability

Name availability payload which is exposed in the response of the resource provider.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | Gets or sets the message. |  [optional] |
|**nameAvailable** | **Boolean** | Gets or sets the value indicating whether the name is available. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Gets or sets the name availability reason. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| ALREADY_EXISTS | &quot;AlreadyExists&quot; |
| INVALID | &quot;Invalid&quot; |



