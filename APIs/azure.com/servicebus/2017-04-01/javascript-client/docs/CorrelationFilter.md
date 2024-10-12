# ServiceBusManagementClient.CorrelationFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentType** | **String** | Content type of the message. | [optional] 
**correlationId** | **String** | Identifier of the correlation. | [optional] 
**label** | **String** | Application specific label. | [optional] 
**messageId** | **String** | Identifier of the message. | [optional] 
**properties** | **{String: String}** | dictionary object for custom filters | [optional] 
**replyTo** | **String** | Address of the queue to reply to. | [optional] 
**replyToSessionId** | **String** | Session identifier to reply to. | [optional] 
**requiresPreprocessing** | **Boolean** | Value that indicates whether the rule action requires preprocessing. | [optional] [default to true]
**sessionId** | **String** | Session identifier. | [optional] 
**to** | **String** | Address to send to. | [optional] 


