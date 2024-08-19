

# StepEntryMetadata

StepEntryMetadata contains metadata information about this step.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**progressNumber** | **String** | Progress number represents the current state of the current progress. eg: A step entry represents the 4th iteration in a progress of PROGRESS_TYPE_FOR. |  [optional] |
|**progressType** | [**ProgressTypeEnum**](#ProgressTypeEnum) | Progress type of this step entry. |  [optional] |
|**threadId** | **String** | Child thread id that this step entry belongs to. |  [optional] |



## Enum: ProgressTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PROGRESS_TYPE_UNSPECIFIED&quot; |
| FOR | &quot;PROGRESS_TYPE_FOR&quot; |
| SWITCH | &quot;PROGRESS_TYPE_SWITCH&quot; |
| RETRY | &quot;PROGRESS_TYPE_RETRY&quot; |
| PARALLEL_FOR | &quot;PROGRESS_TYPE_PARALLEL_FOR&quot; |
| PARALLEL_BRANCH | &quot;PROGRESS_TYPE_PARALLEL_BRANCH&quot; |



