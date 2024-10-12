# KeyVaultManagementClient.CheckNameAvailabilityResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | An error message explaining the Reason value in more detail. | [optional] [readonly] 
**nameAvailable** | **Boolean** | A boolean value that indicates whether the name is available for you to use. If true, the name is available. If false, the name has already been taken or is invalid and cannot be used. | [optional] [readonly] 
**reason** | **String** | The reason that a vault name could not be used. The Reason element is only returned if NameAvailable is false. | [optional] [readonly] 



## Enum: ReasonEnum


* `AccountNameInvalid` (value: `"AccountNameInvalid"`)

* `AlreadyExists` (value: `"AlreadyExists"`)




