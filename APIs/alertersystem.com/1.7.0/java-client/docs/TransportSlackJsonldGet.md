

# TransportSlackJsonldGet

The TransportSlack resource is a collection of transports that carry dispatched alerts to the external Slack service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atContext** | [**AlertLogJsonldGetContext**](AlertLogJsonldGetContext.md) |  |  [optional] |
|**atId** | **String** |  |  [optional] [readonly] |
|**atType** | **String** |  |  [optional] [readonly] |
|**createdAt** | **OffsetDateTime** | When the resource instance was created. This date-time is in the UTC timezone. |  [optional] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] [readonly] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**resourceOwner** | **String** | The name of the person who owns this resource. |  [optional] |
|**slackChannel** | **String** | The channel (channel, private group, or IM channel to send message to, it can be an encoded ID, or a name) for the Slack service. |  |
|**slackToken** | **String** | The token for the Slack service. Stored in encrypted format. |  |
|**transportName** | **String** | The name of the transport. |  |



