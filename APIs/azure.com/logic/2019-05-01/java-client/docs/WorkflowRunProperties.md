

# WorkflowRunProperties

The workflow run properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | Gets the code. |  [optional] [readonly] |
|**correlation** | [**Correlation**](Correlation.md) |  |  [optional] |
|**correlationId** | **String** | Gets the correlation id. |  [optional] [readonly] |
|**endTime** | **OffsetDateTime** | Gets the end time. |  [optional] [readonly] |
|**error** | **Object** |  |  [optional] |
|**outputs** | [**Map&lt;String, WorkflowOutputParameter&gt;**](WorkflowOutputParameter.md) | Gets the outputs. |  [optional] [readonly] |
|**response** | [**WorkflowRunTrigger**](WorkflowRunTrigger.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | Gets the start time. |  [optional] [readonly] |
|**status** | **WorkflowStatus** |  |  [optional] |
|**trigger** | [**WorkflowRunTrigger**](WorkflowRunTrigger.md) |  |  [optional] |
|**waitEndTime** | **OffsetDateTime** | Gets the wait end time. |  [optional] [readonly] |
|**workflow** | [**ResourceReference**](ResourceReference.md) |  |  [optional] |



