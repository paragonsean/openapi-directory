# ConsumptionManagementClient.ReservationDetailsProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instanceId** | **String** | This identifier is the name of the resource or the fully qualified Resource ID. | [optional] [readonly] 
**reservationId** | **String** | The reservation ID is the identifier of a reservation within a reservation order. Each reservation is the grouping for applying the benefit scope and also specifies the number of instances to which the reservation benefit can be applied to. | [optional] [readonly] 
**reservationOrderId** | **String** | The reservation order ID is the identifier for a reservation purchase. Each reservation order ID represents a single purchase transaction. A reservation order contains reservations. The reservation order specifies the VM size and region for the reservations. | [optional] [readonly] 
**reservedHours** | **Number** | This is the total hours reserved for the day. E.g. if reservation for 1 instance was made on 1 PM, this will be 11 hours for that day and 24 hours from subsequent days. | [optional] [readonly] 
**skuName** | **String** | This is the ARM Sku name. It can be used to join with the serviceType field in additional info in usage records. | [optional] [readonly] 
**totalReservedQuantity** | **Number** | This is the total count of instances that are reserved for the reservationId. | [optional] [readonly] 
**usageDate** | **Date** | The date on which consumption occurred. | [optional] [readonly] 
**usedHours** | **Number** | This is the total hours used by the instance. | [optional] [readonly] 


