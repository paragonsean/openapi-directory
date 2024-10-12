# SchedulerManagementClient.JobAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorAction** | [**JobErrorAction**](JobErrorAction.md) |  | [optional] 
**queueMessage** | [**StorageQueueMessage**](StorageQueueMessage.md) |  | [optional] 
**request** | [**HttpRequest**](HttpRequest.md) |  | [optional] 
**retryPolicy** | [**RetryPolicy**](RetryPolicy.md) |  | [optional] 
**serviceBusQueueMessage** | [**ServiceBusQueueMessage**](ServiceBusQueueMessage.md) |  | [optional] 
**serviceBusTopicMessage** | [**ServiceBusTopicMessage**](ServiceBusTopicMessage.md) |  | [optional] 
**type** | **String** | Gets or sets the job action type. | [optional] 



## Enum: TypeEnum


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)

* `StorageQueue` (value: `"StorageQueue"`)

* `ServiceBusQueue` (value: `"ServiceBusQueue"`)

* `ServiceBusTopic` (value: `"ServiceBusTopic"`)




