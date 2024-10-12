

# ProviderShareSubscriptionProperties

Provider share subscription properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumerEmail** | **String** | Email of the consumer who created the share subscription |  [optional] [readonly] |
|**consumerName** | **String** | Name of the consumer who created the share subscription |  [optional] [readonly] |
|**consumerTenantName** | **String** | Tenant name of the consumer who created the share subscription |  [optional] [readonly] |
|**createdAt** | **OffsetDateTime** | created at |  [optional] [readonly] |
|**providerEmail** | **String** | Email of the provider who created the share |  [optional] [readonly] |
|**providerName** | **String** | Name of the provider who created the share |  [optional] [readonly] |
|**shareSubscriptionObjectId** | **String** | share Subscription Object Id |  [optional] [readonly] |
|**shareSubscriptionStatus** | [**ShareSubscriptionStatusEnum**](#ShareSubscriptionStatusEnum) | Gets the status of share subscription |  [optional] [readonly] |
|**sharedAt** | **OffsetDateTime** | Shared at |  [optional] [readonly] |



## Enum: ShareSubscriptionStatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| REVOKED | &quot;Revoked&quot; |
| SOURCE_DELETED | &quot;SourceDeleted&quot; |
| REVOKING | &quot;Revoking&quot; |



