# AzureReservation.ReservationAvailableScopesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservationAvailableScopes**](ReservationAvailableScopesApi.md#reservationAvailableScopes) | **POST** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}/availableScopes | Get Available Scopes for &#x60;Reservation&#x60;.



## reservationAvailableScopes

> Properties reservationAvailableScopes(reservationOrderId, reservationId, apiVersion, body)

Get Available Scopes for &#x60;Reservation&#x60;.

Get Available Scopes for &#x60;Reservation&#x60;. 

### Example

```javascript
import AzureReservation from 'azure_reservation';

let apiInstance = new AzureReservation.ReservationAvailableScopesApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let reservationId = "reservationId_example"; // String | Id of the Reservation Item
let apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
let body = ["null"]; // [String] | 
apiInstance.reservationAvailableScopes(reservationOrderId, reservationId, apiVersion, body, (error, data, response) => {
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
 **body** | [**[String]**](String.md)|  | 

### Return type

[**Properties**](Properties.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

