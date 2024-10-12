# DracoonApi.CreateUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authData** | [**UserAuthData**](UserAuthData.md) |  | [optional] 
**authMethods** | [**[UserAuthMethod]**](UserAuthMethod.md) | &amp;#128679; Deprecated since v4.13.0  Authentication methods:  * &#x60;sql&#x60;  * &#x60;active_directory&#x60;  * &#x60;radius&#x60;  * &#x60;openid&#x60;  use &#x60;authData&#x60; instead | [optional] 
**email** | **String** | Email  | [optional] 
**expiration** | [**ObjectExpiration**](ObjectExpiration.md) |  | [optional] 
**firstName** | **String** | User first name | 
**gender** | **String** | &amp;#128679; Deprecated since v4.12.0  Gender  Do NOT use &#x60;gender&#x60;! It will be ignored. | [optional] [default to &#39;n&#39;]
**isNonmemberViewer** | **Boolean** | &amp;#128640; Since v4.12.0  Determines whether user has the role NONMEMBER_VIEWER | [optional] 
**lastName** | **String** | User last name | 
**login** | **String** | &amp;#128679; Deprecated since v4.13.0  User login name | [optional] 
**mfaConfig** | [**MfaConfig**](MfaConfig.md) |  | [optional] 
**needsToChangePassword** | **Boolean** | &amp;#128679; Deprecated since v4.13.0  Determines whether user has to change his / her initial password.  use &#x60;authDate.mustChangePassword&#x60; instead | [optional] 
**notifyUser** | **Boolean** | &amp;#128640; Since v4.9.0  Notify user about his new account  * default: &#x60;true&#x60; for &#x60;basic&#x60; auth type  * default: &#x60;false&#x60; for &#x60;active_directory&#x60;, &#x60;openid&#x60; and &#x60;radius&#x60; auth types | [optional] 
**password** | **String** | &amp;#128679; Deprecated since v4.13.0  An initial password may be preset  use &#x60;authData&#x60; instead | [optional] 
**phone** | **String** | Phone number | [optional] 
**receiverLanguage** | **String** | IETF language tag | [optional] 
**title** | **String** | &amp;#128679; Deprecated since v4.18.0  Job title | [optional] 
**userName** | **String** | &amp;#128640; Since v4.13.0  Username | [optional] 


