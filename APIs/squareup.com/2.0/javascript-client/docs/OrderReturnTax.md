# SquareConnectApi.OrderReturnTax

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliedMoney** | [**Money**](Money.md) |  | [optional] 
**catalogObjectId** | **String** | The catalog object ID referencing [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax). | [optional] 
**catalogVersion** | **Number** | The version of the catalog object that this tax references. | [optional] 
**name** | **String** | The tax&#39;s name. | [optional] 
**percentage** | **String** | The percentage of the tax, as a string representation of a decimal number. For example, a value of &#x60;\&quot;7.25\&quot;&#x60; corresponds to a percentage of 7.25%. | [optional] 
**scope** | **String** | Indicates the level at which the &#x60;OrderReturnTax&#x60; applies. For &#x60;ORDER&#x60; scoped taxes, Square generates references in &#x60;applied_taxes&#x60; on all &#x60;OrderReturnLineItem&#x60;s. For &#x60;LINE_ITEM&#x60; scoped taxes, the tax is only applied to &#x60;OrderReturnLineItem&#x60;s with references in their &#x60;applied_discounts&#x60; field. | [optional] 
**sourceTaxUid** | **String** | The tax &#x60;uid&#x60; from the order that contains the original tax charge. | [optional] 
**type** | **String** | Indicates the calculation method used to apply the tax. | [optional] 
**uid** | **String** | A unique ID that identifies the returned tax only within this order. | [optional] 


