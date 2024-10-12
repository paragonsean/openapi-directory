

# UserObject

Represents chat user

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**banExpires** | **OffsetDateTime** | Expiration date of the ban |  [optional] |
|**banned** | **Boolean** | Whether a user is banned or not |  |
|**createdAt** | **OffsetDateTime** | Date/time of creation |  [optional] [readonly] |
|**deactivatedAt** | **OffsetDateTime** | Date of deactivation |  [optional] [readonly] |
|**deletedAt** | **OffsetDateTime** | Date/time of deletion |  [optional] [readonly] |
|**id** | **String** | Unique user identifier |  |
|**invisible** | **Boolean** |  |  [optional] |
|**language** | **String** | Preferred language of a user |  [optional] |
|**lastActive** | **OffsetDateTime** | Date of last activity |  [optional] [readonly] |
|**online** | **Boolean** | Whether a user online or not |  [readonly] |
|**pushNotifications** | [**PushNotificationSettings**](PushNotificationSettings.md) |  |  [optional] |
|**revokeTokensIssuedBefore** | **OffsetDateTime** | Revocation date for tokens |  [optional] |
|**role** | **String** | Determines the set of user permissions |  |
|**teams** | **List&lt;String&gt;** | List of teams user is a part of |  [optional] |
|**updatedAt** | **OffsetDateTime** | Date/time of the last update |  [optional] [readonly] |



