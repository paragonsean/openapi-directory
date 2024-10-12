

# SalesDataOrderInterface

Order interface. An order is a document that a web store issues to a customer. Magento generates a sales order that lists the product items, billing and shipping addresses, and shipping and payment methods. A corresponding external document, known as a purchase order, is emailed to the customer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adjustmentNegative** | **BigDecimal** | Negative adjustment value. |  [optional] |
|**adjustmentPositive** | **BigDecimal** | Positive adjustment value. |  [optional] |
|**appliedRuleIds** | **String** | Applied rule IDs. |  [optional] |
|**baseAdjustmentNegative** | **BigDecimal** | Base negative adjustment value. |  [optional] |
|**baseAdjustmentPositive** | **BigDecimal** | Base positive adjustment value. |  [optional] |
|**baseCurrencyCode** | **String** | Base currency code. |  [optional] |
|**baseDiscountAmount** | **BigDecimal** | Base discount amount. |  [optional] |
|**baseDiscountCanceled** | **BigDecimal** | Base discount canceled. |  [optional] |
|**baseDiscountInvoiced** | **BigDecimal** | Base discount invoiced. |  [optional] |
|**baseDiscountRefunded** | **BigDecimal** | Base discount refunded. |  [optional] |
|**baseDiscountTaxCompensationAmount** | **BigDecimal** | Base discount tax compensation amount. |  [optional] |
|**baseDiscountTaxCompensationInvoiced** | **BigDecimal** | Base discount tax compensation invoiced. |  [optional] |
|**baseDiscountTaxCompensationRefunded** | **BigDecimal** | Base discount tax compensation refunded. |  [optional] |
|**baseGrandTotal** | **BigDecimal** | Base grand total. |  |
|**baseShippingAmount** | **BigDecimal** | Base shipping amount. |  [optional] |
|**baseShippingCanceled** | **BigDecimal** | Base shipping canceled. |  [optional] |
|**baseShippingDiscountAmount** | **BigDecimal** | Base shipping discount amount. |  [optional] |
|**baseShippingDiscountTaxCompensationAmnt** | **BigDecimal** | Base shipping discount tax compensation amount. |  [optional] |
|**baseShippingInclTax** | **BigDecimal** | Base shipping including tax. |  [optional] |
|**baseShippingInvoiced** | **BigDecimal** | Base shipping invoiced. |  [optional] |
|**baseShippingRefunded** | **BigDecimal** | Base shipping refunded. |  [optional] |
|**baseShippingTaxAmount** | **BigDecimal** | Base shipping tax amount. |  [optional] |
|**baseShippingTaxRefunded** | **BigDecimal** | Base shipping tax refunded. |  [optional] |
|**baseSubtotal** | **BigDecimal** | Base subtotal. |  [optional] |
|**baseSubtotalCanceled** | **BigDecimal** | Base subtotal canceled. |  [optional] |
|**baseSubtotalInclTax** | **BigDecimal** | Base subtotal including tax. |  [optional] |
|**baseSubtotalInvoiced** | **BigDecimal** | Base subtotal invoiced. |  [optional] |
|**baseSubtotalRefunded** | **BigDecimal** | Base subtotal refunded. |  [optional] |
|**baseTaxAmount** | **BigDecimal** | Base tax amount. |  [optional] |
|**baseTaxCanceled** | **BigDecimal** | Base tax canceled. |  [optional] |
|**baseTaxInvoiced** | **BigDecimal** | Base tax invoiced. |  [optional] |
|**baseTaxRefunded** | **BigDecimal** | Base tax refunded. |  [optional] |
|**baseToGlobalRate** | **BigDecimal** | Base-to-global rate. |  [optional] |
|**baseToOrderRate** | **BigDecimal** | Base-to-order rate. |  [optional] |
|**baseTotalCanceled** | **BigDecimal** | Base total canceled. |  [optional] |
|**baseTotalDue** | **BigDecimal** | Base total due. |  [optional] |
|**baseTotalInvoiced** | **BigDecimal** | Base total invoiced. |  [optional] |
|**baseTotalInvoicedCost** | **BigDecimal** | Base total invoiced cost. |  [optional] |
|**baseTotalOfflineRefunded** | **BigDecimal** | Base total offline refunded. |  [optional] |
|**baseTotalOnlineRefunded** | **BigDecimal** | Base total online refunded. |  [optional] |
|**baseTotalPaid** | **BigDecimal** | Base total paid. |  [optional] |
|**baseTotalQtyOrdered** | **BigDecimal** | Base total quantity ordered. |  [optional] |
|**baseTotalRefunded** | **BigDecimal** | Base total refunded. |  [optional] |
|**billingAddress** | [**SalesDataOrderAddressInterface**](SalesDataOrderAddressInterface.md) |  |  [optional] |
|**billingAddressId** | **Integer** | Billing address ID. |  [optional] |
|**canShipPartially** | **Integer** | Can-ship-partially flag value. |  [optional] |
|**canShipPartiallyItem** | **Integer** | Can-ship-partially-item flag value. |  [optional] |
|**couponCode** | **String** | Coupon code. |  [optional] |
|**createdAt** | **String** | Created-at timestamp. |  [optional] |
|**customerDob** | **String** | Customer date-of-birth (DOB). |  [optional] |
|**customerEmail** | **String** | Customer email address. |  |
|**customerFirstname** | **String** | Customer first name. |  [optional] |
|**customerGender** | **Integer** | Customer gender. |  [optional] |
|**customerGroupId** | **Integer** | Customer group ID. |  [optional] |
|**customerId** | **Integer** | Customer ID. |  [optional] |
|**customerIsGuest** | **Integer** | Customer-is-guest flag value. |  [optional] |
|**customerLastname** | **String** | Customer last name. |  [optional] |
|**customerMiddlename** | **String** | Customer middle name. |  [optional] |
|**customerNote** | **String** | Customer note. |  [optional] |
|**customerNoteNotify** | **Integer** | Customer-note-notify flag value. |  [optional] |
|**customerPrefix** | **String** | Customer prefix. |  [optional] |
|**customerSuffix** | **String** | Customer suffix. |  [optional] |
|**customerTaxvat** | **String** | Customer value-added tax (VAT). |  [optional] |
|**discountAmount** | **BigDecimal** | Discount amount. |  [optional] |
|**discountCanceled** | **BigDecimal** | Discount canceled. |  [optional] |
|**discountDescription** | **String** | Discount description. |  [optional] |
|**discountInvoiced** | **BigDecimal** | Discount invoiced. |  [optional] |
|**discountRefunded** | **BigDecimal** | Discount refunded amount. |  [optional] |
|**discountTaxCompensationAmount** | **BigDecimal** | Discount tax compensation amount. |  [optional] |
|**discountTaxCompensationInvoiced** | **BigDecimal** | Discount tax compensation invoiced amount. |  [optional] |
|**discountTaxCompensationRefunded** | **BigDecimal** | Discount tax compensation refunded amount. |  [optional] |
|**editIncrement** | **Integer** | Edit increment value. |  [optional] |
|**emailSent** | **Integer** | Email-sent flag value. |  [optional] |
|**entityId** | **Integer** | Order ID. |  [optional] |
|**extCustomerId** | **String** | External customer ID. |  [optional] |
|**extOrderId** | **String** | External order ID. |  [optional] |
|**extensionAttributes** | [**SalesDataOrderExtensionInterface**](SalesDataOrderExtensionInterface.md) |  |  [optional] |
|**forcedShipmentWithInvoice** | **Integer** | Forced-shipment-with-invoice flag value. |  [optional] |
|**globalCurrencyCode** | **String** | Global currency code. |  [optional] |
|**grandTotal** | **BigDecimal** | Grand total. |  |
|**holdBeforeState** | **String** | Hold before state. |  [optional] |
|**holdBeforeStatus** | **String** | Hold before status. |  [optional] |
|**incrementId** | **String** | Increment ID. |  [optional] |
|**isVirtual** | **Integer** | Is-virtual flag value. |  [optional] |
|**items** | [**List&lt;SalesDataOrderItemInterface&gt;**](SalesDataOrderItemInterface.md) | Array of items. |  |
|**orderCurrencyCode** | **String** | Order currency code. |  [optional] |
|**originalIncrementId** | **String** | Original increment ID. |  [optional] |
|**payment** | [**SalesDataOrderPaymentInterface**](SalesDataOrderPaymentInterface.md) |  |  [optional] |
|**paymentAuthExpiration** | **Integer** | Payment authorization expiration date. |  [optional] |
|**paymentAuthorizationAmount** | **BigDecimal** | Payment authorization amount. |  [optional] |
|**protectCode** | **String** | Protect code. |  [optional] |
|**quoteAddressId** | **Integer** | Quote address ID. |  [optional] |
|**quoteId** | **Integer** | Quote ID. |  [optional] |
|**relationChildId** | **String** | Relation child ID. |  [optional] |
|**relationChildRealId** | **String** | Relation child real ID. |  [optional] |
|**relationParentId** | **String** | Relation parent ID. |  [optional] |
|**relationParentRealId** | **String** | Relation parent real ID. |  [optional] |
|**remoteIp** | **String** | Remote IP address. |  [optional] |
|**shippingAmount** | **BigDecimal** | Shipping amount. |  [optional] |
|**shippingCanceled** | **BigDecimal** | Shipping canceled amount. |  [optional] |
|**shippingDescription** | **String** | Shipping description. |  [optional] |
|**shippingDiscountAmount** | **BigDecimal** | Shipping discount amount. |  [optional] |
|**shippingDiscountTaxCompensationAmount** | **BigDecimal** | Shipping discount tax compensation amount. |  [optional] |
|**shippingInclTax** | **BigDecimal** | Shipping including tax amount. |  [optional] |
|**shippingInvoiced** | **BigDecimal** | Shipping invoiced amount. |  [optional] |
|**shippingRefunded** | **BigDecimal** | Shipping refunded amount. |  [optional] |
|**shippingTaxAmount** | **BigDecimal** | Shipping tax amount. |  [optional] |
|**shippingTaxRefunded** | **BigDecimal** | Shipping tax refunded amount. |  [optional] |
|**state** | **String** | State. |  [optional] |
|**status** | **String** | Status. |  [optional] |
|**statusHistories** | [**List&lt;SalesDataOrderStatusHistoryInterface&gt;**](SalesDataOrderStatusHistoryInterface.md) | Array of status histories. |  [optional] |
|**storeCurrencyCode** | **String** | Store currency code. |  [optional] |
|**storeId** | **Integer** | Store ID. |  [optional] |
|**storeName** | **String** | Store name. |  [optional] |
|**storeToBaseRate** | **BigDecimal** | Store-to-base rate. |  [optional] |
|**storeToOrderRate** | **BigDecimal** | Store-to-order rate. |  [optional] |
|**subtotal** | **BigDecimal** | Subtotal. |  [optional] |
|**subtotalCanceled** | **BigDecimal** | Subtotal canceled amount. |  [optional] |
|**subtotalInclTax** | **BigDecimal** | Subtotal including tax amount. |  [optional] |
|**subtotalInvoiced** | **BigDecimal** | Subtotal invoiced amount. |  [optional] |
|**subtotalRefunded** | **BigDecimal** | Subtotal refunded amount. |  [optional] |
|**taxAmount** | **BigDecimal** | Tax amount. |  [optional] |
|**taxCanceled** | **BigDecimal** | Tax canceled amount. |  [optional] |
|**taxInvoiced** | **BigDecimal** | Tax invoiced amount. |  [optional] |
|**taxRefunded** | **BigDecimal** | Tax refunded amount. |  [optional] |
|**totalCanceled** | **BigDecimal** | Total canceled. |  [optional] |
|**totalDue** | **BigDecimal** | Total due. |  [optional] |
|**totalInvoiced** | **BigDecimal** | Total invoiced amount. |  [optional] |
|**totalItemCount** | **Integer** | Total item count. |  [optional] |
|**totalOfflineRefunded** | **BigDecimal** | Total offline refunded amount. |  [optional] |
|**totalOnlineRefunded** | **BigDecimal** | Total online refunded amount. |  [optional] |
|**totalPaid** | **BigDecimal** | Total paid. |  [optional] |
|**totalQtyOrdered** | **BigDecimal** | Total quantity ordered. |  [optional] |
|**totalRefunded** | **BigDecimal** | Total amount refunded. |  [optional] |
|**updatedAt** | **String** | Updated-at timestamp. |  [optional] |
|**weight** | **BigDecimal** | Weight. |  [optional] |
|**xForwardedFor** | **String** | X-Forwarded-For field value. |  [optional] |



