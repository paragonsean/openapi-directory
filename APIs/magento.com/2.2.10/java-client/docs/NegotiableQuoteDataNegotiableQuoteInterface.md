

# NegotiableQuoteDataNegotiableQuoteInterface

Interface NegotiableQuoteInterface

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appliedRuleIds** | **String** | Quote rules. |  |
|**baseNegotiatedTotalPrice** | **BigDecimal** | Quote negotiated total price in base currency. |  [optional] |
|**baseOriginalTotalPrice** | **BigDecimal** | Quote original total price in base currency. |  [optional] |
|**creatorId** | **Integer** | Quote creator id. |  |
|**creatorType** | **Integer** | Quote creator type. |  |
|**deletedSku** | **String** | Deleted products sku. |  |
|**emailNotificationStatus** | **Integer** | Email notification status. |  |
|**expirationPeriod** | **String** | Expiration period. |  |
|**extensionAttributes** | **Object** | ExtensionInterface class for @see \\Magento\\NegotiableQuote\\Api\\Data\\NegotiableQuoteInterface |  [optional] |
|**hasUnconfirmedChanges** | **Boolean** | Has unconfirmed changes. |  |
|**isAddressDraft** | **Boolean** | Is address draft. |  |
|**isCustomerPriceChanged** | **Boolean** | Customer price changes. |  |
|**isRegularQuote** | **Boolean** | Is regular quote. |  |
|**isShippingTaxChanged** | **Boolean** | Shipping tax changes. |  |
|**negotiatedPriceType** | **Integer** | Negotiated price type. |  |
|**negotiatedPriceValue** | **BigDecimal** | Negotiated price value. |  |
|**negotiatedTotalPrice** | **BigDecimal** | Quote negotiated total price. |  [optional] |
|**notifications** | **Integer** | Quote notifications. |  |
|**originalTotalPrice** | **BigDecimal** | Quote original total price. |  [optional] |
|**quoteId** | **Integer** | Negotiable quote ID. |  |
|**quoteName** | **String** | Negotiable quote name. |  |
|**shippingPrice** | **BigDecimal** | Proposed shipping price. |  |
|**status** | **String** | Negotiable quote status. |  |



