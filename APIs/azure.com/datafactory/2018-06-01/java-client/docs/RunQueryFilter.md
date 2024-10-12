

# RunQueryFilter

Query filter option for listing runs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operand** | [**OperandEnum**](#OperandEnum) | Parameter name to be used for filter. The allowed operands to query pipeline runs are PipelineName, RunStart, RunEnd and Status; to query activity runs are ActivityName, ActivityRunStart, ActivityRunEnd, ActivityType and Status, and to query trigger runs are TriggerName, TriggerRunTimestamp and Status. |  |
|**operator** | [**OperatorEnum**](#OperatorEnum) | Operator to be used for filter. |  |
|**values** | **List&lt;String&gt;** | List of filter values. |  |



## Enum: OperandEnum

| Name | Value |
|---- | -----|
| PIPELINE_NAME | &quot;PipelineName&quot; |
| STATUS | &quot;Status&quot; |
| RUN_START | &quot;RunStart&quot; |
| RUN_END | &quot;RunEnd&quot; |
| ACTIVITY_NAME | &quot;ActivityName&quot; |
| ACTIVITY_RUN_START | &quot;ActivityRunStart&quot; |
| ACTIVITY_RUN_END | &quot;ActivityRunEnd&quot; |
| ACTIVITY_TYPE | &quot;ActivityType&quot; |
| TRIGGER_NAME | &quot;TriggerName&quot; |
| TRIGGER_RUN_TIMESTAMP | &quot;TriggerRunTimestamp&quot; |
| RUN_GROUP_ID | &quot;RunGroupId&quot; |
| LATEST_ONLY | &quot;LatestOnly&quot; |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| EQUALS | &quot;Equals&quot; |
| NOT_EQUALS | &quot;NotEquals&quot; |
| IN | &quot;In&quot; |
| NOT_IN | &quot;NotIn&quot; |



