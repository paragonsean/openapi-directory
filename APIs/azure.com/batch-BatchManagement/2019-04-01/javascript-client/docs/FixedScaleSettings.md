# BatchManagement.FixedScaleSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodeDeallocationOption** | [**ComputeNodeDeallocationOption**](ComputeNodeDeallocationOption.md) |  | [optional] 
**resizeTimeout** | **String** | The default value is 15 minutes. Timeout values use ISO 8601 format. For example, use PT10M for 10 minutes. The minimum value is 5 minutes. If you specify a value less than 5 minutes, the Batch service rejects the request with an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). | [optional] 
**targetDedicatedNodes** | **Number** | At least one of targetDedicatedNodes, targetLowPriority nodes must be set. | [optional] 
**targetLowPriorityNodes** | **Number** | At least one of targetDedicatedNodes, targetLowPriority nodes must be set. | [optional] 


