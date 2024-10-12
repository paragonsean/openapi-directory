

# UserData

User information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authData** | [**UserAuthData**](UserAuthData.md) |  |  |
|**authMethods** | [**List&lt;UserAuthMethod&gt;**](UserAuthMethod.md) | &amp;#128679; Deprecated since v4.13.0  Authentication methods:  * &#x60;sql&#x60;  * &#x60;active_directory&#x60;  * &#x60;radius&#x60;  * &#x60;openid&#x60;  use &#x60;authData&#x60; instead |  [optional] |
|**avatarUuid** | **String** | &amp;#128640; Since v4.11.0  Avatar UUID |  |
|**email** | **String** | Email  |  [optional] |
|**expireAt** | **OffsetDateTime** | Expiration date |  [optional] |
|**firstName** | **String** | User first name |  |
|**gender** | **String** | &amp;#128679; Deprecated since v4.12.0  Gender |  [optional] |
|**hasManageableRooms** | **Boolean** | User has manageable rooms |  [optional] |
|**homeRoomId** | **Long** | Homeroom ID |  [optional] |
|**id** | **Long** | Unique identifier for the user |  |
|**isEncryptionEnabled** | **Boolean** | User has generated private key.  Possible if client-side encryption is active for this customer |  [optional] |
|**isLocked** | **Boolean** | User is locked:  * &#x60;false&#x60; - unlocked  * &#x60;true&#x60; - locked    User is locked and can not login anymore. |  |
|**isMfaEnabled** | **Boolean** | Determines whether multi-factor authentication is enabled |  [optional] |
|**isMfaEnforced** | **Boolean** | Determines whether multi-factor authentication is enforced |  [optional] |
|**lastLoginSuccessAt** | **OffsetDateTime** | Last successful logon date |  [optional] |
|**lastName** | **String** | User last name |  |
|**lockStatus** | **Integer** | &amp;#128679; Deprecated since v4.7.0  User lock status:  * &#x60;0&#x60; - locked  * &#x60;1&#x60; - Web access allowed  * &#x60;2&#x60; - Web and mobile access allowed    Please use &#x60;isLocked&#x60; instead. |  |
|**login** | **String** | &amp;#128679; Deprecated since v4.13.0  User login name |  [optional] |
|**phone** | **String** | Phone number |  [optional] |
|**publicKeyContainer** | [**PublicKeyContainer**](PublicKeyContainer.md) |  |  [optional] |
|**title** | **String** | &amp;#128679; Deprecated since v4.18.0  Job title |  [optional] |
|**userAttributes** | [**UserAttributes**](UserAttributes.md) |  |  [optional] |
|**userName** | **String** | &amp;#128640; Since v4.13.0  Username |  |
|**userRoles** | [**RoleList**](RoleList.md) |  |  [optional] |



