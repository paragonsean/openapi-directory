# ServiceFabricClientApis.RepairTaskCancelDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestAbort** | **Boolean** | _True_ if the repair should be stopped as soon as possible even if it has already started executing. _False_ if the repair should be cancelled only if execution has not yet started.&lt;/para&gt; | [optional] 
**taskId** | **String** | The ID of the repair task. | 
**version** | **String** | The current version number of the repair task. If non-zero, then the request will only succeed if this value matches the actual current version of the repair task. If zero, then no version check is performed.&lt;/para&gt; | [optional] 


