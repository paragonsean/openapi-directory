

# CheckNameAvailabilityResult

The CheckNameAvailability operation response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | An error message explaining the Reason value in more detail. |  [optional] [readonly] |
|**nameAvailable** | **Boolean** | A boolean value that indicates whether the name is available for you to use. If true, the name is available. If false, the name has already been taken or is invalid and cannot be used. |  [optional] [readonly] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason that a vault name could not be used. The Reason element is only returned if NameAvailable is false. |  [optional] [readonly] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| ACCOUNT_NAME_INVALID | &quot;AccountNameInvalid&quot; |
| ALREADY_EXISTS | &quot;AlreadyExists&quot; |



