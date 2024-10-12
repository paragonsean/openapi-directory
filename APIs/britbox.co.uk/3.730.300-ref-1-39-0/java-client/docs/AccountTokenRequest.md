

# AccountTokenRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cookieType** | [**CookieTypeEnum**](#CookieTypeEnum) | If you specify a cookie type then a content filter cookie will be returned along with the token(s). This is only intended for web based clients which need to pass the cookies to a server to render a page based on the user&#39;s content filters e.g subscription code.  If type &#x60;Session&#x60; the cookie will be session based. If type &#x60;Persistent&#x60; the cookie will have a medium term lifespan. If undefined no cookies will be set.  |  [optional] |
|**email** | **String** | The email associated with the account. |  |
|**password** | **String** | The password associated with the account. |  |
|**scopes** | [**List&lt;ScopesEnum&gt;**](#List&lt;ScopesEnum&gt;) | The scope(s) of the tokens required. For each scope listed an Account and Profile token of that scope will be returned  |  |



## Enum: CookieTypeEnum

| Name | Value |
|---- | -----|
| SESSION | &quot;Session&quot; |
| PERSISTENT | &quot;Persistent&quot; |



## Enum: List&lt;ScopesEnum&gt;

| Name | Value |
|---- | -----|
| CATALOG | &quot;Catalog&quot; |
| COMMERCE | &quot;Commerce&quot; |
| SETTINGS | &quot;Settings&quot; |
| PLAYBACK | &quot;Playback&quot; |



