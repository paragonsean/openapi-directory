

# TestExecution

A single test executed in a single environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**environment** | [**Environment**](Environment.md) |  |  [optional] |
|**id** | **String** | Output only. Unique id set by the service. |  [optional] |
|**matrixId** | **String** | Output only. Id of the containing TestMatrix. |  [optional] |
|**projectId** | **String** | Output only. The cloud project that owns the test execution. |  [optional] |
|**shard** | [**Shard**](Shard.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Indicates the current progress of the test execution (e.g., FINISHED). |  [optional] |
|**testDetails** | [**TestDetails**](TestDetails.md) |  |  [optional] |
|**testSpecification** | [**TestSpecification**](TestSpecification.md) |  |  [optional] |
|**timestamp** | **String** | Output only. The time this test execution was initially created. |  [optional] |
|**toolResultsStep** | [**ToolResultsStep**](ToolResultsStep.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| TEST_STATE_UNSPECIFIED | &quot;TEST_STATE_UNSPECIFIED&quot; |
| VALIDATING | &quot;VALIDATING&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| FINISHED | &quot;FINISHED&quot; |
| ERROR | &quot;ERROR&quot; |
| UNSUPPORTED_ENVIRONMENT | &quot;UNSUPPORTED_ENVIRONMENT&quot; |
| INCOMPATIBLE_ENVIRONMENT | &quot;INCOMPATIBLE_ENVIRONMENT&quot; |
| INCOMPATIBLE_ARCHITECTURE | &quot;INCOMPATIBLE_ARCHITECTURE&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| INVALID | &quot;INVALID&quot; |



