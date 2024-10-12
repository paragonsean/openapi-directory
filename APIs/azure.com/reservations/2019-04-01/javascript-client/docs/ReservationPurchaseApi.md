# AzureReservation.ReservationPurchaseApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservationOrderPurchase**](ReservationPurchaseApi.md#reservationOrderPurchase) | **PUT** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId} | Purchase &#x60;ReservationOrder&#x60;



## reservationOrderPurchase

> ReservationOrderResponse reservationOrderPurchase(reservationOrderId, apiVersion, body)

Purchase &#x60;ReservationOrder&#x60;

Purchase &#x60;ReservationOrder&#x60; and create resource under the specified URI.

### Example

```javascript
import AzureReservation from 'azure_reservation';

let apiInstance = new AzureReservation.ReservationPurchaseApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
let body = new AzureReservation.PurchaseRequest(); // PurchaseRequest | Information needed for calculate or purchase reservation
apiInstance.reservationOrderPurchase(reservationOrderId, apiVersion, body, (error, data, response) => {
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
 **body** | [**PurchaseRequest**](PurchaseRequest.md)| Information needed for calculate or purchase reservation | 

### Return type

[**ReservationOrderResponse**](ReservationOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

