

# ExchangeAuthCodeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | The authorization code received from the authorization server. |  |
|**grantType** | [**GrantTypeEnum**](#GrantTypeEnum) | The grant type. Must be set to &#x60;authorization_code&#x60;. |  |
|**redirectUri** | **String** | The redirect URI. Must match the URI from &#x60;/oauth/authorize&#x60;. |  |



## Enum: GrantTypeEnum

| Name | Value |
|---- | -----|
| AUTHORIZATION_CODE | &quot;authorization_code&quot; |



