# OrdersApiPiiVersion.LogisticsInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressId** | **String** | Address ID. | 
**deliveryChannel** | **String** | Delivery channel. | 
**deliveryCompany** | **String** | Delivery company. | 
**deliveryIds** | [**[DeliveryId]**](DeliveryId.md) | Array of delivery IDs. | 
**deliveryWindow** | **String** | Delivery window information. | 
**itemIndex** | **Number** | Item index, matching the index in the &#x60;items&#x60; array. | 
**listPrice** | **Number** | List price in cents. | 
**lockTTL** | **String** | Reservation lasting period. | 
**pickupStoreInfo** | [**PickupStoreInfo**](PickupStoreInfo.md) |  | 
**polygonName** | **String** | Polygon name. | 
**price** | **Number** | Prince in cents. | 
**selectedSla** | **String** | Selected SLA. | 
**sellingPrice** | **Number** | Selling price in cents. | 
**shippingEstimate** | **String** | Shipping estimate. | 
**shippingEstimateDate** | **String** | Shipping estimate date. | 
**shipsTo** | **[String]** | List of countries (three letter ISO code) to which shipping is available. | 
**slas** | [**[Sla]**](Sla.md) | Array with information on the SLAs. | 


