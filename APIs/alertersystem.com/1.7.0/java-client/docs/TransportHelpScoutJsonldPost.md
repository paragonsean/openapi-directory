

# TransportHelpScoutJsonldPost

The TransportHelpScout resource is a collection of transports that carry dispatched alerts to the external HelpScout service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**helpScoutCustomerEmail** | **String** | The requester customer email address for the HelpScout service. |  |
|**helpScoutMailboxId** | **Integer** | The mailbox ID for the HelpScout service. |  [optional] |
|**helpScoutOauthToken** | **String** | The OAuth token for the HelpScout service. Stored in encrypted format. |  |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



