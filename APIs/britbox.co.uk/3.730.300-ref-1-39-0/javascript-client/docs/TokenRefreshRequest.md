# RocketServices.TokenRefreshRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookieType** | **String** | If you specify a cookie type then a content filter cookie will be returned along with the token(s). This is only intended for web based clients which need to pass the cookies to a server to render a page based on the user&#39;s content filters e.g subscription code.  If type &#x60;Session&#x60; the cookie will be session based. If type &#x60;Persistent&#x60; the cookie will have a medium term lifespan. If undefined no cookies will be set.  | [optional] 
**token** | **String** | The token to refresh. | 



## Enum: CookieTypeEnum


* `Session` (value: `"Session"`)

* `Persistent` (value: `"Persistent"`)




