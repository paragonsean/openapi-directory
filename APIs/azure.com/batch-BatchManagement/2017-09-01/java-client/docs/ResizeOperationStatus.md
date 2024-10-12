

# ResizeOperationStatus

Describes either the current operation (if the pool AllocationState is Resizing) or the previously completed operation (if the AllocationState is Steady).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;ResizeError&gt;**](ResizeError.md) | This property is set only if an error occurred during the last pool resize, and only when the pool allocationState is Steady. |  [optional] |
|**nodeDeallocationOption** | **ComputeNodeDeallocationOption** |  |  [optional] |
|**resizeTimeout** | **String** | The default value is 15 minutes. The minimum value is 5 minutes. If you specify a value less than 5 minutes, the Batch service returns an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). |  [optional] |
|**startTime** | **OffsetDateTime** |  |  [optional] |
|**targetDedicatedNodes** | **Integer** |  |  [optional] |
|**targetLowPriorityNodes** | **Integer** |  |  [optional] |



