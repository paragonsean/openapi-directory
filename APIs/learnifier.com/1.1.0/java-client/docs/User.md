

# User


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationPossible** | **Boolean** | True if the user can authorize herself/himself |  [optional] |
|**displayName** | **String** | Full name of the user |  [optional] |
|**externalId** | **String** | The external id (foreign key). Must not exceed 255 characters. |  [optional] |
|**firstLogin** | **OffsetDateTime** | The timestamp when the first login was made. This value can be *null*. |  [optional] |
|**firstName** | **String** | The first name of the user (or given name) |  [optional] |
|**hardLock** | **Boolean** | True if the user is locked and the lock has been set by an administrator |  [optional] |
|**homeOrg** | **Long** | The primary organization for the user. Must match the id of an Organization Unit. |  [optional] |
|**id** | **UUID** | The id of the user this participation belongs to |  [optional] |
|**lastLogin** | **OffsetDateTime** | The timestamp when the last login was made. This value can be *null*. |  [optional] |
|**lastName** | **String** | The last name of the user (or surname) |  [optional] |
|**locked** | **Boolean** | Lock status. A locked user will not be able to access the platform. |  [optional] |
|**prefs** | [**UserPreferences**](UserPreferences.md) |  |  [optional] |
|**primaryEmail** | **String** | The primary email for this user. If the user has no email this value is *null*. |  [optional] |



