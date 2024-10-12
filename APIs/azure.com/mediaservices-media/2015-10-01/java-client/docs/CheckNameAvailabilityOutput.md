

# CheckNameAvailabilityOutput

The response body for CheckNameAvailability API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | Specifies the detailed reason if the name is not available. |  [optional] |
|**nameAvailable** | **Boolean** | Specifies if the name is available. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Specifies the reason if the name is not available. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| INVALID | &quot;Invalid&quot; |
| ALREADY_EXISTS | &quot;AlreadyExists&quot; |



