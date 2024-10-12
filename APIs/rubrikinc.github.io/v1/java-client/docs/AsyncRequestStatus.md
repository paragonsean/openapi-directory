

# AsyncRequestStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | The end time of the request. |  [optional] |
|**error** | [**RequestErrorInfo**](RequestErrorInfo.md) |  |  [optional] |
|**id** | **String** | The ID of the request object used to poll the status. |  |
|**links** | [**List&lt;Link&gt;**](Link.md) | References to any related objects. |  |
|**nodeId** | **String** | The ID of the node where the job ran. |  [optional] |
|**progress** | **Double** | The current percentage progress of the asynchronous request. |  [optional] |
|**startTime** | **OffsetDateTime** | The start time of the request. |  [optional] |
|**status** | **String** | Status of the ID. |  |



