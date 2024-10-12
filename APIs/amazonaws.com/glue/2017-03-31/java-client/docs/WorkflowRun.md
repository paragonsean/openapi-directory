

# WorkflowRun

A workflow run is an execution of a workflow providing all the runtime information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  [optional] |
|**workflowRunId** | [**String**](String.md) |  |  [optional] |
|**previousRunId** | [**String**](String.md) |  |  [optional] |
|**workflowRunProperties** | [**Map**](Map.md) |  |  [optional] |
|**startedOn** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**completedOn** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**status** | [**WorkflowRunStatus**](WorkflowRunStatus.md) |  |  [optional] |
|**errorMessage** | [**String**](String.md) |  |  [optional] |
|**statistics** | [**WorkflowRunStatistics**](WorkflowRunStatistics.md) |  |  [optional] |
|**graph** | [**WorkflowGraph**](WorkflowGraph.md) |  |  [optional] |
|**startingEventBatchCondition** | [**WorkflowRunStartingEventBatchCondition**](WorkflowRunStartingEventBatchCondition.md) |  |  [optional] |



