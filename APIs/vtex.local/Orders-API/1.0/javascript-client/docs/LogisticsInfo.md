# OrdersApi.LogisticsInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressId** | **String** | Address ID. | 
**deliveryChannel** | **String** | If the delivery channel is &#x60;delivery&#x60; or &#x60;pickup-in-point&#x60;. | 
**deliveryChannels** | [**[LogisticsInfoDeliveryChannelsInner]**](LogisticsInfoDeliveryChannelsInner.md) | List of delivery channels associated with the trade policy. | 
**deliveryCompany** | **String** | [Carrier](https://help.vtex.com/en/tutorial/transportadoras-na-vtex--7u9duMD5UQa2QQwukAWMcE) company&#39;s name. | 
**deliveryIds** | [**[DeliveryId]**](DeliveryId.md) | Information about delivery IDs. | 
**deliveryWindow** | **String** | [Scheduled delivery](https://help.vtex.com/tutorial/scheduled-delivery--22g3HAVCGLFiU7xugShOBi) window information, if it applies to the item. | 
**entityId** | **String** | Shipping address entity ID. | 
**itemIndex** | **Number** | Index of the item starting from 0. | 
**listPrice** | **Number** | SKU&#39;s optional price for a specific trade policy. | 
**lockTTL** | **String** | Logistics [reservation](https://help.vtex.com/en/tutorial/how-does-reservation-work--tutorials_92) waiting time. | 
**pickupPointId** | **String** | [Pickup point](https://help.vtex.com/en/tutorial/pickup-points--2fljn6wLjn8M4lJHA6HP3R)&#39;s ID. | 
**pickupStoreInfo** | [**PickupStoreInfo**](PickupStoreInfo.md) |  | 
**polygonName** | **String** | Name of the [polygon](https://help.vtex.com/en/tutorial/registering-geolocation/) associated with the shipping policy. | 
**price** | **Number** | Shipping price for the item in cents. Does not account for the whole order&#39;s shipping price. | 
**selectedSla** | **String** | Selected shipping option. | 
**sellingPrice** | **Number** | Item&#39;s selling price. | 
**shippingEstimate** | **String** | Total shipping estimate time in days. For instance, three business days is represented &#x60;3bd&#x60;. | 
**shippingEstimateDate** | **String** | Shipping estimate date. It is defined only after the confirmation of the order. | 
**shipsTo** | **[String]** | Three letters ISO code of the country of the shipping address (ISO 3166 ALPHA-3). | 
**slas** | [**[Sla]**](Sla.md) | Information on Service Level Agreement (SLA), corresponding to [shipping policies](https://help.vtex.com/tutorial/shipping-policy--tutorials_140). | 
**transitTime** | **String** | Duration in business days of the time the carrier takes in transit to fulfill the order. For example, three business days is represented &#x60;3bd&#x60;. | 
**versionId** | **String** | Shipping address version ID. | 


