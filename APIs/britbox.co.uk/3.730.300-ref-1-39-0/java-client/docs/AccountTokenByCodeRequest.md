

# AccountTokenByCodeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | The generated device authorization code. |  |
|**id** | **String** | The unique identifier for the device e.g. serial number. |  |
|**scopes** | [**List&lt;ScopesEnum&gt;**](#List&lt;ScopesEnum&gt;) | The scope(s) of the token(s) required. |  |



## Enum: List&lt;ScopesEnum&gt;

| Name | Value |
|---- | -----|
| CATALOG | &quot;Catalog&quot; |
| COMMERCE | &quot;Commerce&quot; |
| SETTINGS | &quot;Settings&quot; |
| PLAYBACK | &quot;Playback&quot; |



