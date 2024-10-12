# BatchService.AutoUserSpecification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elevationLevel** | [**ElevationLevel**](ElevationLevel.md) |  | [optional] 
**scope** | **String** | pool - specifies that the task runs as the common auto user account which is created on every node in a pool. task - specifies that the service should create a new user for the task. The default value is task. | [optional] 



## Enum: ScopeEnum


* `task` (value: `"task"`)

* `pool` (value: `"pool"`)




