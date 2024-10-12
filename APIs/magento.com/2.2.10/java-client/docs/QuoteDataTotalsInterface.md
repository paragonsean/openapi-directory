

# QuoteDataTotalsInterface

Interface TotalsInterface

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseCurrencyCode** | **String** | Base currency code |  [optional] |
|**baseDiscountAmount** | **BigDecimal** | Discount amount in base currency |  [optional] |
|**baseGrandTotal** | **BigDecimal** | Grand total in base currency |  [optional] |
|**baseShippingAmount** | **BigDecimal** | Shipping amount in base currency |  [optional] |
|**baseShippingDiscountAmount** | **BigDecimal** | Shipping discount amount in base currency |  [optional] |
|**baseShippingInclTax** | **BigDecimal** | Shipping including tax in base currency |  [optional] |
|**baseShippingTaxAmount** | **BigDecimal** | Shipping tax amount in base currency |  [optional] |
|**baseSubtotal** | **BigDecimal** | Subtotal in base currency |  [optional] |
|**baseSubtotalInclTax** | **BigDecimal** | Subtotal including tax in base currency |  [optional] |
|**baseSubtotalWithDiscount** | **BigDecimal** | Subtotal in base currency with applied discount |  [optional] |
|**baseTaxAmount** | **BigDecimal** | Tax amount in base currency |  [optional] |
|**couponCode** | **String** | Applied coupon code |  [optional] |
|**discountAmount** | **BigDecimal** | Discount amount in quote currency |  [optional] |
|**extensionAttributes** | [**QuoteDataTotalsExtensionInterface**](QuoteDataTotalsExtensionInterface.md) |  |  [optional] |
|**grandTotal** | **BigDecimal** | Grand total in quote currency |  [optional] |
|**items** | [**List&lt;QuoteDataTotalsItemInterface&gt;**](QuoteDataTotalsItemInterface.md) | Totals by items |  [optional] |
|**itemsQty** | **Integer** | Items qty |  [optional] |
|**quoteCurrencyCode** | **String** | Quote currency code |  [optional] |
|**shippingAmount** | **BigDecimal** | Shipping amount in quote currency |  [optional] |
|**shippingDiscountAmount** | **BigDecimal** | Shipping discount amount in quote currency |  [optional] |
|**shippingInclTax** | **BigDecimal** | Shipping including tax in quote currency |  [optional] |
|**shippingTaxAmount** | **BigDecimal** | Shipping tax amount in quote currency |  [optional] |
|**subtotal** | **BigDecimal** | Subtotal in quote currency |  [optional] |
|**subtotalInclTax** | **BigDecimal** | Subtotal including tax in quote currency |  [optional] |
|**subtotalWithDiscount** | **BigDecimal** | Subtotal in quote currency with applied discount |  [optional] |
|**taxAmount** | **BigDecimal** | Tax amount in quote currency |  [optional] |
|**totalSegments** | [**List&lt;QuoteDataTotalSegmentInterface&gt;**](QuoteDataTotalSegmentInterface.md) | Dynamically calculated totals |  |
|**weeeTaxAppliedAmount** | **BigDecimal** | Item weee tax applied amount in quote currency. |  |



