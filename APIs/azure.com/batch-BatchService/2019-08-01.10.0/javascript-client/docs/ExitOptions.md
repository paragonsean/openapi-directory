# BatchService.ExitOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencyAction** | **String** | Possible values are &#39;satisfy&#39; (allowing dependent tasks to progress) and &#39;block&#39; (dependent tasks continue to wait). Batch does not yet support cancellation of dependent tasks. | [optional] 
**jobAction** | **String** | The default is none for exit code 0 and terminate for all other exit conditions. If the Job&#39;s onTaskFailed property is noaction, then specifying this property returns an error and the add Task request fails with an invalid property value error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). | [optional] 



## Enum: DependencyActionEnum


* `satisfy` (value: `"satisfy"`)

* `block` (value: `"block"`)





## Enum: JobActionEnum


* `none` (value: `"none"`)

* `disable` (value: `"disable"`)

* `terminate` (value: `"terminate"`)




