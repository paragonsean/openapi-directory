

# OrderPricing


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**discount** | **Integer** | Discount from promotional pricing |  |
|**fees** | [**OrderFee**](OrderFee.md) |  |  |
|**id** | **Double** |  |  [optional] |
|**_list** | **Integer** | Sum of list prices for the entire cart |  |
|**savings** | **Integer** | Savings off of list price &lt;pre&gt;&#x60;savings&#x60; &#x3D; &#x60;list&#x60; - &#x60;subtotal&#x60;&lt;/pre&gt; |  |
|**subtotal** | **Integer** | Price with &#x60;discount&#x60; and without taxes or fees |  |
|**taxDetails** | [**List&lt;LineItemPricingTaxDetail&gt;**](LineItemPricingTaxDetail.md) | A collection of line item tax details |  [optional] |
|**taxes** | **Integer** | Taxes for the entire cart |  |
|**total** | **Integer** | Price the customer pays &lt;pre&gt;&#x60;total&#x60; &#x3D; &#x60;subtotal&#x60; + &#x60;taxes&#x60; + &#x60;fees.total&#x60;&lt;/pre&gt; |  |



