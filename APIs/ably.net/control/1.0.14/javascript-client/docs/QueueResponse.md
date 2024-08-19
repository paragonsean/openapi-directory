# ControlApiV1.QueueResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amqp** | [**QueueResponseAmqp**](QueueResponseAmqp.md) |  | [optional] 
**appId** | **String** | The Ably application ID. | [optional] 
**deadletter** | **Boolean** | A boolean that indicates whether this is a dead letter queue or not. | [optional] 
**deadletterId** | **String** |  | [optional] 
**id** | **String** | The ID of the Ably queue | [optional] 
**maxLength** | **Number** | Message limit in number of messages. | [optional] 
**messages** | [**QueueResponseMessages**](QueueResponseMessages.md) |  | [optional] 
**name** | **String** | The friendly name of the queue. | [optional] 
**region** | **String** | The data center region for the queue. | [optional] 
**state** | **String** | The current state of the queue. | [optional] 
**stats** | [**QueueResponseStats**](QueueResponseStats.md) |  | [optional] 
**stomp** | [**QueueResponseStomp**](QueueResponseStomp.md) |  | [optional] 
**ttl** | **Number** | TTL in minutes. | [optional] 


