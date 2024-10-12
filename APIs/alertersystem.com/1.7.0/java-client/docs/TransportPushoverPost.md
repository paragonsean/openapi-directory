

# TransportPushoverPost

The TransportPushover resource is a collection of transports that carry dispatched alerts to the external Pushover service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**pushoverAppToken** | **String** | The app token for the Pushover service. Stored in encrypted format. |  |
|**pushoverUserKey** | **String** | The user key for the Pushover service. |  |
|**transportName** | **String** | The name of the transport. |  |



