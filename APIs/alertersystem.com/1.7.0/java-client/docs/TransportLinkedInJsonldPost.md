

# TransportLinkedInJsonldPost

The TransportLinkedIn resource is a collection of transports that carry dispatched alerts to the external LinkedIn service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**linkedInToken** | **String** | The access token for the LinkedIn service. Stored in encrypted format. |  |
|**linkedInUserId** | **String** | The user ID for the LinkedIn service. |  |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



