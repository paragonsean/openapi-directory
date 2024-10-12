

# ApiTokensCreateResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiToken** | **String** | The api token generated will not be accessible again |  |
|**createdAt** | **String** | The creation time |  |
|**description** | **String** | The description of the token |  [optional] |
|**id** | **String** | The unique id (UUID) of the api token |  |
|**scope** | [**List&lt;ScopeEnum&gt;**](#List&lt;ScopeEnum&gt;) | The scope for this token. |  [optional] |



## Enum: List&lt;ScopeEnum&gt;

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| VIEWER | &quot;viewer&quot; |



