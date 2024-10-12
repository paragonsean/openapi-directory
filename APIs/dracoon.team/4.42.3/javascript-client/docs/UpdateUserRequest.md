# DracoonApi.UpdateUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authData** | [**UserAuthDataUpdateRequest**](UserAuthDataUpdateRequest.md) |  | [optional] 
**authMethods** | [**[UserAuthMethod]**](UserAuthMethod.md) | &amp;#128679; Deprecated since v4.13.0  Authentication methods:  * &#x60;sql&#x60;  * &#x60;active_directory&#x60;  * &#x60;radius&#x60;  * &#x60;openid&#x60;  use &#x60;authData&#x60; instead | [optional] 
**email** | **String** | Email  | [optional] 
**expiration** | [**ObjectExpiration**](ObjectExpiration.md) |  | [optional] 
**firstName** | **String** | User first name | [optional] 
**gender** | **String** | &amp;#128679; Deprecated since v4.12.0  Gender  Do NOT use &#x60;gender&#x60;! It will be ignored. | [optional] [default to &#39;n&#39;]
**isLocked** | **Boolean** | User is locked:  * &#x60;false&#x60; - unlocked  * &#x60;true&#x60; - locked    User is locked and can not login anymore. | [optional] [default to false]
**lastName** | **String** | User last name | [optional] 
**lockStatus** | **Number** | &amp;#128679; Deprecated since v4.7.0  User lock status:  * &#x60;0&#x60; - locked  * &#x60;1&#x60; - Web access allowed  * &#x60;2&#x60; - Web and mobile access allowed    Please use &#x60;isLocked&#x60; instead. | [optional] 
**mfaConfig** | [**MfaConfig**](MfaConfig.md) |  | [optional] 
**phone** | **String** | Phone number | [optional] 
**receiverLanguage** | **String** | IETF language tag | [optional] 
**title** | **String** | &amp;#128679; Deprecated since v4.18.0  Job title | [optional] 
**userName** | **String** | &amp;#128640; Since v4.13.0  Username | [optional] 


