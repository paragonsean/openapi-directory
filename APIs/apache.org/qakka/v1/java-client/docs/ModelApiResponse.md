

# ModelApiResponse

Response returned by most Queue API calls.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | Count of Queues or QueueMessages returned by the call. |  [optional] |
|**message** | **String** | Informative message intended for client. |  [optional] |
|**queueMessages** | [**List&lt;QueueMessage&gt;**](QueueMessage.md) | Queues Messages returned by the call, or empty if not applicable. |  [optional] |
|**queues** | [**List&lt;Queue&gt;**](Queue.md) | Queues returned but the call, or empty if not applicable. |  [optional] |



