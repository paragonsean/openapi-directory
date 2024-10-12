

# SalesDataOrderItemInterface

Order item interface. An order is a document that a web store issues to a customer. Magento generates a sales order that lists the product items, billing and shipping addresses, and shipping and payment methods. A corresponding external document, known as a purchase order, is emailed to the customer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalData** | **String** | Additional data. |  [optional] |
|**amountRefunded** | **BigDecimal** | Amount refunded. |  [optional] |
|**appliedRuleIds** | **String** | Applied rule IDs. |  [optional] |
|**baseAmountRefunded** | **BigDecimal** | Base amount refunded. |  [optional] |
|**baseCost** | **BigDecimal** | Base cost. |  [optional] |
|**baseDiscountAmount** | **BigDecimal** | Base discount amount. |  [optional] |
|**baseDiscountInvoiced** | **BigDecimal** | Base discount invoiced. |  [optional] |
|**baseDiscountRefunded** | **BigDecimal** | Base discount refunded. |  [optional] |
|**baseDiscountTaxCompensationAmount** | **BigDecimal** | Base discount tax compensation amount. |  [optional] |
|**baseDiscountTaxCompensationInvoiced** | **BigDecimal** | Base discount tax compensation invoiced. |  [optional] |
|**baseDiscountTaxCompensationRefunded** | **BigDecimal** | Base discount tax compensation refunded. |  [optional] |
|**baseOriginalPrice** | **BigDecimal** | Base original price. |  [optional] |
|**basePrice** | **BigDecimal** | Base price. |  [optional] |
|**basePriceInclTax** | **BigDecimal** | Base price including tax. |  [optional] |
|**baseRowInvoiced** | **BigDecimal** | Base row invoiced. |  [optional] |
|**baseRowTotal** | **BigDecimal** | Base row total. |  [optional] |
|**baseRowTotalInclTax** | **BigDecimal** | Base row total including tax. |  [optional] |
|**baseTaxAmount** | **BigDecimal** | Base tax amount. |  [optional] |
|**baseTaxBeforeDiscount** | **BigDecimal** | Base tax before discount. |  [optional] |
|**baseTaxInvoiced** | **BigDecimal** | Base tax invoiced. |  [optional] |
|**baseTaxRefunded** | **BigDecimal** | Base tax refunded. |  [optional] |
|**baseWeeeTaxAppliedAmount** | **BigDecimal** | Base WEEE tax applied amount. |  [optional] |
|**baseWeeeTaxAppliedRowAmnt** | **BigDecimal** | Base WEEE tax applied row amount. |  [optional] |
|**baseWeeeTaxDisposition** | **BigDecimal** | Base WEEE tax disposition. |  [optional] |
|**baseWeeeTaxRowDisposition** | **BigDecimal** | Base WEEE tax row disposition. |  [optional] |
|**createdAt** | **String** | Created-at timestamp. |  [optional] |
|**description** | **String** | Description. |  [optional] |
|**discountAmount** | **BigDecimal** | Discount amount. |  [optional] |
|**discountInvoiced** | **BigDecimal** | Discount invoiced. |  [optional] |
|**discountPercent** | **BigDecimal** | Discount percent. |  [optional] |
|**discountRefunded** | **BigDecimal** | Discount refunded. |  [optional] |
|**discountTaxCompensationAmount** | **BigDecimal** | Discount tax compensation amount. |  [optional] |
|**discountTaxCompensationCanceled** | **BigDecimal** | Discount tax compensation canceled. |  [optional] |
|**discountTaxCompensationInvoiced** | **BigDecimal** | Discount tax compensation invoiced. |  [optional] |
|**discountTaxCompensationRefunded** | **BigDecimal** | Discount tax compensation refunded. |  [optional] |
|**eventId** | **Integer** | Event ID. |  [optional] |
|**extOrderItemId** | **String** | External order item ID. |  [optional] |
|**extensionAttributes** | [**SalesDataOrderItemExtensionInterface**](SalesDataOrderItemExtensionInterface.md) |  |  [optional] |
|**freeShipping** | **Integer** | Free-shipping flag value. |  [optional] |
|**gwBasePrice** | **BigDecimal** | GW base price. |  [optional] |
|**gwBasePriceInvoiced** | **BigDecimal** | GW base price invoiced. |  [optional] |
|**gwBasePriceRefunded** | **BigDecimal** | GW base price refunded. |  [optional] |
|**gwBaseTaxAmount** | **BigDecimal** | GW base tax amount. |  [optional] |
|**gwBaseTaxAmountInvoiced** | **BigDecimal** | GW base tax amount invoiced. |  [optional] |
|**gwBaseTaxAmountRefunded** | **BigDecimal** | GW base tax amount refunded. |  [optional] |
|**gwId** | **Integer** | GW ID. |  [optional] |
|**gwPrice** | **BigDecimal** | GW price. |  [optional] |
|**gwPriceInvoiced** | **BigDecimal** | GW price invoiced. |  [optional] |
|**gwPriceRefunded** | **BigDecimal** | GW price refunded. |  [optional] |
|**gwTaxAmount** | **BigDecimal** | GW tax amount. |  [optional] |
|**gwTaxAmountInvoiced** | **BigDecimal** | GW tax amount invoiced. |  [optional] |
|**gwTaxAmountRefunded** | **BigDecimal** | GW tax amount refunded. |  [optional] |
|**isQtyDecimal** | **Integer** | Is-quantity-decimal flag value. |  [optional] |
|**isVirtual** | **Integer** | Is-virtual flag value. |  [optional] |
|**itemId** | **Integer** | Item ID. |  [optional] |
|**lockedDoInvoice** | **Integer** | Locked DO invoice flag value. |  [optional] |
|**lockedDoShip** | **Integer** | Locked DO ship flag value. |  [optional] |
|**name** | **String** | Name. |  [optional] |
|**noDiscount** | **Integer** | No-discount flag value. |  [optional] |
|**orderId** | **Integer** | Order ID. |  [optional] |
|**originalPrice** | **BigDecimal** | Original price. |  [optional] |
|**parentItem** | [**SalesDataOrderItemInterface**](SalesDataOrderItemInterface.md) |  |  [optional] |
|**parentItemId** | **Integer** | Parent item ID. |  [optional] |
|**price** | **BigDecimal** | Price. |  [optional] |
|**priceInclTax** | **BigDecimal** | Price including tax. |  [optional] |
|**productId** | **Integer** | Product ID. |  [optional] |
|**productOption** | [**CatalogDataProductOptionInterface**](CatalogDataProductOptionInterface.md) |  |  [optional] |
|**productType** | **String** | Product type. |  [optional] |
|**qtyBackordered** | **BigDecimal** | Quantity backordered. |  [optional] |
|**qtyCanceled** | **BigDecimal** | Quantity canceled. |  [optional] |
|**qtyInvoiced** | **BigDecimal** | Quantity invoiced. |  [optional] |
|**qtyOrdered** | **BigDecimal** | Quantity ordered. |  [optional] |
|**qtyRefunded** | **BigDecimal** | Quantity refunded. |  [optional] |
|**qtyReturned** | **BigDecimal** | Quantity returned. |  [optional] |
|**qtyShipped** | **BigDecimal** | Quantity shipped. |  [optional] |
|**quoteItemId** | **Integer** | Quote item ID. |  [optional] |
|**rowInvoiced** | **BigDecimal** | Row invoiced. |  [optional] |
|**rowTotal** | **BigDecimal** | Row total. |  [optional] |
|**rowTotalInclTax** | **BigDecimal** | Row total including tax. |  [optional] |
|**rowWeight** | **BigDecimal** | Row weight. |  [optional] |
|**sku** | **String** | SKU. |  |
|**storeId** | **Integer** | Store ID. |  [optional] |
|**taxAmount** | **BigDecimal** | Tax amount. |  [optional] |
|**taxBeforeDiscount** | **BigDecimal** | Tax before discount. |  [optional] |
|**taxCanceled** | **BigDecimal** | Tax canceled. |  [optional] |
|**taxInvoiced** | **BigDecimal** | Tax invoiced. |  [optional] |
|**taxPercent** | **BigDecimal** | Tax percent. |  [optional] |
|**taxRefunded** | **BigDecimal** | Tax refunded. |  [optional] |
|**updatedAt** | **String** | Updated-at timestamp. |  [optional] |
|**weeeTaxApplied** | **String** | WEEE tax applied. |  [optional] |
|**weeeTaxAppliedAmount** | **BigDecimal** | WEEE tax applied amount. |  [optional] |
|**weeeTaxAppliedRowAmount** | **BigDecimal** | WEEE tax applied row amount. |  [optional] |
|**weeeTaxDisposition** | **BigDecimal** | WEEE tax disposition. |  [optional] |
|**weeeTaxRowDisposition** | **BigDecimal** | WEEE tax row disposition. |  [optional] |
|**weight** | **BigDecimal** | Weight. |  [optional] |



