

# BuildSystemSharedInterfacesIActivityRunStatus

Declares members of objects that communicate the progress of an               asynchronous activity run.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentStep** | **Integer** | Gets or sets the number of the step the activity is currently running. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Gets or sets the status of the activity run. |  [optional] |
|**stepProgress** | **Integer** | Gets or sets a measurement of the current progress of the current step. |  [optional] |
|**stepStatus** | **String** | Gets or sets a description of the current status of the currently               running step. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| READY | &quot;Ready&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| FAILED | &quot;Failed&quot; |



