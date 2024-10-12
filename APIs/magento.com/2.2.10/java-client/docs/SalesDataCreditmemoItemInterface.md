

# SalesDataCreditmemoItemInterface

Credit memo item interface. After a customer places and pays for an order and an invoice has been issued, the merchant can create a credit memo to refund all or part of the amount paid for any returned or undelivered items. The memo restores funds to the customer account so that the customer can make future purchases. A credit memo item is an invoiced item for which a merchant creates a credit memo.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalData** | **String** | Additional data. |  [optional] |
|**baseCost** | **BigDecimal** | The base cost for a credit memo item. |  |
|**baseDiscountAmount** | **BigDecimal** | The base discount amount for a credit memo item. |  [optional] |
|**baseDiscountTaxCompensationAmount** | **BigDecimal** | The base discount tax compensation amount for a credit memo item. |  [optional] |
|**basePrice** | **BigDecimal** | The base price for a credit memo item. |  |
|**basePriceInclTax** | **BigDecimal** | Base price including tax. |  [optional] |
|**baseRowTotal** | **BigDecimal** | Base row total. |  [optional] |
|**baseRowTotalInclTax** | **BigDecimal** | Base row total including tax. |  [optional] |
|**baseTaxAmount** | **BigDecimal** | Base tax amount. |  [optional] |
|**baseWeeeTaxAppliedAmount** | **BigDecimal** | Base WEEE tax applied amount. |  [optional] |
|**baseWeeeTaxAppliedRowAmnt** | **BigDecimal** | Base WEEE tax applied row amount. |  [optional] |
|**baseWeeeTaxDisposition** | **BigDecimal** | Base WEEE tax disposition. |  [optional] |
|**baseWeeeTaxRowDisposition** | **BigDecimal** | Base WEEE tax row disposition. |  [optional] |
|**description** | **String** | Description. |  [optional] |
|**discountAmount** | **BigDecimal** | Discount amount. |  [optional] |
|**discountTaxCompensationAmount** | **BigDecimal** | Discount tax compensation amount. |  [optional] |
|**entityId** | **Integer** | Credit memo item ID. |  |
|**extensionAttributes** | [**SalesDataCreditmemoItemExtensionInterface**](SalesDataCreditmemoItemExtensionInterface.md) |  |  [optional] |
|**name** | **String** | Name. |  [optional] |
|**orderItemId** | **Integer** | Order item ID. |  |
|**parentId** | **Integer** | Parent ID. |  [optional] |
|**price** | **BigDecimal** | Price. |  [optional] |
|**priceInclTax** | **BigDecimal** | Price including tax. |  [optional] |
|**productId** | **Integer** | Product ID. |  [optional] |
|**qty** | **BigDecimal** | Quantity. |  |
|**rowTotal** | **BigDecimal** | Row total. |  [optional] |
|**rowTotalInclTax** | **BigDecimal** | Row total including tax. |  [optional] |
|**sku** | **String** | SKU. |  [optional] |
|**taxAmount** | **BigDecimal** | Tax amount. |  [optional] |
|**weeeTaxApplied** | **String** | WEEE tax applied. |  [optional] |
|**weeeTaxAppliedAmount** | **BigDecimal** | WEEE tax applied amount. |  [optional] |
|**weeeTaxAppliedRowAmount** | **BigDecimal** | WEEE tax applied row amount. |  [optional] |
|**weeeTaxDisposition** | **BigDecimal** | WEEE tax disposition. |  [optional] |
|**weeeTaxRowDisposition** | **BigDecimal** | WEEE tax row disposition. |  [optional] |



