# DataFactoryManagementClient.RunQueryOrderBy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **String** | Sorting order of the parameter. | 
**orderBy** | **String** | Parameter name to be used for order by. The allowed parameters to order by for pipeline runs are PipelineName, RunStart, RunEnd and Status; for activity runs are ActivityName, ActivityRunStart, ActivityRunEnd and Status; for trigger runs are TriggerName, TriggerRunTimestamp and Status. | 



## Enum: OrderEnum


* `ASC` (value: `"ASC"`)

* `DESC` (value: `"DESC"`)





## Enum: OrderByEnum


* `RunStart` (value: `"RunStart"`)

* `RunEnd` (value: `"RunEnd"`)

* `PipelineName` (value: `"PipelineName"`)

* `Status` (value: `"Status"`)

* `ActivityName` (value: `"ActivityName"`)

* `ActivityRunStart` (value: `"ActivityRunStart"`)

* `ActivityRunEnd` (value: `"ActivityRunEnd"`)

* `TriggerName` (value: `"TriggerName"`)

* `TriggerRunTimestamp` (value: `"TriggerRunTimestamp"`)




