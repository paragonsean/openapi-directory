

# Channel

A user who joins a conversation as a member can have one channel per membership type. Channels can be `app`, `phone`, `sip`, `websocket`, or `vbc`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**from** | [**ChannelFrom**](ChannelFrom.md) |  |  [optional] |
|**legId** | **String** | The id of the leg. rtc_id and call_id are leg id |  [optional] |
|**legIds** | [**List&lt;ChannelLegIdsInner&gt;**](ChannelLegIdsInner.md) | Leg ids associated with this Channel. The first item in the array represents the main active Leg. The second item, if exists, represents a screen-share Leg. |  [optional] |
|**to** | [**ChannelTo**](ChannelTo.md) |  |  [optional] |
|**type** | **ChannelType** |  |  [optional] |



