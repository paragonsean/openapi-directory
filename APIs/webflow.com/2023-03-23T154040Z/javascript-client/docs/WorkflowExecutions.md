# LucidtechApi.WorkflowExecutions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executions** | [**[WorkflowExecutionsExecutionsInner]**](WorkflowExecutionsExecutionsInner.md) |  | 
**nextToken** | **String** |  | 
**order** | **String** |  | [optional] 
**sortBy** | **String** |  | [optional] 
**status** | **[String]** |  | [optional] 
**workflowId** | **String** |  | 



## Enum: OrderEnum


* `ascending` (value: `"ascending"`)

* `descending` (value: `"descending"`)





## Enum: SortByEnum


* `startTime` (value: `"startTime"`)

* `endTime` (value: `"endTime"`)





## Enum: [StatusEnum]


* `running` (value: `"running"`)

* `succeeded` (value: `"succeeded"`)

* `failed` (value: `"failed"`)

* `rejected` (value: `"rejected"`)

* `retry` (value: `"retry"`)

* `error` (value: `"error"`)




