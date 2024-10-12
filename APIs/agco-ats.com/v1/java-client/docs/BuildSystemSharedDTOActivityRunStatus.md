

# BuildSystemSharedDTOActivityRunStatus

A DTO for an IActivityRunStatus

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentStep** | **Integer** | The activity step currently executing, indicated by numeric order |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the ActivityRun |  [optional] |
|**stepProgress** | **Integer** | The percent progress from the currently executing step.  This value shall be null if progress is not available |  [optional] |
|**stepStatus** | **String** | The status text from the currently executing step |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| READY | &quot;Ready&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| FAILED | &quot;Failed&quot; |



