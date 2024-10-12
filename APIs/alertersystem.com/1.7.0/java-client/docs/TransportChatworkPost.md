

# TransportChatworkPost

The TransportChatwork resource is a collection of transports that carry dispatched alerts to the external Chatwork service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chatworkApiToken** | **String** | The API token for the Chatwork service. Stored in encrypted format. |  |
|**chatworkRoomId** | **String** | The room ID for the Chatwork service. |  |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



