# AzureMediaServices.JobOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**odataType** | **String** | The discriminator for derived types. | 
**error** | [**JobError**](JobError.md) |  | [optional] 
**label** | **String** | A label that is assigned to a JobOutput in order to help uniquely identify it. This is useful when your Transform has more than one TransformOutput, whereby your Job has more than one JobOutput. In such cases, when you submit the Job, you will add two or more JobOutputs, in the same order as TransformOutputs in the Transform. Subsequently, when you retrieve the Job, either through events or on a GET request, you can use the label to easily identify the JobOutput. If a label is not provided, a default value of &#39;{presetName}_{outputIndex}&#39; will be used, where the preset name is the name of the preset in the corresponding TransformOutput and the output index is the relative index of the this JobOutput within the Job. Note that this index is the same as the relative index of the corresponding TransformOutput within its Transform. | [optional] 
**progress** | **Number** | If the JobOutput is in a Processing state, this contains the Job completion percentage. The value is an estimate and not intended to be used to predict Job completion times. To determine if the JobOutput is complete, use the State property. | [optional] [readonly] 
**state** | **String** | Describes the state of the JobOutput. | [optional] [readonly] 



## Enum: StateEnum


* `Canceled` (value: `"Canceled"`)

* `Canceling` (value: `"Canceling"`)

* `Error` (value: `"Error"`)

* `Finished` (value: `"Finished"`)

* `Processing` (value: `"Processing"`)

* `Queued` (value: `"Queued"`)

* `Scheduled` (value: `"Scheduled"`)




