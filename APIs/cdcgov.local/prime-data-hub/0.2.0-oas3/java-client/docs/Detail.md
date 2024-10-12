

# Detail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detail** | **String** | The details of the error |  [optional] |
|**id** | **String** | Depends on scope, either the item&#39;s id (message_id) or the report&#39;s id |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | Does the error apply to one item |  [optional] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| PARAMETER | &quot;Parameter&quot; |
| REPORT | &quot;Report&quot; |
| ITEM | &quot;Item&quot; |



