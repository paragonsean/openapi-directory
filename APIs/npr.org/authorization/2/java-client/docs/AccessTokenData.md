

# AccessTokenData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessToken** | **String** | The access token to use for all future calls |  |
|**expiresIn** | **Integer** | The remaining lifetime of the access token (in seconds) |  |
|**refreshToken** | **String** | The refresh token that can be used to obtain a new access token if the old one expires; if a refresh token is returned, it is the client&#39;s responsibility to securely cache it for future use. |  [optional] |
|**tokenType** | [**TokenTypeEnum**](#TokenTypeEnum) | Identifies the type of token returned. At this time, this field always has the value &#x60;Bearer&#x60;. |  |



## Enum: TokenTypeEnum

| Name | Value |
|---- | -----|
| BEARER | &quot;Bearer&quot; |
| MAC | &quot;MAC&quot; |



