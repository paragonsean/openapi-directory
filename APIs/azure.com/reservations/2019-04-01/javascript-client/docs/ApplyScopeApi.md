# AzureReservation.ApplyScopeApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservationUpdate_0**](ApplyScopeApi.md#reservationUpdate_0) | **PATCH** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId} | Updates a &#x60;Reservation&#x60;.



## reservationUpdate_0

> ReservationResponse reservationUpdate_0(reservationOrderId, reservationId, apiVersion, parameters)

Updates a &#x60;Reservation&#x60;.

Updates the applied scopes of the &#x60;Reservation&#x60;.

### Example

```javascript
import AzureReservation from 'azure_reservation';

let apiInstance = new AzureReservation.ApplyScopeApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let reservationId = "reservationId_example"; // String | Id of the Reservation Item
let apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
let parameters = new AzureReservation.Patch(); // Patch | Information needed to patch a reservation item
apiInstance.reservationUpdate_0(reservationOrderId, reservationId, apiVersion, parameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservationOrderId** | **String**| Order Id of the reservation | 
 **reservationId** | **String**| Id of the Reservation Item | 
 **apiVersion** | **String**| Supported version for this document is 2019-04-01 | 
 **parameters** | [**Patch**](Patch.md)| Information needed to patch a reservation item | 

### Return type

[**ReservationResponse**](ReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

