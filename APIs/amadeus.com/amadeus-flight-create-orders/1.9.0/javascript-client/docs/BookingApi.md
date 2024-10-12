# FlightCreateOrders.BookingApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createFligtOrders**](BookingApi.md#createFligtOrders) | **POST** /booking/flight-orders | Create Order associated to the Flight offers.



## createFligtOrders

> SuccessBooking createFligtOrders(body)

Create Order associated to the Flight offers.

### Example

```javascript
import FlightCreateOrders from 'flight_create_orders';

let apiInstance = new FlightCreateOrders.BookingApi();
let body = new FlightCreateOrders.FlightOrderQuery(); // FlightOrderQuery | list of element needed to book a flight Order
apiInstance.createFligtOrders(body, (error, data, response) => {
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
 **body** | [**FlightOrderQuery**](FlightOrderQuery.md)| list of element needed to book a flight Order | 

### Return type

[**SuccessBooking**](SuccessBooking.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.amadeus+json
- **Accept**: application/vnd.amadeus+json

