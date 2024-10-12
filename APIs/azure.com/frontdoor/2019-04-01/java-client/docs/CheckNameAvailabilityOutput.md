

# CheckNameAvailabilityOutput

Output of check name availability API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | The detailed error message describing why the name is not available. |  [optional] [readonly] |
|**nameAvailability** | [**NameAvailabilityEnum**](#NameAvailabilityEnum) | Indicates whether the name is available. |  [optional] [readonly] |
|**reason** | **String** | The reason why the name is not available. |  [optional] [readonly] |



## Enum: NameAvailabilityEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;Available&quot; |
| UNAVAILABLE | &quot;Unavailable&quot; |



