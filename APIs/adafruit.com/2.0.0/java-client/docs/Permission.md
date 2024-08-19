

# Permission


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** |  |  [optional] [readonly] |
|**id** | **BigDecimal** |  |  [optional] [readonly] |
|**model** | [**ModelEnum**](#ModelEnum) |  |  [optional] |
|**objectId** | **BigDecimal** |  |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) |  |  [optional] |
|**scopeValue** | **String** |  |  [optional] |
|**updatedAt** | **String** |  |  [optional] [readonly] |
|**userId** | **BigDecimal** |  |  [optional] [readonly] |



## Enum: ModelEnum

| Name | Value |
|---- | -----|
| FEED | &quot;feed&quot; |
| GROUP | &quot;group&quot; |
| DASHBOARD | &quot;dashboard&quot; |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| SECRET | &quot;secret&quot; |
| PUBLIC | &quot;public&quot; |
| USER | &quot;user&quot; |
| ORGANIZATION | &quot;organization&quot; |



