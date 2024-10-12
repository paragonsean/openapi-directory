

# CreateTokenRequestDataAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** | Contact Fitbit Plus API Support to get a client id and secret. |  |
|**clientSecret** | **String** | Contact Fitbit Plus API Support to get a client id and secret. Secret is required if grant_type is \&quot;client_credentials\&quot; |  [optional] |
|**grantType** | [**GrantTypeEnum**](#GrantTypeEnum) |  |  |
|**refreshToken** | **String** | Required if grant_type is \&quot;refresh_token\&quot; |  [optional] |



## Enum: GrantTypeEnum

| Name | Value |
|---- | -----|
| REFRESH_TOKEN | &quot;refresh_token&quot; |
| CLIENT_CREDENTIALS | &quot;client_credentials&quot; |



