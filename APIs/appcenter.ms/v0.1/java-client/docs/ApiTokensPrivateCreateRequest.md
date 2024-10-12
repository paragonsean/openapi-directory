

# ApiTokensPrivateCreateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the token |  [optional] |
|**principalId** | **UUID** | The principal ID assigned to the API token |  |
|**principalType** | [**PrincipalTypeEnum**](#PrincipalTypeEnum) | The principal type assigned to the API token |  |
|**scope** | [**List&lt;ScopeEnum&gt;**](#List&lt;ScopeEnum&gt;) | The scope for this token (default \&quot;all\&quot;). |  [optional] |
|**tokenType** | [**TokenTypeEnum**](#TokenTypeEnum) | The token&#39;s type (default \&quot;public\&quot;)   public: managed by the user   in_app_update: special token for in-app update scenario   buid: dedicated for CI usage for now   session: for CLI session management   tester_app: used for tester mobile app |  [optional] |



## Enum: PrincipalTypeEnum

| Name | Value |
|---- | -----|
| APP | &quot;app&quot; |
| USER | &quot;user&quot; |



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



