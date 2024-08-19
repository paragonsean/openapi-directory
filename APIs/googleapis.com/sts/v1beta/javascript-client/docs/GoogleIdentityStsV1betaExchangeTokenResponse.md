# SecurityTokenServiceApi.GoogleIdentityStsV1betaExchangeTokenResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | An OAuth 2.0 security token, issued by Google, in response to the token exchange request. Tokens can vary in size, depending in part on the size of mapped claims, up to a maximum of 12288 bytes (12 KB). Google reserves the right to change the token size and the maximum length at any time. | [optional] 
**expiresIn** | **Number** | The amount of time, in seconds, between the time when the access token was issued and the time when the access token will expire. This field is absent when the &#x60;subject_token&#x60; in the request is a Google-issued, short-lived access token. In this case, the access token has the same expiration time as the &#x60;subject_token&#x60;. | [optional] 
**issuedTokenType** | **String** | The token type. Always matches the value of &#x60;requested_token_type&#x60; from the request. | [optional] 
**tokenType** | **String** | The type of access token. Always has the value &#x60;Bearer&#x60;. | [optional] 


