# PricingApi.CreateUpdatePriceOrFixedPriceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basePrice** | **Number** | SKU selling base price. If you decide to fill only the &#x60;basePrice&#x60; item, the &#x60;markup&#x60; and &#x60;costPrice&#x60; will be automatically generated to adapt to the number inserted in &#x60;basePrice&#x60;. | [default to 100]
**costPrice** | **Number** | SKU selling cost price. If you decide to fill the &#x60;costPrice&#x60; item, you must also fill the &#x60;markup&#x60; and &#x60;basePrice&#x60; will be automatically generated based on both values. | [optional] [default to 35]
**fixedPrices** | [**[FixedPrices]**](FixedPrices.md) |  | [optional] 
**listPrice** | **Number** | SKU&#39;s suggested selling price. | [default to 50]
**markup** | **Number** | The profit percentage that is to be obtained from the sale of that SKU. If you decide to fill the &#x60;markup&#x60; item, you must also fill the &#x60;costPrice&#x60;. The &#x60;basePrice&#x60; will be automatically generated based on both values. | [default to 30]


