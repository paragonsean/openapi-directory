# AppCenterClient.ApiTokensPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of the token | [optional] 
**encryptedToken** | **String** | An encrypted value of the token. | [optional] 
**scope** | **[String]** | The scope for this token. An array of supported roles. | [optional] 
**tokenHash** | **String** | The hashed value of api token | [optional] 
**tokenType** | **String** | The token&#39;s type. public:managed by the user; in_app_update:special token for in-app update scenario; buid:dedicated for CI usage for now; session:for CLI session management; tester_app: used for tester mobile app; default is \&quot;public\&quot;.&#39; | [optional] 



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




