

# Connection


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authEventId** | **UUID** | Identifier shared across connections authorised at the same time |  [optional] |
|**createdDateUtc** | **OffsetDateTime** | The date when the user connected this tenant to your app |  [optional] |
|**id** | **UUID** | Xero identifier |  [optional] |
|**tenantId** | **UUID** | Xero identifier of organisation |  [optional] |
|**tenantName** | **String** | Xero tenant name |  [optional] |
|**tenantType** | **String** | Xero tenant type (i.e. ORGANISATION, PRACTICE) |  [optional] |
|**updatedDateUtc** | **OffsetDateTime** | The date when the user most recently connected this tenant to your app. May differ to the created date if the user has disconnected and subsequently reconnected this tenant to your app. |  [optional] |



