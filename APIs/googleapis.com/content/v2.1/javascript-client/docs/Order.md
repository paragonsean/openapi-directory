# ContentApiForShopping.Order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledged** | **Boolean** | Whether the order was acknowledged. | [optional] 
**annotations** | [**[OrderOrderAnnotation]**](OrderOrderAnnotation.md) | List of key-value pairs that are attached to a given order. | [optional] 
**billingAddress** | [**OrderAddress**](OrderAddress.md) |  | [optional] 
**customer** | [**OrderCustomer**](OrderCustomer.md) |  | [optional] 
**deliveryDetails** | [**OrderDeliveryDetails**](OrderDeliveryDetails.md) |  | [optional] 
**id** | **String** | The REST ID of the order. Globally unique. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#order&#x60;\&quot; | [optional] 
**lineItems** | [**[OrderLineItem]**](OrderLineItem.md) | Line items that are ordered. | [optional] 
**merchantId** | **String** |  | [optional] 
**merchantOrderId** | **String** | Merchant-provided ID of the order. | [optional] 
**netPriceAmount** | [**Price**](Price.md) |  | [optional] 
**netTaxAmount** | [**Price**](Price.md) |  | [optional] 
**paymentStatus** | **String** | The status of the payment. Acceptable values are: - \&quot;&#x60;paymentCaptured&#x60;\&quot; - \&quot;&#x60;paymentRejected&#x60;\&quot; - \&quot;&#x60;paymentSecured&#x60;\&quot; - \&quot;&#x60;pendingAuthorization&#x60;\&quot;  | [optional] 
**pickupDetails** | [**OrderPickupDetails**](OrderPickupDetails.md) |  | [optional] 
**placedDate** | **String** | The date when the order was placed, in ISO 8601 format. | [optional] 
**promotions** | [**[OrderPromotion]**](OrderPromotion.md) | Promotions associated with the order. To determine which promotions apply to which products, check the &#x60;Promotions[].appliedItems[].lineItemId&#x60; field against the &#x60;LineItems[].id&#x60; field for each promotion. If a promotion is applied to more than 1 offerId, divide the discount value by the number of affected offers to determine how much discount to apply to each offerId. Examples: 1. To calculate price paid by the customer for a single line item including the discount: For each promotion, subtract the &#x60;LineItems[].adjustments[].priceAdjustment.value&#x60; amount from the &#x60;LineItems[].Price.value&#x60;. 2. To calculate price paid by the customer for a single line item including the discount in case of multiple quantity: For each promotion, divide the &#x60;LineItems[].adjustments[].priceAdjustment.value&#x60; by the quantity of products then subtract the resulting value from the &#x60;LineItems[].Product.Price.value&#x60; for each quantity item. Only 1 promotion can be applied to an offerId in a given order. To refund an item which had a promotion applied to it, make sure to refund the amount after first subtracting the promotion discount from the item price. More details about the program are here. | [optional] 
**refunds** | [**[OrderRefund]**](OrderRefund.md) | Refunds for the order. | [optional] 
**shipments** | [**[OrderShipment]**](OrderShipment.md) | Shipments of the order. | [optional] 
**shippingCost** | [**Price**](Price.md) |  | [optional] 
**shippingCostTax** | [**Price**](Price.md) |  | [optional] 
**status** | **String** | The status of the order. Acceptable values are: - \&quot;&#x60;canceled&#x60;\&quot; - \&quot;&#x60;delivered&#x60;\&quot; - \&quot;&#x60;inProgress&#x60;\&quot; - \&quot;&#x60;partiallyDelivered&#x60;\&quot; - \&quot;&#x60;partiallyReturned&#x60;\&quot; - \&quot;&#x60;partiallyShipped&#x60;\&quot; - \&quot;&#x60;pendingShipment&#x60;\&quot; - \&quot;&#x60;returned&#x60;\&quot; - \&quot;&#x60;shipped&#x60;\&quot;  | [optional] 
**taxCollector** | **String** | The party responsible for collecting and remitting taxes. Acceptable values are: - \&quot;&#x60;marketplaceFacilitator&#x60;\&quot; - \&quot;&#x60;merchant&#x60;\&quot;  | [optional] 


