

# CheckNameAvailabilityResponse

A response indicating whether the specified name for a resource is available.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**available** | **Boolean** | True if the name is available, otherwise false. |  [optional] [readonly] |
|**message** | **String** | A message explaining why the name is unavailable. Will be null if the name is available. |  [optional] [readonly] |
|**name** | **String** | The name whose availability was checked. |  [optional] [readonly] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason code explaining why the name is unavailable. Will be null if the name is available. |  [optional] [readonly] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| ALREADY_EXISTS | &quot;AlreadyExists&quot; |



