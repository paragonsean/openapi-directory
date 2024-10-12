

# TransportPushbulletJsonldPost

The TransportPushbullet resource is a collection of transports that carry dispatched alerts to the external Pushbullet service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**pushbulletAccessToken** | **String** | The access token for the Pushbullet service. Stored in encrypted format. |  |
|**pushbulletEmail** | **String** | The recipient email for the Pushbullet service. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |



