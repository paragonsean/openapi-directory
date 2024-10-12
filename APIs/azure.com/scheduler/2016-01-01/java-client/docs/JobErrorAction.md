

# JobErrorAction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**queueMessage** | [**StorageQueueMessage**](StorageQueueMessage.md) |  |  [optional] |
|**request** | [**HttpRequest**](HttpRequest.md) |  |  [optional] |
|**retryPolicy** | [**RetryPolicy**](RetryPolicy.md) |  |  [optional] |
|**serviceBusQueueMessage** | [**ServiceBusQueueMessage**](ServiceBusQueueMessage.md) |  |  [optional] |
|**serviceBusTopicMessage** | [**ServiceBusTopicMessage**](ServiceBusTopicMessage.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Gets or sets the job error action type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |
| STORAGE_QUEUE | &quot;StorageQueue&quot; |
| SERVICE_BUS_QUEUE | &quot;ServiceBusQueue&quot; |
| SERVICE_BUS_TOPIC | &quot;ServiceBusTopic&quot; |



