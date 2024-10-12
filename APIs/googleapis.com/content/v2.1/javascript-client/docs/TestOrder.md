# ContentApiForShopping.TestOrder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deliveryDetails** | [**TestOrderDeliveryDetails**](TestOrderDeliveryDetails.md) |  | [optional] 
**enableOrderinvoices** | **Boolean** | Whether the orderinvoices service should support this order. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#testOrder&#x60;\&quot; | [optional] 
**lineItems** | [**[TestOrderLineItem]**](TestOrderLineItem.md) | Required. Line items that are ordered. At least one line item must be provided. | [optional] 
**notificationMode** | **String** | Restricted. Do not use. | [optional] 
**pickupDetails** | [**TestOrderPickupDetails**](TestOrderPickupDetails.md) |  | [optional] 
**predefinedBillingAddress** | **String** | Required. The billing address. Acceptable values are: - \&quot;&#x60;dwight&#x60;\&quot; - \&quot;&#x60;jim&#x60;\&quot; - \&quot;&#x60;pam&#x60;\&quot;  | [optional] 
**predefinedDeliveryAddress** | **String** | Required. Identifier of one of the predefined delivery addresses for the delivery. Acceptable values are: - \&quot;&#x60;dwight&#x60;\&quot; - \&quot;&#x60;jim&#x60;\&quot; - \&quot;&#x60;pam&#x60;\&quot;  | [optional] 
**predefinedEmail** | **String** | Required. Email address of the customer. Acceptable values are: - \&quot;&#x60;pog.dwight.schrute@gmail.com&#x60;\&quot; - \&quot;&#x60;pog.jim.halpert@gmail.com&#x60;\&quot; - \&quot;&#x60;penpog.pam.beesly@gmail.comding&#x60;\&quot;  | [optional] 
**predefinedPickupDetails** | **String** | Identifier of one of the predefined pickup details. Required for orders containing line items with shipping type &#x60;pickup&#x60;. Acceptable values are: - \&quot;&#x60;dwight&#x60;\&quot; - \&quot;&#x60;jim&#x60;\&quot; - \&quot;&#x60;pam&#x60;\&quot;  | [optional] 
**promotions** | [**[OrderPromotion]**](OrderPromotion.md) | Promotions associated with the order. | [optional] 
**shippingCost** | [**Price**](Price.md) |  | [optional] 
**shippingOption** | **String** | Required. The requested shipping option. Acceptable values are: - \&quot;&#x60;economy&#x60;\&quot; - \&quot;&#x60;expedited&#x60;\&quot; - \&quot;&#x60;oneDay&#x60;\&quot; - \&quot;&#x60;sameDay&#x60;\&quot; - \&quot;&#x60;standard&#x60;\&quot; - \&quot;&#x60;twoDay&#x60;\&quot;  | [optional] 


