

# Amount

A complex type that describes the value of a monetary amount as represented by a global currency.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currency** | **String** | The base currency applied to the value field to establish a monetary amount. The currency is represented as a 3-letter ISO4217 currency code. For example, the code for the Canadian Dollar is CAD. Default: The default currency of the eBay marketplace that hosts the listing. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/negotiation/types/bas:CurrencyCodeEnum&#39;&gt;eBay API documentation&lt;/a&gt; |  [optional] |
|**value** | **String** | The monetary amount in the specified currency. |  [optional] |



