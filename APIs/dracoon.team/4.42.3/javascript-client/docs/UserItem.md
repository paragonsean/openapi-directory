# DracoonApi.UserItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatarUuid** | **String** | &amp;#128640; Since v4.11.0  Avatar UUID | 
**createdAt** | **Date** | Creation date | [optional] 
**email** | **String** | Email  | [optional] 
**expireAt** | **Date** | Expiration date | [optional] 
**firstName** | **String** | User first name | 
**gender** | **String** | &amp;#128679; Deprecated since v4.12.0  Gender | [optional] [default to &#39;n&#39;]
**hasManageableRooms** | **Boolean** | &amp;#128679; Deprecated since v4.27.0  User has manageable rooms | [optional] 
**homeRoomId** | **Number** | Homeroom ID | [optional] 
**id** | **Number** | Unique identifier for the user | 
**isEncryptionEnabled** | **Boolean** | User has generated private key.  Possible if client-side encryption is active for this customer | [optional] 
**isLocked** | **Boolean** | User is locked:  * &#x60;false&#x60; - unlocked  * &#x60;true&#x60; - locked    User is locked and can not login anymore. | [default to false]
**lastLoginSuccessAt** | **Date** | Last successful logon date | [optional] 
**lastName** | **String** | User last name | 
**lockStatus** | **Number** | &amp;#128679; Deprecated since v4.7.0  User lock status:  * &#x60;0&#x60; - locked  * &#x60;1&#x60; - Web access allowed  * &#x60;2&#x60; - Web and mobile access allowed    Please use &#x60;isLocked&#x60; instead. | 
**login** | **String** | &amp;#128679; Deprecated since v4.13.0  User login name | 
**phone** | **String** | Phone number | [optional] 
**title** | **String** | &amp;#128679; Deprecated since v4.18.0  Job title | [optional] 
**userAttributes** | [**UserAttributes**](UserAttributes.md) |  | [optional] 
**userName** | **String** | &amp;#128640; Since v4.13.0  Username | 
**userRoles** | [**RoleList**](RoleList.md) |  | [optional] 


