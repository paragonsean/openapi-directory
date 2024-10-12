

# UserObjectRequest

Represents chat user

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**banExpires** | **OffsetDateTime** | Expiration date of the ban |  [optional] |
|**banned** | **Boolean** | Whether a user is banned or not |  [optional] |
|**id** | **String** | Unique user identifier |  |
|**invisible** | **Boolean** |  |  [optional] |
|**language** | **String** | Preferred language of a user |  [optional] |
|**pushNotifications** | [**PushNotificationSettingsRequest**](PushNotificationSettingsRequest.md) |  |  [optional] |
|**revokeTokensIssuedBefore** | **OffsetDateTime** | Revocation date for tokens |  [optional] |
|**role** | **String** | Determines the set of user permissions |  [optional] |
|**teams** | **List&lt;String&gt;** | List of teams user is a part of |  [optional] |



