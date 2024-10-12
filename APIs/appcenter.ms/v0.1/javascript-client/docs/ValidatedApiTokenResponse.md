# AppCenterClient.ValidatedApiTokenResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claims** | [**[ValidatedApiTokenResponseClaimsInner]**](ValidatedApiTokenResponseClaimsInner.md) | Collection of attributes that describe the principal of the specified API Token | 
**principalId** | **String** | The ID of the owner of the API Token (user_id or app_id) | 
**principalType** | **String** | Indicates the type of the principal (app or user) | 
**tokenId** | **String** | The token&#39;s unique id (UUID) | 
**tokenScope** | **[String]** | The token&#39;s scope. A list of allowed roles. | 



## Enum: PrincipalTypeEnum


* `app` (value: `"app"`)

* `user` (value: `"user"`)





## Enum: [TokenScopeEnum]


* `all` (value: `"all"`)

* `in_app_update` (value: `"in_app_update"`)

* `viewer` (value: `"viewer"`)




