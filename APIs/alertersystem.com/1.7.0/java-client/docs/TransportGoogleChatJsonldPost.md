

# TransportGoogleChatJsonldPost

The TransportGoogleChat resource is a collection of transports that carry dispatched alerts to the external Google Chat service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**googleChatAccessKey** | **String** | The access key for the Google Chat service. |  |
|**googleChatAccessToken** | **String** | The access token for the Google Chat service. Stored in encrypted format. |  |
|**googleChatSpace** | **String** | The space name for the Google Chat service. |  |
|**googleChatThreadKey** | **String** | The optional thread key for the Google Chat service. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



