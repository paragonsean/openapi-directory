# AzureMediaServices.JobOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**odataType** | **String** | The discriminator for derived types. | 
**error** | [**JobError**](JobError.md) |  | [optional] 
**progress** | **Number** | If the JobOutput is in a Processing state, this contains the job completion percentage.  The value is an estimate and not intended to be used to predict job completion times. To determine if the JobOutput is complete, use the State property. | [optional] [readonly] 
**state** | **String** | Describes the state of the JobOutput. | [optional] [readonly] 



## Enum: StateEnum


* `Canceled` (value: `"Canceled"`)

* `Canceling` (value: `"Canceling"`)

* `Error` (value: `"Error"`)

* `Finished` (value: `"Finished"`)

* `Processing` (value: `"Processing"`)

* `Queued` (value: `"Queued"`)

* `Scheduled` (value: `"Scheduled"`)




