

# AuthConfig

AuthConfig defines details of a authentication type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalVariables** | [**List&lt;ConfigVariable&gt;**](ConfigVariable.md) | List containing additional auth configs. |  [optional] |
|**authKey** | **String** | Identifier key for auth config |  [optional] |
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) | The type of authentication configured. |  [optional] |
|**oauth2AuthCodeFlow** | [**Oauth2AuthCodeFlow**](Oauth2AuthCodeFlow.md) |  |  [optional] |
|**oauth2ClientCredentials** | [**Oauth2ClientCredentials**](Oauth2ClientCredentials.md) |  |  [optional] |
|**oauth2JwtBearer** | [**Oauth2JwtBearer**](Oauth2JwtBearer.md) |  |  [optional] |
|**sshPublicKey** | [**SshPublicKey**](SshPublicKey.md) |  |  [optional] |
|**userPassword** | [**UserPassword**](UserPassword.md) |  |  [optional] |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| AUTH_TYPE_UNSPECIFIED | &quot;AUTH_TYPE_UNSPECIFIED&quot; |
| USER_PASSWORD | &quot;USER_PASSWORD&quot; |
| OAUTH2_JWT_BEARER | &quot;OAUTH2_JWT_BEARER&quot; |
| OAUTH2_CLIENT_CREDENTIALS | &quot;OAUTH2_CLIENT_CREDENTIALS&quot; |
| SSH_PUBLIC_KEY | &quot;SSH_PUBLIC_KEY&quot; |
| OAUTH2_AUTH_CODE_FLOW | &quot;OAUTH2_AUTH_CODE_FLOW&quot; |
| GOOGLE_AUTHENTICATION | &quot;GOOGLE_AUTHENTICATION&quot; |



