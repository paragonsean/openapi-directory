# LogisticsApi.RequestBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**businessHourSettings** | [**BusinessHourSettings**](BusinessHourSettings.md) |  | 
**carrierSchedule** | [**[CarrierScheduleInner]**](CarrierScheduleInner.md) | Schedule sent by the carrier, to configure Shipping policy | [optional] 
**cubicWeightSettings** | [**CubicWeightSettings**](CubicWeightSettings.md) |  | 
**deliveryScheduleSettings** | [**DeliveryScheduleSettings**](DeliveryScheduleSettings.md) |  | 
**id** | **String** | ID of the shipping policy. | 
**isActive** | **Boolean** | Indicates whether shipping policy is active or not. | 
**maxDimension** | [**MaxDimension**](MaxDimension.md) |  | 
**maximumValueAceptable** | **Number** | Maximum value accepted by the carrier, to realize the shipping. | 
**minimumValueAceptable** | **Number** | Minimum value accepted by the carrier, to realize the shipping. | 
**modalSettings** | [**ModalSettings**](ModalSettings.md) |  | 
**name** | **String** | Name of the shipping policy. | 
**numberOfItemsPerShipment** | **Number** | Capacity of your store&#39;s logistics of shipment, determines number of items permitted per shipment. | 
**pickupPointsSettings** | [**PickupPointsSettings**](PickupPointsSettings.md) |  | 
**shippingMethod** | **String** | Type of shipping available for this shipping policy (carrier). Options shown on freight simulation | 
**weekendAndHolidays** | [**WeekendAndHolidays**](WeekendAndHolidays.md) |  | 


