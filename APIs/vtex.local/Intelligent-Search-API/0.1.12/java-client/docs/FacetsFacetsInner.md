

# FacetsFacetsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hidden** | **Boolean** | Whether the client-side should hide the facet (&#x60;true&#x60;) or not (&#x60;false&#x60;) |  [optional] |
|**name** | **String** | Human-readable format of the facet key. |  [optional] |
|**quantity** | **BigDecimal** | Number of possible values. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Facet type  - &#x60;TEXT&#x60; - The value is a simple text.  - &#x60;PRICERANGE&#x60; - The value contains the property &#x60;range&#x60; representing the minimum and the maximum price for the query.  |  [optional] |
|**values** | [**List&lt;FacetsFacetsInnerValuesInner&gt;**](FacetsFacetsInnerValuesInner.md) | Possible values. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;TEXT&quot; |
| PRICERANGE | &quot;PRICERANGE&quot; |



