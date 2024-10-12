# DataformApi.GitRemoteSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticationTokenSecretVersion** | **String** | Optional. The name of the Secret Manager secret version to use as an authentication token for Git operations. Must be in the format &#x60;projects/_*_/secrets/_*_/versions/_*&#x60;. | [optional] 
**defaultBranch** | **String** | Required. The Git remote&#39;s default branch name. | [optional] 
**sshAuthenticationConfig** | [**SshAuthenticationConfig**](SshAuthenticationConfig.md) |  | [optional] 
**tokenStatus** | **String** | Output only. Deprecated: The field does not contain any token status information. Instead use https://cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories/computeAccessTokenStatus | [optional] [readonly] 
**url** | **String** | Required. The Git remote&#39;s URL. | [optional] 



## Enum: TokenStatusEnum


* `TOKEN_STATUS_UNSPECIFIED` (value: `"TOKEN_STATUS_UNSPECIFIED"`)

* `NOT_FOUND` (value: `"NOT_FOUND"`)

* `INVALID` (value: `"INVALID"`)

* `VALID` (value: `"VALID"`)




