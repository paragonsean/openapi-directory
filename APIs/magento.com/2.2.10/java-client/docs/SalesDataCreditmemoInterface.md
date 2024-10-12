

# SalesDataCreditmemoInterface

Credit memo interface. After a customer places and pays for an order and an invoice has been issued, the merchant can create a credit memo to refund all or part of the amount paid for any returned or undelivered items. The memo restores funds to the customer account so that the customer can make future purchases.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adjustment** | **BigDecimal** | Credit memo adjustment. |  [optional] |
|**adjustmentNegative** | **BigDecimal** | Credit memo negative adjustment. |  [optional] |
|**adjustmentPositive** | **BigDecimal** | Credit memo positive adjustment. |  [optional] |
|**baseAdjustment** | **BigDecimal** | Credit memo base adjustment. |  [optional] |
|**baseAdjustmentNegative** | **BigDecimal** | Credit memo negative base adjustment. |  [optional] |
|**baseAdjustmentPositive** | **BigDecimal** | Credit memo positive base adjustment. |  [optional] |
|**baseCurrencyCode** | **String** | Credit memo base currency code. |  [optional] |
|**baseDiscountAmount** | **BigDecimal** | Credit memo base discount amount. |  [optional] |
|**baseDiscountTaxCompensationAmount** | **BigDecimal** | Credit memo base discount tax compensation amount. |  [optional] |
|**baseGrandTotal** | **BigDecimal** | Credit memo base grand total. |  [optional] |
|**baseShippingAmount** | **BigDecimal** | Credit memo base shipping amount. |  [optional] |
|**baseShippingDiscountTaxCompensationAmnt** | **BigDecimal** | Credit memo base shipping discount tax compensation amount. |  [optional] |
|**baseShippingInclTax** | **BigDecimal** | Credit memo base shipping including tax. |  [optional] |
|**baseShippingTaxAmount** | **BigDecimal** | Credit memo base shipping tax amount. |  [optional] |
|**baseSubtotal** | **BigDecimal** | Credit memo base subtotal. |  [optional] |
|**baseSubtotalInclTax** | **BigDecimal** | Credit memo base subtotal including tax. |  [optional] |
|**baseTaxAmount** | **BigDecimal** | Credit memo base tax amount. |  [optional] |
|**baseToGlobalRate** | **BigDecimal** | Credit memo base-to-global rate. |  [optional] |
|**baseToOrderRate** | **BigDecimal** | Credit memo base-to-order rate. |  [optional] |
|**billingAddressId** | **Integer** | Credit memo billing address ID. |  [optional] |
|**comments** | [**List&lt;SalesDataCreditmemoCommentInterface&gt;**](SalesDataCreditmemoCommentInterface.md) | Array of any credit memo comments. Otherwise, null. |  [optional] |
|**createdAt** | **String** | Credit memo created-at timestamp. |  [optional] |
|**creditmemoStatus** | **Integer** | Credit memo status. |  [optional] |
|**discountAmount** | **BigDecimal** | Credit memo discount amount. |  [optional] |
|**discountDescription** | **String** | Credit memo discount description. |  [optional] |
|**discountTaxCompensationAmount** | **BigDecimal** | Credit memo discount tax compensation amount. |  [optional] |
|**emailSent** | **Integer** | Credit memo email sent flag value. |  [optional] |
|**entityId** | **Integer** | Credit memo ID. |  [optional] |
|**extensionAttributes** | [**SalesDataCreditmemoExtensionInterface**](SalesDataCreditmemoExtensionInterface.md) |  |  [optional] |
|**globalCurrencyCode** | **String** | Credit memo global currency code. |  [optional] |
|**grandTotal** | **BigDecimal** | Credit memo grand total. |  [optional] |
|**incrementId** | **String** | Credit memo increment ID. |  [optional] |
|**invoiceId** | **Integer** | Credit memo invoice ID. |  [optional] |
|**items** | [**List&lt;SalesDataCreditmemoItemInterface&gt;**](SalesDataCreditmemoItemInterface.md) | Array of credit memo items. |  |
|**orderCurrencyCode** | **String** | Credit memo order currency code. |  [optional] |
|**orderId** | **Integer** | Credit memo order ID. |  |
|**shippingAddressId** | **Integer** | Credit memo shipping address ID. |  [optional] |
|**shippingAmount** | **BigDecimal** | Credit memo shipping amount. |  [optional] |
|**shippingDiscountTaxCompensationAmount** | **BigDecimal** | Credit memo shipping discount tax compensation amount. |  [optional] |
|**shippingInclTax** | **BigDecimal** | Credit memo shipping including tax. |  [optional] |
|**shippingTaxAmount** | **BigDecimal** | Credit memo shipping tax amount. |  [optional] |
|**state** | **Integer** | Credit memo state. |  [optional] |
|**storeCurrencyCode** | **String** | Credit memo store currency code. |  [optional] |
|**storeId** | **Integer** | Credit memo store ID. |  [optional] |
|**storeToBaseRate** | **BigDecimal** | Credit memo store-to-base rate. |  [optional] |
|**storeToOrderRate** | **BigDecimal** | Credit memo store-to-order rate. |  [optional] |
|**subtotal** | **BigDecimal** | Credit memo subtotal. |  [optional] |
|**subtotalInclTax** | **BigDecimal** | Credit memo subtotal including tax. |  [optional] |
|**taxAmount** | **BigDecimal** | Credit memo tax amount. |  [optional] |
|**transactionId** | **String** | Credit memo transaction ID. |  [optional] |
|**updatedAt** | **String** | Credit memo updated-at timestamp. |  [optional] |



