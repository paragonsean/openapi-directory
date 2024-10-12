

# ImageTemplateLastRunStatus

Describes the latest status of running an image template

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | End time of the last run (UTC) |  [optional] |
|**message** | **String** | Verbose information about the last run state |  [optional] |
|**runState** | [**RunStateEnum**](#RunStateEnum) | State of the last run |  [optional] |
|**runSubState** | [**RunSubStateEnum**](#RunSubStateEnum) | Sub-state of the last run |  [optional] |
|**startTime** | **OffsetDateTime** | Start time of the last run (UTC) |  [optional] |



## Enum: RunStateEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;Running&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| PARTIALLY_SUCCEEDED | &quot;PartiallySucceeded&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: RunSubStateEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;Queued&quot; |
| BUILDING | &quot;Building&quot; |
| CUSTOMIZING | &quot;Customizing&quot; |
| DISTRIBUTING | &quot;Distributing&quot; |



