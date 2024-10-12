# ConsumptionManagementClient.ReservationSummariesProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avgUtilizationPercentage** | **Number** | This is average utilization for the entire time range. (day or month depending on the grain) | [optional] [readonly] 
**maxUtilizationPercentage** | **Number** | This is the maximum hourly utilization in the usage time (day or month). E.g. if usage record corresponds to 12/10/2017 and on that for hour 4 and 5, utilization was 100%, this field will return 100% for that day. | [optional] [readonly] 
**minUtilizationPercentage** | **Number** | This is the minimum hourly utilization in the usage time (day or month). E.g. if usage record corresponds to 12/10/2017 and on that for hour 4 and 5, utilization was 10%, this field will return 10% for that day | [optional] [readonly] 
**reservationId** | **String** | The reservation ID is the identifier of a reservation within a reservation order. Each reservation is the grouping for applying the benefit scope and also specifies the number of instances to which the reservation benefit can be applied to. | [optional] [readonly] 
**reservationOrderId** | **String** | The reservation order ID is the identifier for a reservation purchase. Each reservation order ID represents a single purchase transaction. A reservation order contains reservations. The reservation order specifies the VM size and region for the reservations. | [optional] [readonly] 
**reservedHours** | **Number** | This is the total hours reserved. E.g. if reservation for 1 instance was made on 1 PM, this will be 11 hours for that day and 24 hours from subsequent days | [optional] [readonly] 
**skuName** | **String** | This is the ARM Sku name. It can be used to join with the serviceType field in additional info in usage records. | [optional] [readonly] 
**usageDate** | **Date** | Data corresponding to the utilization record. If the grain of data is monthly, it will be first day of month. | [optional] [readonly] 
**usedHours** | **Number** | Total used hours by the reservation | [optional] [readonly] 


