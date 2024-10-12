

# TransportMastodonPatch

The TransportMastodon resource is a collection of transports that carry dispatched alerts to the external Mastodon service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**mastodonAccessToken** | **String** | The access token for the Mastodon service. Stored in encrypted format. |  |
|**mastodonHost** | **String** | The host name for the Mastodon service (omit the \&quot;https://\&quot; part). |  |
|**transportName** | **String** | The name of the transport. |  |



