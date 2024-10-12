# AzureReservation.ReservationSplitApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservationSplit**](ReservationSplitApi.md#reservationSplit) | **POST** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/split | Split the &#x60;Reservation&#x60;.



## reservationSplit

> [ReservationResponse] reservationSplit(reservationOrderId, apiVersion, body)

Split the &#x60;Reservation&#x60;.

Split a &#x60;Reservation&#x60; into two &#x60;Reservation&#x60;s with specified quantity distribution.

### Example

```javascript
import AzureReservation from 'azure_reservation';

let apiInstance = new AzureReservation.ReservationSplitApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
let body = new AzureReservation.SplitRequest(); // SplitRequest | Information needed to Split a reservation item
apiInstance.reservationSplit(reservationOrderId, apiVersion, body, (error, data, response) => {
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
 **apiVersion** | **String**| Supported version for this document is 2019-04-01 | 
 **body** | [**SplitRequest**](SplitRequest.md)| Information needed to Split a reservation item | 

### Return type

[**[ReservationResponse]**](ReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

