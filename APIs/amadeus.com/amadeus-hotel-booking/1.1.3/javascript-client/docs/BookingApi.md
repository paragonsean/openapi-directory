# HotelBooking.BookingApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBooking**](BookingApi.md#createBooking) | **POST** /booking/hotel-bookings | Create Orders associated to the Hotel Offers



## createBooking

> HotelBookedResponse createBooking(requestBody, opts)

Create Orders associated to the Hotel Offers

### Example

```javascript
import HotelBooking from 'hotel_booking';

let apiInstance = new HotelBooking.BookingApi();
let requestBody = new HotelBooking.BookingSchema(); // BookingSchema | `offerId`, `guests`, `payments` and optional `rooms` for the repartition (when used the `rooms` array items must match the shopping offer `roomQuantity`) 
let opts = {
  'amaClientRef': "amaClientRef_example", // String | Client Reference to track Request/Response
  'acceptEncoding': "acceptEncoding_example" // String | Compress the Response
};
apiInstance.createBooking(requestBody, opts, (error, data, response) => {
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
 **requestBody** | [**BookingSchema**](BookingSchema.md)| &#x60;offerId&#x60;, &#x60;guests&#x60;, &#x60;payments&#x60; and optional &#x60;rooms&#x60; for the repartition (when used the &#x60;rooms&#x60; array items must match the shopping offer &#x60;roomQuantity&#x60;)  | 
 **amaClientRef** | **String**| Client Reference to track Request/Response | [optional] 
 **acceptEncoding** | **String**| Compress the Response | [optional] 

### Return type

[**HotelBookedResponse**](HotelBookedResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.amadeus+json
- **Accept**: application/vnd.amadeus+json

