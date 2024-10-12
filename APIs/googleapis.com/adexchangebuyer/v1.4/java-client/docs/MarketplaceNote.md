

# MarketplaceNote

A proposal is associated with a bunch of notes which may optionally be associated with a deal and/or revision number.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creatorRole** | **String** | The role of the person (buyer/seller) creating the note. (readonly) |  [optional] |
|**dealId** | **String** | Notes can optionally be associated with a deal. (readonly, except on create) |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;adexchangebuyer#marketplaceNote\&quot;. |  [optional] |
|**note** | **String** | The actual note to attach. (readonly, except on create) |  [optional] |
|**noteId** | **String** | The unique id for the note. (readonly) |  [optional] |
|**proposalId** | **String** | The proposalId that a note is attached to. (readonly) |  [optional] |
|**proposalRevisionNumber** | **String** | If the note is associated with a proposal revision number, then store that here. (readonly, except on create) |  [optional] |
|**timestampMs** | **String** | The timestamp (ms since epoch) that this note was created. (readonly) |  [optional] |



