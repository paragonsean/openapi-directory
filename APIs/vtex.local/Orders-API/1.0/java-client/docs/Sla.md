

# Sla


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deliveryChannel** | **String** | If the delivery channel is &#x60;delivery&#x60; or &#x60;pickup-in-point&#x60;. |  |
|**deliveryWindow** | **String** | [Scheduled delivery window](https://help.vtex.com/tutorial/scheduled-delivery--22g3HAVCGLFiU7xugShOBi) information, if it applies to the item. |  |
|**id** | **String** | ID of the shipping method used in the [shipping policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140). |  |
|**lockTTL** | **String** | Logistics [reservation](https://help.vtex.com/en/tutorial/how-does-reservation-work--tutorials_92) waiting time of the SLA. |  |
|**name** | **String** | Name of the shipping policy. |  |
|**pickupDistance** | **BigDecimal** | Distance in kilometers between the pickup point and the customer&#39;s address. The distance is measured as a straight line. |  |
|**pickupPointId** | **String** | [Pickup point](https://help.vtex.com/en/tutorial/pickup-points--2fljn6wLjn8M4lJHA6HP3R) ID related to the SLA. |  |
|**pickupStoreInfo** | [**PickupStoreInfo**](PickupStoreInfo.md) |  |  |
|**polygonName** | **String** | Name of the [polygon](https://help.vtex.com/en/tutorial/registering-geolocation/) associated with the shipping policy. |  |
|**price** | **Integer** | Shipping price for the item in cents. Does not account for the whole order&#39;s shipping price. |  |
|**shippingEstimate** | **String** | Total shipping estimate time in days. For instance, three business days is represented &#x60;3bd&#x60;. |  |
|**transitTime** | **String** | Duration in business days of the time the carrier takes in transit to fulfill the order. For example, three business days is represented &#x60;3bd&#x60;. |  |



