

# QuoteDataShippingMethodInterface

Interface ShippingMethodInterface

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** | Shipping amount in store currency. |  |
|**available** | **Boolean** | The value of the availability flag for the current shipping method. |  |
|**baseAmount** | **BigDecimal** | Shipping amount in base currency. |  |
|**carrierCode** | **String** | Shipping carrier code. |  |
|**carrierTitle** | **String** | Shipping carrier title. Otherwise, null. |  [optional] |
|**errorMessage** | **String** | Shipping Error message. |  |
|**extensionAttributes** | **Object** | ExtensionInterface class for @see \\Magento\\Quote\\Api\\Data\\ShippingMethodInterface |  [optional] |
|**methodCode** | **String** | Shipping method code. |  |
|**methodTitle** | **String** | Shipping method title. Otherwise, null. |  [optional] |
|**priceExclTax** | **BigDecimal** | Shipping price excl tax. |  |
|**priceInclTax** | **BigDecimal** | Shipping price incl tax. |  |



