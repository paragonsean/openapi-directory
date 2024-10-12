# BatchService.PoolResizeParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodeDeallocationOption** | **String** | The default value is requeue. | [optional] 
**resizeTimeout** | **String** | The default value is 15 minutes. The minimum value is 5 minutes. If you specify a value less than 5 minutes, the Batch service returns an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). | [optional] 
**targetDedicated** | **Number** |  | 



## Enum: NodeDeallocationOptionEnum


* `requeue` (value: `"requeue"`)

* `terminate` (value: `"terminate"`)

* `taskcompletion` (value: `"taskcompletion"`)

* `retaineddata` (value: `"retaineddata"`)




