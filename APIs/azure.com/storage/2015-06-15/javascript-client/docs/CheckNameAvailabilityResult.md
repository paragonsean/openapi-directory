# StorageManagement.CheckNameAvailabilityResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | The error message explaining the Reason value in more detail. | [optional] 
**nameAvailable** | **Boolean** | Boolean value that indicates whether the name is available for you to use. If true, the name is available. If false, the name has already been taken or is invalid and cannot be used. | [optional] 
**reason** | **String** | The reason that a storage account name could not be used. The Reason element is only returned if NameAvailable is false. | [optional] 



## Enum: ReasonEnum


* `AccountNameInvalid` (value: `"AccountNameInvalid"`)

* `AlreadyExists` (value: `"AlreadyExists"`)




