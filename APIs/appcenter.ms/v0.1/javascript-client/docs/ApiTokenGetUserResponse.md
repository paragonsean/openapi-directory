# AppCenterClient.ApiTokenGetUserResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tokenId** | **String** | The token&#39;s unique id (UUID) | 
**tokenScope** | **[String]** | The token&#39;s scope. A list of allowed roles. | 
**userEmail** | **String** | The user email | 
**userId** | **String** | The unique id (UUID) of the user | 
**userOrigin** | **String** | The creation origin of the user who created this api token | 



## Enum: [TokenScopeEnum]


* `all` (value: `"all"`)

* `in_app_update` (value: `"in_app_update"`)

* `viewer` (value: `"viewer"`)





## Enum: UserOriginEnum


* `appcenter` (value: `"appcenter"`)

* `hockeyapp` (value: `"hockeyapp"`)

* `codepush` (value: `"codepush"`)




