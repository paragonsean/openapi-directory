

# UserAuthData

User Authentication Data

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adConfigId** | **Integer** | ID of the user&#39;s Active Directory. |  [optional] |
|**login** | **String** | User login name |  [optional] |
|**method** | **String** | Authentication method    Authentication methods:  * &#x60;basic&#x60;  * &#x60;active_directory&#x60;  * &#x60;radius&#x60;  * &#x60;openid&#x60; |  |
|**mustChangePassword** | **Boolean** | Determines whether user has to change his / her password  * default: &#x60;true&#x60; for &#x60;basic&#x60; auth type  * default: &#x60;false&#x60; for &#x60;active_directory&#x60;, &#x60;openid&#x60; and &#x60;radius&#x60; auth types |  [optional] |
|**oidConfigId** | **Integer** | ID of the user&#39;s OIDC provider. |  [optional] |
|**password** | **String** | Password (only relevant for &#x60;basic&#x60; authentication type)  *NOT* your Active Directory, OpenID or RADIUS password! |  [optional] |



