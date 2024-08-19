# WorkflowExecutionsApi.StepEntryMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**progressNumber** | **String** | Progress number represents the current state of the current progress. eg: A step entry represents the 4th iteration in a progress of PROGRESS_TYPE_FOR. | [optional] 
**progressType** | **String** | Progress type of this step entry. | [optional] 
**threadId** | **String** | Child thread id that this step entry belongs to. | [optional] 



## Enum: ProgressTypeEnum


* `UNSPECIFIED` (value: `"PROGRESS_TYPE_UNSPECIFIED"`)

* `FOR` (value: `"PROGRESS_TYPE_FOR"`)

* `SWITCH` (value: `"PROGRESS_TYPE_SWITCH"`)

* `RETRY` (value: `"PROGRESS_TYPE_RETRY"`)

* `PARALLEL_FOR` (value: `"PROGRESS_TYPE_PARALLEL_FOR"`)

* `PARALLEL_BRANCH` (value: `"PROGRESS_TYPE_PARALLEL_BRANCH"`)




