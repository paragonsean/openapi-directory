# DataFactoryManagementClient.RunQueryFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operand** | **String** | Parameter name to be used for filter. The allowed operands to query pipeline runs are PipelineName, RunStart, RunEnd and Status; to query activity runs are ActivityName, ActivityRunStart, ActivityRunEnd, ActivityType and Status, and to query trigger runs are TriggerName, TriggerRunTimestamp and Status. | 
**operator** | **String** | Operator to be used for filter. | 
**values** | **[String]** | List of filter values. | 



## Enum: OperandEnum


* `PipelineName` (value: `"PipelineName"`)

* `Status` (value: `"Status"`)

* `RunStart` (value: `"RunStart"`)

* `RunEnd` (value: `"RunEnd"`)

* `ActivityName` (value: `"ActivityName"`)

* `ActivityRunStart` (value: `"ActivityRunStart"`)

* `ActivityRunEnd` (value: `"ActivityRunEnd"`)

* `ActivityType` (value: `"ActivityType"`)

* `TriggerName` (value: `"TriggerName"`)

* `TriggerRunTimestamp` (value: `"TriggerRunTimestamp"`)

* `RunGroupId` (value: `"RunGroupId"`)

* `LatestOnly` (value: `"LatestOnly"`)





## Enum: OperatorEnum


* `Equals` (value: `"Equals"`)

* `NotEquals` (value: `"NotEquals"`)

* `In` (value: `"In"`)

* `NotIn` (value: `"NotIn"`)




