

# FlexV1InteractionInteractionChannelInteractionChannelInvite


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelSid** | **String** | The Channel SID for this Invite. |  [optional] |
|**interactionSid** | **String** | The Interaction SID for this Channel. |  [optional] |
|**routing** | **Object** | A JSON object representing the routing rules for the Interaction Channel. See [Outbound SMS Example](https://www.twilio.com/docs/flex/developer/conversations/interactions-api/interactions#agent-initiated-outbound-interactions) for an example Routing object. The Interactions resource uses TaskRouter for all routing functionality.   All attributes in the Routing object on your Interaction request body are added “as is” to the task. For a list of known attributes consumed by the Flex UI and/or Flex Insights, see [Known Task Attributes](https://www.twilio.com/docs/flex/developer/conversations/interactions-api#task-attributes). |  [optional] |
|**sid** | **String** | The unique string created by Twilio to identify an Interaction Channel Invite resource. |  [optional] |
|**url** | **URI** |  |  [optional] |



