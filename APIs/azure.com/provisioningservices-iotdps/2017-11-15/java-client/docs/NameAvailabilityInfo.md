

# NameAvailabilityInfo

Description of name availability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | message containing a etailed reason name is unavailable |  [optional] |
|**nameAvailable** | **Boolean** | specifies if a name is available or not |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | specifies the reason a name is unavailable |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| ALREADY_EXISTS | &quot;AlreadyExists&quot; |



