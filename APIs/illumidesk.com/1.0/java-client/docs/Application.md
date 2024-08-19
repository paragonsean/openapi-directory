

# Application


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationGrantType** | [**AuthorizationGrantTypeEnum**](#AuthorizationGrantTypeEnum) | OAuth2 authorization grant type |  [optional] |
|**clientId** | **String** | OAuth2 client id |  [optional] |
|**clientSecret** | **String** | OAuth2 client secret |  [optional] |
|**clientType** | [**ClientTypeEnum**](#ClientTypeEnum) | OAuth2 client type |  [optional] |
|**id** | **String** | Application unique identifier, expressed as UUID. |  [optional] |
|**name** | **String** | Application name |  [optional] |
|**redirectUris** | **String** | Uris to redirect auth request |  [optional] |



## Enum: AuthorizationGrantTypeEnum

| Name | Value |
|---- | -----|
| AUTHORIZATION_CODE | &quot;authorization-code&quot; |
| IMPLICIT | &quot;implicit&quot; |
| PASSWORD | &quot;password&quot; |
| CLIENT_CREDENTIALS | &quot;client-credentials&quot; |



## Enum: ClientTypeEnum

| Name | Value |
|---- | -----|
| CONFIDENTIAL | &quot;confidential&quot; |
| PUBLIC | &quot;public&quot; |



