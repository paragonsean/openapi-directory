# BatchManagement.ResizeOperationStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[ResizeError]**](ResizeError.md) | This property is set only if an error occurred during the last pool resize, and only when the pool allocationState is Steady. | [optional] 
**nodeDeallocationOption** | [**ComputeNodeDeallocationOption**](ComputeNodeDeallocationOption.md) |  | [optional] 
**resizeTimeout** | **String** | The default value is 15 minutes. The minimum value is 5 minutes. If you specify a value less than 5 minutes, the Batch service returns an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). | [optional] 
**startTime** | **Date** |  | [optional] 
**targetDedicatedNodes** | **Number** |  | [optional] 
**targetLowPriorityNodes** | **Number** |  | [optional] 


