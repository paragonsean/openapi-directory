

# CheckNameAvailabilityResult

The CheckNameAvailability operation response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | Gets an error message explaining the Reason value in more detail. |  [optional] |
|**nameAvailable** | **Boolean** | Gets a boolean value that indicates whether the name is available for you to use. If true, the name is available. If false, the name has already been taken or invalid and cannot be used. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Gets the reason that a storage account name could not be used. The Reason element is only returned if NameAvailable is false. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| ACCOUNT_NAME_INVALID | &quot;AccountNameInvalid&quot; |
| ALREADY_EXISTS | &quot;AlreadyExists&quot; |



