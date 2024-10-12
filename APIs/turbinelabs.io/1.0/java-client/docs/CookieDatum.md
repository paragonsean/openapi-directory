

# CookieDatum

This describes a cookie that should be set in response to a HTTP request. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domain** | **String** | Specifies the hosts to hich a cookie will be sent. Maps directly to a cookie&#39;s &#39;Domain&#39; attribute.  |  [optional] |
|**expiresInSec** | **Integer** | This indicates how long a cookie will be valid, in seconds. If not set the default is to provide no expiration information. If set to 0 the cookie will have an &#39;Expires&#39; attribute set to &#39;Mon, 1 Jan 0001 12:00:00 UTC&#39;. For values greater than 0 the cookie&#39;s &#39;Max-Age&#39; attribute will be set to that value.  |  [optional] |
|**httpOnly** | **Boolean** | If set the cookie value will not be accessible via Document.cookie. Maps directly to &#39;HttpOnly&#39; attribute.  |  [optional] |
|**name** | **String** | The name of the cookie that will be attached to the response sent. |  [optional] |
|**path** | **String** | Specifies the path a cookie will be associated with. Maps directly to the &#39;Path&#39; attribute.  |  [optional] |
|**sameSite** | [**SameSiteEnum**](#SameSiteEnum) | Allows assertions how a cookie should behave wend making cross-site requests. Maps directly to &#39;SameSite&#39; attribute. If unset no guidance will be included in the cookie.  |  [optional] |
|**secure** | **Boolean** | If set the cookie will only be sent on subsequent requests when accessing a server via HTTPS. Maps directly to &#39;Secure&#39; attribute.  |  [optional] |
|**value** | **String** | A literal value to send as the cookie value or a reference to some metadatum value set on the Cluster Intsance that handles a specific request.  |  [optional] |
|**valueIsLiteral** | **Boolean** | If true then the value attribute is treated as a literal and no attempt to resolve to a server metadatum.  |  [optional] |



## Enum: SameSiteEnum

| Name | Value |
|---- | -----|
| STRICT | &quot;Strict&quot; |
| LAX | &quot;Lax&quot; |



