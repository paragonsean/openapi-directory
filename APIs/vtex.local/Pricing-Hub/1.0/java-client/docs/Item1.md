

# Item1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**costPrice** | **BigDecimal** | The cost price returned by the pricing API that was used by Pricing Hub. It is measured in cents, so 5000 means 50,00 in local currency. |  |
|**index** | **Integer** | The same index referring to Checkout&#39;s cart that was passed to the API |  |
|**listPrice** | **BigDecimal** | The list price returned by the pricing API that was used by Pricing Hub. It is measured in cents, so 5000 means 50,00 in local currency |  |
|**price** | **BigDecimal** | The price returned by the pricing API that was used by Pricing Hub. It is measured in cents, so 5000 means 50,00 in local currency |  |
|**priceTable** | **String** | The price table that was used to price the item |  |
|**priceValidUntil** | **String** | The moment up until the price is valid. After that moment, it will be necessary to call the pricing API again. The format of the string is in RFC3339 |  |
|**skuId** | **String** | The same skuId that was passed to the API |  |



