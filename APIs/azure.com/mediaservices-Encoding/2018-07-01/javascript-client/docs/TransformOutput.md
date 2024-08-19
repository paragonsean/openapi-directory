# AzureMediaServices.TransformOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**onError** | **String** | A Transform can define more than one outputs. This property defines what the service should do when one output fails - either continue to produce other outputs, or, stop the other outputs. The overall Job state will not reflect failures of outputs that are specified with &#39;ContinueJob&#39;. The default is &#39;StopProcessingJob&#39;. | [optional] 
**preset** | [**Preset**](Preset.md) |  | 
**relativePriority** | **String** | Sets the relative priority of the TransformOutputs within a Transform. This sets the priority that the service uses for processing TransformOutputs. The default priority is Normal. | [optional] 



## Enum: OnErrorEnum


* `StopProcessingJob` (value: `"StopProcessingJob"`)

* `ContinueJob` (value: `"ContinueJob"`)





## Enum: RelativePriorityEnum


* `Low` (value: `"Low"`)

* `Normal` (value: `"Normal"`)

* `High` (value: `"High"`)




