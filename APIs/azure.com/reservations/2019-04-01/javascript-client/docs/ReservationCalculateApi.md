# AzureReservation.ReservationCalculateApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservationOrderCalculate**](ReservationCalculateApi.md#reservationOrderCalculate) | **POST** /providers/Microsoft.Capacity/calculatePrice | Calculate price for a &#x60;ReservationOrder&#x60;.



## reservationOrderCalculate

> CalculatePriceResponse reservationOrderCalculate(apiVersion, body)

Calculate price for a &#x60;ReservationOrder&#x60;.

Calculate price for placing a &#x60;ReservationOrder&#x60;.

### Example

```javascript
import AzureReservation from 'azure_reservation';

let apiInstance = new AzureReservation.ReservationCalculateApi();
let apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
let body = new AzureReservation.PurchaseRequest(); // PurchaseRequest | Information needed for calculate or purchase reservation
apiInstance.reservationOrderCalculate(apiVersion, body, (error, data, response) => {
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
 **apiVersion** | **String**| Supported version for this document is 2019-04-01 | 
 **body** | [**PurchaseRequest**](PurchaseRequest.md)| Information needed for calculate or purchase reservation | 

### Return type

[**CalculatePriceResponse**](CalculatePriceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

