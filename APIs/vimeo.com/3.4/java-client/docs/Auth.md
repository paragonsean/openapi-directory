

# Auth


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessToken** | **String** | The access token string. |  |
|**app** | [**ApiApp**](ApiApp.md) | The API application associated with the token. |  |
|**expiresOn** | **String** | The date and time that the token expires. |  [optional] |
|**refreshToken** | **String** | The refresh token string. |  [optional] |
|**scope** | **String** | The scope or scopes that the token supports. |  |
|**tokenType** | [**TokenTypeEnum**](#TokenTypeEnum) | The token type:  Option descriptions:  * &#x60;bearer&#x60; - The token is of the &#x60;bearer&#x60; type.  |  |
|**user** | [**User**](User.md) | The user associated with the token. |  [optional] |



## Enum: TokenTypeEnum

| Name | Value |
|---- | -----|
| BEARER | &quot;bearer&quot; |



