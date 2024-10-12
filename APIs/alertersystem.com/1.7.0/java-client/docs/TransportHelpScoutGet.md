

# TransportHelpScoutGet

The TransportHelpScout resource is a collection of transports that carry dispatched alerts to the external HelpScout service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | When the resource instance was created. This date-time is in the UTC timezone. |  [optional] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**helpScoutCustomerEmail** | **String** | The requester customer email address for the HelpScout service. |  |
|**helpScoutMailboxId** | **Integer** | The mailbox ID for the HelpScout service. |  [optional] |
|**helpScoutOauthToken** | **String** | The OAuth token for the HelpScout service. Stored in encrypted format. |  |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] [readonly] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**resourceOwner** | **String** | The name of the person who owns this resource. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |



