# AzureSqlDatabase.CheckNameAvailabilityResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **Boolean** | True if the name is available, otherwise false. | [optional] [readonly] 
**message** | **String** | A message explaining why the name is unavailable. Will be null if the name is available. | [optional] [readonly] 
**name** | **String** | The name whose availability was checked. | [optional] [readonly] 
**reason** | **String** | The reason code explaining why the name is unavailable. Will be null if the name is available. | [optional] [readonly] 



## Enum: ReasonEnum


* `Invalid` (value: `"Invalid"`)

* `AlreadyExists` (value: `"AlreadyExists"`)




