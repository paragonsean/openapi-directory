# FlightOrderManagement.BookingApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelFlightOrder**](BookingApi.md#cancelFlightOrder) | **DELETE** /booking/flight-orders/{flight-orderId} | Cancel a given flight order
[**getFlightOrder**](BookingApi.md#getFlightOrder) | **GET** /booking/flight-orders/{flight-orderId} | Retrieve a given flight order



## cancelFlightOrder

> cancelFlightOrder(flightOrderId)

Cancel a given flight order

### Example

```javascript
import FlightOrderManagement from 'flight_order_management';

let apiInstance = new FlightOrderManagement.BookingApi();
let flightOrderId = "flightOrderId_example"; // String | identifier of the flight order
apiInstance.cancelFlightOrder(flightOrderId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flightOrderId** | **String**| identifier of the flight order | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json


## getFlightOrder

> SuccessBooking getFlightOrder(flightOrderId)

Retrieve a given flight order

### Example

```javascript
import FlightOrderManagement from 'flight_order_management';

let apiInstance = new FlightOrderManagement.BookingApi();
let flightOrderId = "flightOrderId_example"; // String | identifier of the flight order
apiInstance.getFlightOrder(flightOrderId, (error, data, response) => {
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
 **flightOrderId** | **String**| identifier of the flight order | 

### Return type

[**SuccessBooking**](SuccessBooking.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

