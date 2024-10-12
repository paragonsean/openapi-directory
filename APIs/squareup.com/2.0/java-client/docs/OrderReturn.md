

# OrderReturn

The set of line items, service charges, taxes, discounts, tips, and other items being returned in an order.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**returnAmounts** | [**OrderMoneyAmounts**](OrderMoneyAmounts.md) |  |  [optional] |
|**returnDiscounts** | [**List&lt;OrderReturnDiscount&gt;**](OrderReturnDiscount.md) | A collection of references to discounts being returned for an order, including the total applied discount amount to be returned. The discounts must reference a top-level discount ID from the source order. |  [optional] |
|**returnLineItems** | [**List&lt;OrderReturnLineItem&gt;**](OrderReturnLineItem.md) | A collection of line items that are being returned. |  [optional] |
|**returnServiceCharges** | [**List&lt;OrderReturnServiceCharge&gt;**](OrderReturnServiceCharge.md) | A collection of service charges that are being returned. |  [optional] |
|**returnTaxes** | [**List&lt;OrderReturnTax&gt;**](OrderReturnTax.md) | A collection of references to taxes being returned for an order, including the total applied tax amount to be returned. The taxes must reference a top-level tax ID from the source order. |  [optional] |
|**roundingAdjustment** | [**OrderRoundingAdjustment**](OrderRoundingAdjustment.md) |  |  [optional] |
|**sourceOrderId** | **String** | An order that contains the original sale of these return line items. This is unset for unlinked returns. |  [optional] |
|**uid** | **String** | A unique ID that identifies the return only within this order. |  [optional] |



