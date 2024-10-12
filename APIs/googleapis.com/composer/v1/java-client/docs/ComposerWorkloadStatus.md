

# ComposerWorkloadStatus

Workload status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detailedStatusMessage** | **String** | Output only. Detailed message of the status. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Workload state. |  [optional] [readonly] |
|**statusMessage** | **String** | Output only. Text to provide more descriptive status. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| COMPOSER_WORKLOAD_STATE_UNSPECIFIED | &quot;COMPOSER_WORKLOAD_STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| OK | &quot;OK&quot; |
| WARNING | &quot;WARNING&quot; |
| ERROR | &quot;ERROR&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |



