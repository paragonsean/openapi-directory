# Sakari.SendMessagesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**[ContactRequest]**](ContactRequest.md) |  | [optional] 
**conversationStrategy** | **String** |  | [optional] 
**conversations** | **[String]** | List of conversation ids to send messages to | [optional] 
**filters** | [**SendMessagesRequestFilters**](SendMessagesRequestFilters.md) |  | [optional] 
**media** | [**[SendMessagesRequestMediaInner]**](SendMessagesRequestMediaInner.md) | List of media objects to attach to message | [optional] 
**phoneNumberFilter** | [**SendMessagesRequestPhoneNumberFilter**](SendMessagesRequestPhoneNumberFilter.md) |  | [optional] 
**template** | **String** |  | [optional] 
**type** | **String** |  | [optional] 



## Enum: TypeEnum


* `SMS` (value: `"SMS"`)

* `MMS` (value: `"MMS"`)




