# CatalogInventory.Task

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archivedAt** | **Date** |  | [optional] [readonly] 
**childTaskId** | **String** |  | [optional] [readonly] 
**completedAt** | **Date** |  | [optional] 
**controllerMessageId** | **String** |  | [optional] [readonly] 
**createdAt** | **Date** |  | [optional] [readonly] 
**id** | **String** | UUID of task | [optional] [readonly] 
**input** | **Object** |  | [optional] [readonly] 
**message** | **String** |  | [optional] 
**name** | **String** |  | [optional] 
**output** | **Object** |  | [optional] 
**owner** | **String** |  | [optional] [readonly] 
**sourceId** | **String** | ID of the resource | [optional] [readonly] 
**state** | **String** |  | [optional] 
**status** | **String** |  | [optional] 
**targetSourceRef** | **String** |  | [optional] 
**targetType** | **String** |  | [optional] 
**type** | **String** |  | [optional] 
**updatedAt** | **Date** |  | [optional] [readonly] 



## Enum: StateEnum


* `pending` (value: `"pending"`)

* `queued` (value: `"queued"`)

* `running` (value: `"running"`)

* `timedout` (value: `"timedout"`)

* `completed` (value: `"completed"`)





## Enum: StatusEnum


* `ok` (value: `"ok"`)

* `warn` (value: `"warn"`)

* `unchanged` (value: `"unchanged"`)

* `error` (value: `"error"`)




