

# AppNameAvailabilityInfo

The properties indicating whether a given IoT Central application name is available.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | The detailed reason message. |  [optional] |
|**nameAvailable** | **Boolean** | The value which indicates whether the provided name is available. |  [optional] [readonly] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason for unavailability. |  [optional] [readonly] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| ALREADY_EXISTS | &quot;AlreadyExists&quot; |



