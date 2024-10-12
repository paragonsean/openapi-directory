# OpenapiJsClient.OrderPricing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount** | **Number** | Discount from promotional pricing | 
**fees** | [**OrderFee**](OrderFee.md) |  | 
**id** | **Number** |  | [optional] 
**list** | **Number** | Sum of list prices for the entire cart | 
**savings** | **Number** | Savings off of list price &lt;pre&gt;&#x60;savings&#x60; &#x3D; &#x60;list&#x60; - &#x60;subtotal&#x60;&lt;/pre&gt; | 
**subtotal** | **Number** | Price with &#x60;discount&#x60; and without taxes or fees | 
**taxDetails** | [**[LineItemPricingTaxDetail]**](LineItemPricingTaxDetail.md) | A collection of line item tax details | [optional] 
**taxes** | **Number** | Taxes for the entire cart | 
**total** | **Number** | Price the customer pays &lt;pre&gt;&#x60;total&#x60; &#x3D; &#x60;subtotal&#x60; + &#x60;taxes&#x60; + &#x60;fees.total&#x60;&lt;/pre&gt; | 


