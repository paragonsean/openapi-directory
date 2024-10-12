# ContentApiForShopping.Order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledged** | **Boolean** | Whether the order was acknowledged. | [optional] 
**channelType** | **String** | Deprecated. Acceptable values are: - \&quot;&#x60;googleExpress&#x60;\&quot; - \&quot;&#x60;purchasesOnGoogle&#x60;\&quot;  | [optional] 
**customer** | [**OrderCustomer**](OrderCustomer.md) |  | [optional] 
**deliveryDetails** | [**OrderDeliveryDetails**](OrderDeliveryDetails.md) |  | [optional] 
**id** | **String** | The REST ID of the order. Globally unique. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#order&#x60;\&quot; | [optional] 
**lineItems** | [**[OrderLineItem]**](OrderLineItem.md) | Line items that are ordered. | [optional] 
**merchantId** | **String** |  | [optional] 
**merchantOrderId** | **String** | Merchant-provided ID of the order. | [optional] 
**netAmount** | [**Price**](Price.md) |  | [optional] 
**paymentMethod** | [**OrderPaymentMethod**](OrderPaymentMethod.md) |  | [optional] 
**paymentStatus** | **String** | The status of the payment. Acceptable values are: - \&quot;&#x60;paymentCaptured&#x60;\&quot; - \&quot;&#x60;paymentRejected&#x60;\&quot; - \&quot;&#x60;paymentSecured&#x60;\&quot; - \&quot;&#x60;pendingAuthorization&#x60;\&quot;  | [optional] 
**pickupDetails** | [**OrderPickupDetails**](OrderPickupDetails.md) |  | [optional] 
**placedDate** | **String** | The date when the order was placed, in ISO 8601 format. | [optional] 
**promotions** | [**[OrderLegacyPromotion]**](OrderLegacyPromotion.md) | The details of the merchant provided promotions applied to the order. To determine which promotions apply to which products, check the &#x60;Promotions[].Benefits[].OfferIds&#x60; field against the &#x60;LineItems[].Product.OfferId&#x60; field for each promotion. If a promotion is applied to more than 1 &#x60;offerId&#x60;, divide the discount value by the number of affected offers to determine how much discount to apply to each &#x60;offerId&#x60;. Examples: 1. To calculate the line item level discount for a single specific item: For each promotion, subtract the &#x60;Promotions[].Benefits[].Discount.value&#x60; amount from the &#x60;LineItems[].Price.value&#x60;. 2. To calculate the line item level discount for multiple quantity of a specific item: For each promotion, divide the &#x60;Promotions[].Benefits[].Discount.value&#x60; by the quantity of products and substract it from &#x60;LineItems[].Product.Price.value&#x60; for each quantity item. Only 1 promotion can be applied to an offerId in a given order. To refund an item which had a promotion applied to it, make sure to refund the amount after first subtracting the promotion discount from the item price. More details about the program are here. | [optional] 
**refunds** | [**[OrderRefund]**](OrderRefund.md) | Refunds for the order. | [optional] 
**shipments** | [**[OrderShipment]**](OrderShipment.md) | Shipments of the order. | [optional] 
**shippingCost** | [**Price**](Price.md) |  | [optional] 
**shippingCostTax** | [**Price**](Price.md) |  | [optional] 
**shippingOption** | **String** | Deprecated. Shipping details are provided with line items instead. Acceptable values are: - \&quot;&#x60;economy&#x60;\&quot; - \&quot;&#x60;expedited&#x60;\&quot; - \&quot;&#x60;oneDay&#x60;\&quot; - \&quot;&#x60;sameDay&#x60;\&quot; - \&quot;&#x60;standard&#x60;\&quot; - \&quot;&#x60;twoDay&#x60;\&quot;  | [optional] 
**status** | **String** | The status of the order. Acceptable values are: - \&quot;&#x60;canceled&#x60;\&quot; - \&quot;&#x60;delivered&#x60;\&quot; - \&quot;&#x60;inProgress&#x60;\&quot; - \&quot;&#x60;partiallyDelivered&#x60;\&quot; - \&quot;&#x60;partiallyReturned&#x60;\&quot; - \&quot;&#x60;partiallyShipped&#x60;\&quot; - \&quot;&#x60;pendingShipment&#x60;\&quot; - \&quot;&#x60;returned&#x60;\&quot; - \&quot;&#x60;shipped&#x60;\&quot;  | [optional] 
**taxCollector** | **String** | The party responsible for collecting and remitting taxes. Acceptable values are: - \&quot;&#x60;marketplaceFacilitator&#x60;\&quot; - \&quot;&#x60;merchant&#x60;\&quot;  | [optional] 


