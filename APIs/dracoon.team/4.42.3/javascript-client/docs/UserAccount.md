# DracoonApi.UserAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authData** | [**UserAuthData**](UserAuthData.md) |  | 
**authMethods** | [**[UserAuthMethod]**](UserAuthMethod.md) | &amp;#128679; Deprecated since v4.13.0  Authentication methods:  * &#x60;sql&#x60;  * &#x60;active_directory&#x60;  * &#x60;radius&#x60;  * &#x60;openid&#x60;  use &#x60;authData&#x60; instead | [optional] 
**email** | **String** | Email  | [optional] 
**expireAt** | **Date** | Expiration date | [optional] 
**firstName** | **String** | User first name | 
**gender** | **String** | &amp;#128679; Deprecated since v4.12.0  Gender | [optional] [default to &#39;n&#39;]
**hasManageableRooms** | **Boolean** | User has manageable rooms | 
**homeRoomId** | **Number** | Homeroom ID | [optional] 
**id** | **Number** | Unique identifier for the user | 
**isEncryptionEnabled** | **Boolean** | User has generated private key.  Possible if client-side encryption is active for this customer | [optional] 
**isLocked** | **Boolean** | User is locked:  * &#x60;false&#x60; - unlocked  * &#x60;true&#x60; - locked    User is locked and can not login anymore. | [default to false]
**language** | **String** | &amp;#128640; Since v4.20.0  IETF language tag | 
**lastLoginFailAt** | **Date** | Last failed logon date | [optional] 
**lastLoginFailIp** | **String** | &amp;#128679; Deprecated since v4.6.0  Last failed logon IP address | [optional] 
**lastLoginSuccessAt** | **Date** | Last successful logon date | [optional] 
**lastLoginSuccessIp** | **String** | &amp;#128679; Deprecated since v4.6.0  Last successful logon IP address | [optional] 
**lastName** | **String** | User last name | 
**lockStatus** | **Number** | &amp;#128679; Deprecated since v4.7.0  User lock status:  * &#x60;0&#x60; - locked  * &#x60;1&#x60; - Web access allowed  * &#x60;2&#x60; - Web and mobile access allowed    Please use &#x60;isLocked&#x60; instead. | 
**login** | **String** | &amp;#128679; Deprecated since v4.13.0  User login name | [optional] 
**mustSetEmail** | **Boolean** | &amp;#128640; Since v4.13.0  If &#x60;true&#x60;, the user must set the &#x60;email&#x60; at the first login. | [optional] [default to false]
**needsToAcceptEULA** | **Boolean** | User has accepted EULA.  Present, if EULA is system global active.  cf. &#x60;GET system/config/settings/general&#x60; - &#x60;eulaEnabled&#x60; | [optional] 
**needsToChangePassword** | **Boolean** | &amp;#128679; Deprecated since v4.13.0  Determines whether user has to change his / her password | 
**needsToChangeUserName** | **Boolean** | &amp;#128679; Deprecated since v4.13.0  If &#x60;true&#x60;, the user must change the &#x60;userName&#x60; at the first login. | [optional] [default to false]
**phone** | **String** | Phone number | [optional] 
**title** | **String** | &amp;#128679; Deprecated since v4.18.0  Job title | [optional] 
**userAttributes** | [**UserAttributes**](UserAttributes.md) |  | [optional] 
**userGroups** | [**[UserGroup]**](UserGroup.md) | All groups the user is member of | [optional] 
**userName** | **String** | &amp;#128640; Since v4.13.0  Username | 
**userRoles** | [**RoleList**](RoleList.md) |  | 


