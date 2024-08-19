

# ImageTemplateLastRunStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | End time of the last run (UTC) |  [optional] |
|**message** | **String** | Verbose information about the last run state |  [optional] |
|**runState** | [**RunStateEnum**](#RunStateEnum) | State of the last run |  [optional] |
|**runSubState** | [**RunSubStateEnum**](#RunSubStateEnum) | Sub state of the last run |  [optional] |
|**startTime** | **OffsetDateTime** | Start time of the last run (UTC) |  [optional] |



## Enum: RunStateEnum

| Name | Value |
|---- | -----|
| READY | &quot;ready&quot; |
| RUNNING | &quot;running&quot; |
| SUCCEEDED | &quot;succeeded&quot; |
| PARTIALLY_SUCCEEDED | &quot;partiallySucceeded&quot; |
| FAILED | &quot;failed&quot; |



## Enum: RunSubStateEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;queued&quot; |
| BUILDING | &quot;building&quot; |
| CUSTOMIZING | &quot;customizing&quot; |
| DISTRIBUTING | &quot;distributing&quot; |



