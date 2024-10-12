# ConsumptionManagementClient.ReservationTransactionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountName** | **String** | The name of the account that makes the transaction. | [optional] [readonly] 
**accountOwnerEmail** | **String** | The email of the account owner that makes the transaction. | [optional] [readonly] 
**amount** | **Number** | The charge of the transaction. | [optional] [readonly] 
**armSkuName** | **String** | This is the ARM Sku name. It can be used to join with the serviceType field in additional info in usage records. | [optional] [readonly] 
**billingFrequency** | **String** | The billing frequency, which can be either one-time or recurring. | [optional] [readonly] 
**costCenter** | **String** | The cost center of this department if it is a department and a cost center is provided. | [optional] [readonly] 
**currency** | **String** | The ISO currency in which the transaction is charged, for example, USD. | [optional] [readonly] 
**currentEnrollment** | **String** | The current enrollment. | [optional] [readonly] 
**departmentName** | **String** | The department name. | [optional] [readonly] 
**description** | **String** | The description of the transaction. | [optional] [readonly] 
**eventDate** | **Date** | The date of the transaction | [optional] [readonly] 
**eventType** | **String** | The type of the transaction (Purchase, Cancel, etc.) | [optional] [readonly] 
**purchasingEnrollment** | **String** | The purchasing enrollment. | [optional] [readonly] 
**purchasingSubscriptionGuid** | **String** | The subscription guid that makes the transaction. | [optional] [readonly] 
**purchasingSubscriptionName** | **String** | The subscription name that makes the transaction. | [optional] [readonly] 
**quantity** | **Number** | The quantity of the transaction. | [optional] [readonly] 
**region** | **String** | The region of the transaction. | [optional] [readonly] 
**reservationOrderId** | **String** | The reservation order ID is the identifier for a reservation purchase. Each reservation order ID represents a single purchase transaction. A reservation order contains reservations. The reservation order specifies the VM size and region for the reservations. | [optional] [readonly] 
**reservationOrderName** | **String** | The name of the reservation order. | [optional] [readonly] 
**term** | **String** | This is the term of the transaction. | [optional] [readonly] 


