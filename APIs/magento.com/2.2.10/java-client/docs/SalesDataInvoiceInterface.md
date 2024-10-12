

# SalesDataInvoiceInterface

Invoice interface. An invoice is a record of the receipt of payment for an order.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseCurrencyCode** | **String** | Base currency code. |  [optional] |
|**baseDiscountAmount** | **BigDecimal** | Base discount amount. |  [optional] |
|**baseDiscountTaxCompensationAmount** | **BigDecimal** | Base discount tax compensation amount. |  [optional] |
|**baseGrandTotal** | **BigDecimal** | Base grand total. |  [optional] |
|**baseShippingAmount** | **BigDecimal** | Base shipping amount. |  [optional] |
|**baseShippingDiscountTaxCompensationAmnt** | **BigDecimal** | Base shipping discount tax compensation amount. |  [optional] |
|**baseShippingInclTax** | **BigDecimal** | Base shipping including tax. |  [optional] |
|**baseShippingTaxAmount** | **BigDecimal** | Base shipping tax amount. |  [optional] |
|**baseSubtotal** | **BigDecimal** | Base subtotal. |  [optional] |
|**baseSubtotalInclTax** | **BigDecimal** | Base subtotal including tax. |  [optional] |
|**baseTaxAmount** | **BigDecimal** | Base tax amount. |  [optional] |
|**baseToGlobalRate** | **BigDecimal** | Base-to-global rate. |  [optional] |
|**baseToOrderRate** | **BigDecimal** | Base-to-order rate. |  [optional] |
|**baseTotalRefunded** | **BigDecimal** | Base total refunded. |  [optional] |
|**billingAddressId** | **Integer** | Billing address ID. |  [optional] |
|**canVoidFlag** | **Integer** | Can void flag value. |  [optional] |
|**comments** | [**List&lt;SalesDataInvoiceCommentInterface&gt;**](SalesDataInvoiceCommentInterface.md) | Array of any invoice comments. Otherwise, null. |  [optional] |
|**createdAt** | **String** | Created-at timestamp. |  [optional] |
|**discountAmount** | **BigDecimal** | Discount amount. |  [optional] |
|**discountDescription** | **String** | Discount description. |  [optional] |
|**discountTaxCompensationAmount** | **BigDecimal** | Discount tax compensation amount. |  [optional] |
|**emailSent** | **Integer** | Email-sent flag value. |  [optional] |
|**entityId** | **Integer** | Invoice ID. |  [optional] |
|**extensionAttributes** | [**SalesDataInvoiceExtensionInterface**](SalesDataInvoiceExtensionInterface.md) |  |  [optional] |
|**globalCurrencyCode** | **String** | Global currency code. |  [optional] |
|**grandTotal** | **BigDecimal** | Grand total. |  [optional] |
|**incrementId** | **String** | Increment ID. |  [optional] |
|**isUsedForRefund** | **Integer** | Is-used-for-refund flag value. |  [optional] |
|**items** | [**List&lt;SalesDataInvoiceItemInterface&gt;**](SalesDataInvoiceItemInterface.md) | Array of invoice items. |  |
|**orderCurrencyCode** | **String** | Order currency code. |  [optional] |
|**orderId** | **Integer** | Order ID. |  |
|**shippingAddressId** | **Integer** | Shipping address ID. |  [optional] |
|**shippingAmount** | **BigDecimal** | Shipping amount. |  [optional] |
|**shippingDiscountTaxCompensationAmount** | **BigDecimal** | Shipping discount tax compensation amount. |  [optional] |
|**shippingInclTax** | **BigDecimal** | Shipping including tax. |  [optional] |
|**shippingTaxAmount** | **BigDecimal** | Shipping tax amount. |  [optional] |
|**state** | **Integer** | State. |  [optional] |
|**storeCurrencyCode** | **String** | Store currency code. |  [optional] |
|**storeId** | **Integer** | Store ID. |  [optional] |
|**storeToBaseRate** | **BigDecimal** | Store-to-base rate. |  [optional] |
|**storeToOrderRate** | **BigDecimal** | Store-to-order rate. |  [optional] |
|**subtotal** | **BigDecimal** | Subtotal. |  [optional] |
|**subtotalInclTax** | **BigDecimal** | Subtotal including tax. |  [optional] |
|**taxAmount** | **BigDecimal** | Tax amount. |  [optional] |
|**totalQty** | **BigDecimal** | Total quantity. |  |
|**transactionId** | **String** | Transaction ID. |  [optional] |
|**updatedAt** | **String** | Updated-at timestamp. |  [optional] |



