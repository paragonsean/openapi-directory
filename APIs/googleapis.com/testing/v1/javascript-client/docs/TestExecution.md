# CloudTestingApi.TestExecution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**Environment**](Environment.md) |  | [optional] 
**id** | **String** | Output only. Unique id set by the service. | [optional] 
**matrixId** | **String** | Output only. Id of the containing TestMatrix. | [optional] 
**projectId** | **String** | Output only. The cloud project that owns the test execution. | [optional] 
**shard** | [**Shard**](Shard.md) |  | [optional] 
**state** | **String** | Output only. Indicates the current progress of the test execution (e.g., FINISHED). | [optional] 
**testDetails** | [**TestDetails**](TestDetails.md) |  | [optional] 
**testSpecification** | [**TestSpecification**](TestSpecification.md) |  | [optional] 
**timestamp** | **String** | Output only. The time this test execution was initially created. | [optional] 
**toolResultsStep** | [**ToolResultsStep**](ToolResultsStep.md) |  | [optional] 



## Enum: StateEnum


* `TEST_STATE_UNSPECIFIED` (value: `"TEST_STATE_UNSPECIFIED"`)

* `VALIDATING` (value: `"VALIDATING"`)

* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `FINISHED` (value: `"FINISHED"`)

* `ERROR` (value: `"ERROR"`)

* `UNSUPPORTED_ENVIRONMENT` (value: `"UNSUPPORTED_ENVIRONMENT"`)

* `INCOMPATIBLE_ENVIRONMENT` (value: `"INCOMPATIBLE_ENVIRONMENT"`)

* `INCOMPATIBLE_ARCHITECTURE` (value: `"INCOMPATIBLE_ARCHITECTURE"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `INVALID` (value: `"INVALID"`)




