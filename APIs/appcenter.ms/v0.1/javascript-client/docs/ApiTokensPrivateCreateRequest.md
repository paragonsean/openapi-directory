# AppCenterClient.ApiTokensPrivateCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of the token | [optional] 
**principalId** | **String** | The principal ID assigned to the API token | 
**principalType** | **String** | The principal type assigned to the API token | 
**scope** | **[String]** | The scope for this token (default \&quot;all\&quot;). | [optional] 
**tokenType** | **String** | The token&#39;s type (default \&quot;public\&quot;)   public: managed by the user   in_app_update: special token for in-app update scenario   buid: dedicated for CI usage for now   session: for CLI session management   tester_app: used for tester mobile app | [optional] 



## Enum: PrincipalTypeEnum


* `app` (value: `"app"`)

* `user` (value: `"user"`)





## Enum: [ScopeEnum]


* `all` (value: `"all"`)

* `in_app_update` (value: `"in_app_update"`)

* `viewer` (value: `"viewer"`)





## Enum: TokenTypeEnum


* `public` (value: `"public"`)

* `in_app_update` (value: `"in_app_update"`)

* `build` (value: `"build"`)

* `session` (value: `"session"`)

* `tester_app` (value: `"tester_app"`)




