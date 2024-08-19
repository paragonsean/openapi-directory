

# TransformOutput

Describes the properties of a TransformOutput, which are the rules to be applied while generating the desired output.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**onError** | [**OnErrorEnum**](#OnErrorEnum) | A Transform can define more than one outputs. This property defines what the service should do when one output fails - either continue to produce other outputs, or, stop the other outputs. The default is stop. |  [optional] |
|**preset** | [**Preset**](Preset.md) |  |  |
|**relativePriority** | [**RelativePriorityEnum**](#RelativePriorityEnum) | Sets the relative priority of the TransformOutputs within a Transform. This sets the priority that the service uses for processing TransformOutputs. The default priority is Normal. |  [optional] |



## Enum: OnErrorEnum

| Name | Value |
|---- | -----|
| STOP_PROCESSING_JOB | &quot;StopProcessingJob&quot; |
| CONTINUE_JOB | &quot;ContinueJob&quot; |



## Enum: RelativePriorityEnum

| Name | Value |
|---- | -----|
| LOW | &quot;Low&quot; |
| NORMAL | &quot;Normal&quot; |
| HIGH | &quot;High&quot; |



