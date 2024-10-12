

# SensitiveAdminAction

Alert that is triggered when Sensitive Admin Action occur in customer account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actorEmail** | **String** | Email of person who performed the action |  [optional] |
|**eventTime** | **String** | The time at which event occurred |  [optional] |
|**primaryAdminChangedEvent** | [**PrimaryAdminChangedEvent**](PrimaryAdminChangedEvent.md) |  |  [optional] |
|**ssoProfileCreatedEvent** | [**SSOProfileCreatedEvent**](SSOProfileCreatedEvent.md) |  |  [optional] |
|**ssoProfileDeletedEvent** | [**SSOProfileDeletedEvent**](SSOProfileDeletedEvent.md) |  |  [optional] |
|**ssoProfileUpdatedEvent** | [**SSOProfileUpdatedEvent**](SSOProfileUpdatedEvent.md) |  |  [optional] |
|**superAdminPasswordResetEvent** | [**SuperAdminPasswordResetEvent**](SuperAdminPasswordResetEvent.md) |  |  [optional] |



