# BatchService.AutoUserSpecification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elevationLevel** | [**ElevationLevel**](ElevationLevel.md) |  | [optional] 
**scope** | **String** | The default value is pool. If the pool is running Windows a value of Task should be specified if stricter isolation between tasks is required. For example, if the task mutates the registry in a way which could impact other tasks, or if certificates have been specified on the pool which should not be accessible by normal tasks but should be accessible by StartTasks. | [optional] 



## Enum: ScopeEnum


* `task` (value: `"task"`)

* `pool` (value: `"pool"`)




