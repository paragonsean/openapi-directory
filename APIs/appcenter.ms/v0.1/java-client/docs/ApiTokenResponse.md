

# ApiTokenResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | The creation time |  |
|**description** | **String** | The description of the token |  [optional] |
|**encryptedToken** | **String** | The encrypted value of a token. This value will only be returned for token of type in_app_update. |  [optional] |
|**id** | **UUID** | The unique id (UUID) of the api token |  |
|**scope** | [**List&lt;ScopeEnum&gt;**](#List&lt;ScopeEnum&gt;) | The token&#39;s scope. A list of allowed roles. |  [optional] |



## Enum: List&lt;ScopeEnum&gt;

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| IN_APP_UPDATE | &quot;in_app_update&quot; |
| VIEWER | &quot;viewer&quot; |



