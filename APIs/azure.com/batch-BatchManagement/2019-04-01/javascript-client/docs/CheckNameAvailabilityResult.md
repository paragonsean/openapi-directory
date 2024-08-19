# BatchManagement.CheckNameAvailabilityResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | Gets an error message explaining the Reason value in more detail. | [optional] [readonly] 
**nameAvailable** | **Boolean** | Gets a boolean value that indicates whether the name is available for you to use. If true, the name is available. If false, the name has already been taken or invalid and cannot be used. | [optional] [readonly] 
**reason** | **String** | Gets the reason that a Batch account name could not be used. The Reason element is only returned if NameAvailable is false. | [optional] [readonly] 



## Enum: ReasonEnum


* `Invalid` (value: `"Invalid"`)

* `AlreadyExists` (value: `"AlreadyExists"`)




