# AmazonInteractiveVideoServiceChat.UpdateRoomRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **String** | Identifier of the room to be updated. Currently this must be an ARN. | 
**loggingConfigurationIdentifiers** | **[String]** | Array of logging-configuration identifiers attached to the room. | [optional] 
**maximumMessageLength** | **Number** | The maximum number of characters in a single message. Messages are expected to be UTF-8 encoded and this limit applies specifically to rune/code-point count, not number of bytes. Default: 500. | [optional] 
**maximumMessageRatePerSecond** | **Number** | Maximum number of messages per second that can be sent to the room (by all clients). Default: 10. | [optional] 
**messageReviewHandler** | [**CreateRoomRequestMessageReviewHandler**](CreateRoomRequestMessageReviewHandler.md) |  | [optional] 
**name** | **String** | Room name. The value does not need to be unique. | [optional] 


