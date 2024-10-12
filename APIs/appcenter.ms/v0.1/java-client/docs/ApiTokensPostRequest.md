

# ApiTokensPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the token |  [optional] |
|**encryptedToken** | **String** | An encrypted value of the token. |  [optional] |
|**scope** | [**List&lt;ScopeEnum&gt;**](#List&lt;ScopeEnum&gt;) | The scope for this token. An array of supported roles. |  [optional] |
|**tokenHash** | **String** | The hashed value of api token |  [optional] |
|**tokenType** | [**TokenTypeEnum**](#TokenTypeEnum) | The token&#39;s type. public:managed by the user; in_app_update:special token for in-app update scenario; buid:dedicated for CI usage for now; session:for CLI session management; tester_app: used for tester mobile app; default is \&quot;public\&quot;.&#39; |  [optional] |



## Enum: List&lt;ScopeEnum&gt;

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| IN_APP_UPDATE | &quot;in_app_update&quot; |
| VIEWER | &quot;viewer&quot; |



## Enum: TokenTypeEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| IN_APP_UPDATE | &quot;in_app_update&quot; |
| BUILD | &quot;build&quot; |
| SESSION | &quot;session&quot; |
| TESTER_APP | &quot;tester_app&quot; |



