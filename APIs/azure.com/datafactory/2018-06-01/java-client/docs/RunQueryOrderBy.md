

# RunQueryOrderBy

An object to provide order by options for listing runs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**order** | [**OrderEnum**](#OrderEnum) | Sorting order of the parameter. |  |
|**orderBy** | [**OrderByEnum**](#OrderByEnum) | Parameter name to be used for order by. The allowed parameters to order by for pipeline runs are PipelineName, RunStart, RunEnd and Status; for activity runs are ActivityName, ActivityRunStart, ActivityRunEnd and Status; for trigger runs are TriggerName, TriggerRunTimestamp and Status. |  |



## Enum: OrderEnum

| Name | Value |
|---- | -----|
| ASC | &quot;ASC&quot; |
| DESC | &quot;DESC&quot; |



## Enum: OrderByEnum

| Name | Value |
|---- | -----|
| RUN_START | &quot;RunStart&quot; |
| RUN_END | &quot;RunEnd&quot; |
| PIPELINE_NAME | &quot;PipelineName&quot; |
| STATUS | &quot;Status&quot; |
| ACTIVITY_NAME | &quot;ActivityName&quot; |
| ACTIVITY_RUN_START | &quot;ActivityRunStart&quot; |
| ACTIVITY_RUN_END | &quot;ActivityRunEnd&quot; |
| TRIGGER_NAME | &quot;TriggerName&quot; |
| TRIGGER_RUN_TIMESTAMP | &quot;TriggerRunTimestamp&quot; |



