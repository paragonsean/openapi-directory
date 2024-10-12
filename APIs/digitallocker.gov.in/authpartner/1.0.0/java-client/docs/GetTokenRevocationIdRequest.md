

# GetTokenRevocationIdRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**token** | **String** | The token that needs to be revoked. |  |
|**tokenTypeHint** | [**TokenTypeHintEnum**](#TokenTypeHintEnum) | The type of the above token. The value will be one of access_token or refresh_token. If this parameter is not sent, DigiLocker will look for this token in both access and refresh tokens and then revoke it. |  [optional] |



## Enum: TokenTypeHintEnum

| Name | Value |
|---- | -----|
| REFRESH_TOKEN | &quot;refresh_token&quot; |
| ACCESS_TOKEN | &quot;access_token&quot; |



