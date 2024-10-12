# OpenapiJsClient.LineItemPricing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount** | **Number** | Discount off of sale price for given &#x60;quantity&#x60; and &#x60;period&#x60; &lt;pre&gt;&#x60;discount&#x60; &#x3D; &#x60;sale&#x60; - &#x60;subtotal&#x60;&lt;/pre&gt; | 
**fees** | [**OrderFee**](OrderFee.md) |  | 
**list** | **Number** | List price for given &#x60;quantity&#x60; and &#x60;period&#x60; | 
**sale** | **Number** | Actual price for the current product | 
**savings** | **Number** | Savings off of list price for given &#x60;quantity&#x60; and &#x60;period&#x60; &lt;pre&gt;&#x60;savings&#x60; &#x3D; &#x60;list&#x60; - &#x60;subtotal&#x60;&lt;/pre&gt; | 
**subtotal** | **Number** | Price with any discounts and without taxes or fees for given &#x60;quantity&#x60; and &#x60;period&#x60; | 
**taxes** | **Number** | Taxes for given &#x60;quantity&#x60; and &#x60;period&#x60; | 
**unit** | **Object** | Pricing for a single unit of the given item | 


