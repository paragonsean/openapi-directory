# SchedulerManagementClient.JobErrorAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queueMessage** | [**StorageQueueMessage**](StorageQueueMessage.md) |  | [optional] 
**request** | [**HttpRequest**](HttpRequest.md) |  | [optional] 
**retryPolicy** | [**RetryPolicy**](RetryPolicy.md) |  | [optional] 
**serviceBusQueueMessage** | [**ServiceBusQueueMessage**](ServiceBusQueueMessage.md) |  | [optional] 
**serviceBusTopicMessage** | [**ServiceBusTopicMessage**](ServiceBusTopicMessage.md) |  | [optional] 
**type** | **String** | Gets or sets the job error action type. | [optional] 



## Enum: TypeEnum


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)

* `StorageQueue` (value: `"StorageQueue"`)

* `ServiceBusQueue` (value: `"ServiceBusQueue"`)

* `ServiceBusTopic` (value: `"ServiceBusTopic"`)




