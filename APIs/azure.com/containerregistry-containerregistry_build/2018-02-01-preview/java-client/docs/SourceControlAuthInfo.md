

# SourceControlAuthInfo

The authorization properties for accessing the source code repository.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiresIn** | **Integer** | Time in seconds that the token remains valid |  [optional] |
|**refreshToken** | **String** | The refresh token used to refresh the access token. |  [optional] |
|**scope** | **String** | The scope of the access token. |  [optional] |
|**token** | **String** | The access token used to access the source control provider. |  |
|**tokenType** | [**TokenTypeEnum**](#TokenTypeEnum) | The type of Auth token. |  [optional] |



## Enum: TokenTypeEnum

| Name | Value |
|---- | -----|
| PAT | &quot;PAT&quot; |
| O_AUTH | &quot;OAuth&quot; |



