

# GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageSegmentationMetadata


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**costMilliNodeHours** | **String** | The actual training cost of creating this model, expressed in milli node hours, i.e. 1,000 value in this field means 1 node hour. Guaranteed to not exceed inputs.budgetMilliNodeHours. |  [optional] |
|**successfulStopReason** | [**SuccessfulStopReasonEnum**](#SuccessfulStopReasonEnum) | For successful job completions, this is the reason why the job has finished. |  [optional] |



## Enum: SuccessfulStopReasonEnum

| Name | Value |
|---- | -----|
| SUCCESSFUL_STOP_REASON_UNSPECIFIED | &quot;SUCCESSFUL_STOP_REASON_UNSPECIFIED&quot; |
| BUDGET_REACHED | &quot;BUDGET_REACHED&quot; |
| MODEL_CONVERGED | &quot;MODEL_CONVERGED&quot; |



