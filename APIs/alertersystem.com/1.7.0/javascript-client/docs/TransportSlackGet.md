# AlerterSystemApi.TransportSlackGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 
**slackChannel** | **String** | The channel (channel, private group, or IM channel to send message to, it can be an encoded ID, or a name) for the Slack service. | 
**slackToken** | **String** | The token for the Slack service. Stored in encrypted format. | 
**transportName** | **String** | The name of the transport. | 


