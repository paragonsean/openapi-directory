# PosApi.OrderTaxesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** |  | [optional] 
**autoApplied** | **Boolean** | Square-only: Determines whether the tax was automatically applied to the order based on the catalog configuration. For an example, see Automatically Apply Taxes to an Order. [https://developer.squareup.com/docs/orders-api/apply-taxes-and-discounts/auto-apply-taxes]() | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**id** | **String** |  | [optional] 
**name** | **String** | The tax&#39;s name. | [optional] 
**percentage** | **Number** |  | [optional] 
**scope** | **String** |  | [optional] 
**type** | **String** |  | [optional] 



## Enum: ScopeEnum


* `order` (value: `"order"`)

* `line_item` (value: `"line_item"`)





## Enum: TypeEnum


* `unknown` (value: `"unknown"`)

* `additive` (value: `"additive"`)

* `inclusive` (value: `"inclusive"`)




