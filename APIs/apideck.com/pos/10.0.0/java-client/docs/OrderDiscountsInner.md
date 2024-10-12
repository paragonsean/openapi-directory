

# OrderDiscountsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** |  |  [optional] |
|**currency** | **Currency** |  |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**name** | **String** |  |  [optional] |
|**productId** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**scope** | [**ScopeEnum**](#ScopeEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| ORDER | &quot;order&quot; |
| LINE_ITEM | &quot;line_item&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PERCENTAGE | &quot;percentage&quot; |
| FLAT_FEE | &quot;flat_fee&quot; |



