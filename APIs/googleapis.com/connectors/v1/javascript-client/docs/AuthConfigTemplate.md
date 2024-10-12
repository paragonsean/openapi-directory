# ConnectorsApi.AuthConfigTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authKey** | **String** | Identifier key for auth config | [optional] 
**authType** | **String** | The type of authentication configured. | [optional] 
**configVariableTemplates** | [**[ConfigVariableTemplate]**](ConfigVariableTemplate.md) | Config variables to describe an &#x60;AuthConfig&#x60; for a &#x60;Connection&#x60;. | [optional] 
**description** | **String** | Connector specific description for an authentication template. | [optional] 
**displayName** | **String** | Display name for authentication template. | [optional] 



## Enum: AuthTypeEnum


* `AUTH_TYPE_UNSPECIFIED` (value: `"AUTH_TYPE_UNSPECIFIED"`)

* `USER_PASSWORD` (value: `"USER_PASSWORD"`)

* `OAUTH2_JWT_BEARER` (value: `"OAUTH2_JWT_BEARER"`)

* `OAUTH2_CLIENT_CREDENTIALS` (value: `"OAUTH2_CLIENT_CREDENTIALS"`)

* `SSH_PUBLIC_KEY` (value: `"SSH_PUBLIC_KEY"`)

* `OAUTH2_AUTH_CODE_FLOW` (value: `"OAUTH2_AUTH_CODE_FLOW"`)

* `GOOGLE_AUTHENTICATION` (value: `"GOOGLE_AUTHENTICATION"`)




