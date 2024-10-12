# ContainerRegistryManagementClient.AuthInfoUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiresIn** | **Number** | Time in seconds that the token remains valid | [optional] 
**refreshToken** | **String** | The refresh token used to refresh the access token. | [optional] 
**scope** | **String** | The scope of the access token. | [optional] 
**token** | **String** | The access token used to access the source control provider. | [optional] 
**tokenType** | **String** | The type of Auth token. | [optional] 



## Enum: TokenTypeEnum


* `PAT` (value: `"PAT"`)

* `OAuth` (value: `"OAuth"`)




