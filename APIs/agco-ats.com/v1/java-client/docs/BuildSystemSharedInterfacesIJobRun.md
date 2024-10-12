

# BuildSystemSharedInterfacesIJobRun

interface of JobRun

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityRuns** | [**List&lt;BuildSystemSharedInterfacesIActivityRun&gt;**](BuildSystemSharedInterfacesIActivityRun.md) | ActivityRuns |  [optional] |
|**endDate** | **OffsetDateTime** | end date |  [optional] |
|**jobID** | **Integer** | job id |  [optional] |
|**jobRunID** | **Integer** | JobRunID |  [optional] [readonly] |
|**parameters** | [**List&lt;BuildSystemSharedInterfacesIParameterValue&gt;**](BuildSystemSharedInterfacesIParameterValue.md) | Parameters |  [optional] [readonly] |
|**startDate** | **OffsetDateTime** | Start Date |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | status |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| READY | &quot;Ready&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| FAILED | &quot;Failed&quot; |



