

# ContactType


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **String** |  |  [optional] [readonly] |
|**createdById** | **UUID** | Read-only |  [optional] |
|**deleted** | **String** | Only present if it&#39;s a deleted object |  [optional] [readonly] |
|**description** | **String** |  |  [optional] |
|**id** | **UUID** |  |  [optional] |
|**identifier** | [**IdentifierEnum**](#IdentifierEnum) | One of 3 values |  [optional] |
|**modified** | **String** |  |  [optional] [readonly] |
|**name** | **String** |  |  [optional] |



## Enum: IdentifierEnum

| Name | Value |
|---- | -----|
| CLIENT | &quot;client&quot; |
| PARTNER | &quot;partner&quot; |
| SUPPLIER | &quot;supplier&quot; |



