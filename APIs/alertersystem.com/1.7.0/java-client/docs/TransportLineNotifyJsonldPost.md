

# TransportLineNotifyJsonldPost

The TransportLineNotify resource is a collection of transports that carry dispatched alerts to the external LINE Notify service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**lineNotifyAccessToken** | **String** | The access token for the LINE Notify service. Stored in encrypted format. |  |
|**lineNotifyStickerId** | **String** | The sticker ID value for the LINE Notify service. |  [optional] |
|**lineNotifyStickerPackageId** | **String** | The sticker package ID value for the LINE Notify service. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



