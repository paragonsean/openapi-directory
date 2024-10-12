# AppCenterClient.ApiTokenResponsev2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **String** | The creation time | 
**description** | **String** | The description of the token | [optional] 
**encryptedToken** | **String** | The encrypted value of a token. This value will only be returned for token of type in_app_update. | [optional] 
**id** | **String** | The unique id (UUID) of the api token | 
**scope** | **[String]** | The token&#39;s scope. A list of allowed roles. | [optional] 



## Enum: [ScopeEnum]


* `all` (value: `"all"`)

* `in_app_update` (value: `"in_app_update"`)

* `viewer` (value: `"viewer"`)




