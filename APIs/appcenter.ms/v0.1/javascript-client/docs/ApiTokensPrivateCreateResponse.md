# AppCenterClient.ApiTokensPrivateCreateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiToken** | **String** | The api token generated will not be accessible again | 
**createdAt** | **String** | The creation time | 
**description** | **String** | The description of the token | [optional] 
**encryptedToken** | **String** | The encrypted value of a token. This value will only be returned for token of type in_app_update. | [optional] 
**id** | **String** | The unique id (UUID) of the api token | 
**scope** | **[String]** | The scope for this token. | [optional] 



## Enum: [ScopeEnum]


* `all` (value: `"all"`)

* `in_app_update` (value: `"in_app_update"`)

* `viewer` (value: `"viewer"`)




