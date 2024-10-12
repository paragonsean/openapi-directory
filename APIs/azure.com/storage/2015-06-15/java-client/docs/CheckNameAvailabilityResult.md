

# CheckNameAvailabilityResult

The CheckNameAvailability operation response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | The error message explaining the Reason value in more detail. |  [optional] |
|**nameAvailable** | **Boolean** | Boolean value that indicates whether the name is available for you to use. If true, the name is available. If false, the name has already been taken or is invalid and cannot be used. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason that a storage account name could not be used. The Reason element is only returned if NameAvailable is false. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| ACCOUNT_NAME_INVALID | &quot;AccountNameInvalid&quot; |
| ALREADY_EXISTS | &quot;AlreadyExists&quot; |



