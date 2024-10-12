

# Workflow

A workflow is a collection of multiple dependent Glue jobs and crawlers that are run to complete a complex ETL task. A workflow manages the execution and monitoring of all its jobs and crawlers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**defaultRunProperties** | [**Map**](Map.md) |  |  [optional] |
|**createdOn** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModifiedOn** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastRun** | [**WorkflowLastRun**](WorkflowLastRun.md) |  |  [optional] |
|**graph** | [**WorkflowGraph**](WorkflowGraph.md) |  |  [optional] |
|**maxConcurrentRuns** | [**Integer**](Integer.md) |  |  [optional] |
|**blueprintDetails** | [**WorkflowBlueprintDetails**](WorkflowBlueprintDetails.md) |  |  [optional] |



