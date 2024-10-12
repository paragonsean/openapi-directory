

# OrderTaxesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** |  |  [optional] |
|**autoApplied** | **Boolean** | Square-only: Determines whether the tax was automatically applied to the order based on the catalog configuration. For an example, see Automatically Apply Taxes to an Order. [https://developer.squareup.com/docs/orders-api/apply-taxes-and-discounts/auto-apply-taxes]() |  [optional] |
|**currency** | **Currency** |  |  [optional] |
|**id** | **String** |  |  [optional] |
|**name** | **String** | The tax&#39;s name. |  [optional] |
|**percentage** | **BigDecimal** |  |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| ORDER | &quot;order&quot; |
| LINE_ITEM | &quot;line_item&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| ADDITIVE | &quot;additive&quot; |
| INCLUSIVE | &quot;inclusive&quot; |



