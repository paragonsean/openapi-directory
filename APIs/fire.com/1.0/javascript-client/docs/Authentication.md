# FireFinancialServicesBusinessApi.Authentication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | The Client ID for this API Application | [optional] 
**clientSecret** | **String** | The SHA256 hash of the nonce above and the app’s Client Key. The Client Key will only be shown to you when you create the app, so don’t forget to save it somewhere safe. SECRET&#x3D;( &#x60;/bin/echo -n $NONCE$CLIENT_KEY | sha256sum&#x60; ). | [optional] 
**grantType** | **String** | Always &#x60;AccessToken&#x60;. (This will change to &#x60;refresh_token&#x60; in a future release.) | [optional] 
**nonce** | **Number** | A random non-repeating number used as a salt for the &#x60;clientSecret&#x60; below. The simplest nonce is a unix time. | [optional] 
**refreshToken** | **String** | The Refresh Token for this API Application | [optional] 



## Enum: GrantTypeEnum


* `AccessToken` (value: `"AccessToken"`)




