

# AuthConfigTemplate

AuthConfigTemplate defines required field over an authentication type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authKey** | **String** | Identifier key for auth config |  [optional] |
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) | The type of authentication configured. |  [optional] |
|**configVariableTemplates** | [**List&lt;ConfigVariableTemplate&gt;**](ConfigVariableTemplate.md) | Config variables to describe an &#x60;AuthConfig&#x60; for a &#x60;Connection&#x60;. |  [optional] |
|**description** | **String** | Connector specific description for an authentication template. |  [optional] |
|**displayName** | **String** | Display name for authentication template. |  [optional] |



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



