# AzureReservation.ReservationMergeApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservationMerge**](ReservationMergeApi.md#reservationMerge) | **POST** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/merge | Merges two &#x60;Reservation&#x60;s.



## reservationMerge

> [ReservationResponse] reservationMerge(reservationOrderId, apiVersion, body)

Merges two &#x60;Reservation&#x60;s.

Merge the specified &#x60;Reservation&#x60;s into a new &#x60;Reservation&#x60;. The two &#x60;Reservation&#x60;s being merged must have same properties.

### Example

```javascript
import AzureReservation from 'azure_reservation';

let apiInstance = new AzureReservation.ReservationMergeApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation 
let apiVersion = "apiVersion_example"; // String | Supported version.
let body = new AzureReservation.MergeRequest(); // MergeRequest | Information needed for commercial request for a reservation
apiInstance.reservationMerge(reservationOrderId, apiVersion, body, (error, data, response) => {
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
 **reservationOrderId** | **String**| Order Id of the reservation  | 
 **apiVersion** | **String**| Supported version. | 
 **body** | [**MergeRequest**](MergeRequest.md)| Information needed for commercial request for a reservation | 

### Return type

[**[ReservationResponse]**](ReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

