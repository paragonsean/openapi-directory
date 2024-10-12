

# TransportGotifyPost

The TransportGotify resource is a collection of transports that carry dispatched alerts to the external Gotify service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**gotifyApiUrl** | **URI** | The API URL name for the Gotify service (https://example.com) - (do not include the path /message/createMessage). |  |
|**gotifyAppToken** | **String** | The app token for the Gotify service. Stored in encrypted format. |  |
|**gotifyPriority** | **String** | The priority for the Gotify service. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



