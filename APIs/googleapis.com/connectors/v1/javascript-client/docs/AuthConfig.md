# ConnectorsApi.AuthConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalVariables** | [**[ConfigVariable]**](ConfigVariable.md) | List containing additional auth configs. | [optional] 
**authKey** | **String** | Identifier key for auth config | [optional] 
**authType** | **String** | The type of authentication configured. | [optional] 
**oauth2AuthCodeFlow** | [**Oauth2AuthCodeFlow**](Oauth2AuthCodeFlow.md) |  | [optional] 
**oauth2ClientCredentials** | [**Oauth2ClientCredentials**](Oauth2ClientCredentials.md) |  | [optional] 
**oauth2JwtBearer** | [**Oauth2JwtBearer**](Oauth2JwtBearer.md) |  | [optional] 
**sshPublicKey** | [**SshPublicKey**](SshPublicKey.md) |  | [optional] 
**userPassword** | [**UserPassword**](UserPassword.md) |  | [optional] 



## Enum: AuthTypeEnum


* `AUTH_TYPE_UNSPECIFIED` (value: `"AUTH_TYPE_UNSPECIFIED"`)

* `USER_PASSWORD` (value: `"USER_PASSWORD"`)

* `OAUTH2_JWT_BEARER` (value: `"OAUTH2_JWT_BEARER"`)

* `OAUTH2_CLIENT_CREDENTIALS` (value: `"OAUTH2_CLIENT_CREDENTIALS"`)

* `SSH_PUBLIC_KEY` (value: `"SSH_PUBLIC_KEY"`)

* `OAUTH2_AUTH_CODE_FLOW` (value: `"OAUTH2_AUTH_CODE_FLOW"`)

* `GOOGLE_AUTHENTICATION` (value: `"GOOGLE_AUTHENTICATION"`)




