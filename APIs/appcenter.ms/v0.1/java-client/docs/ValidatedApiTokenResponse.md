

# ValidatedApiTokenResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**claims** | [**List&lt;ValidatedApiTokenResponseClaimsInner&gt;**](ValidatedApiTokenResponseClaimsInner.md) | Collection of attributes that describe the principal of the specified API Token |  |
|**principalId** | **UUID** | The ID of the owner of the API Token (user_id or app_id) |  |
|**principalType** | [**PrincipalTypeEnum**](#PrincipalTypeEnum) | Indicates the type of the principal (app or user) |  |
|**tokenId** | **UUID** | The token&#39;s unique id (UUID) |  |
|**tokenScope** | [**List&lt;TokenScopeEnum&gt;**](#List&lt;TokenScopeEnum&gt;) | The token&#39;s scope. A list of allowed roles. |  |



## Enum: PrincipalTypeEnum

| Name | Value |
|---- | -----|
| APP | &quot;app&quot; |
| USER | &quot;user&quot; |



## Enum: List&lt;TokenScopeEnum&gt;

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| IN_APP_UPDATE | &quot;in_app_update&quot; |
| VIEWER | &quot;viewer&quot; |



