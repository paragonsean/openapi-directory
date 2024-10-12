# SeatmapDisplay.DisplaySeatMapsApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSeatmapFromFlightOffer**](DisplaySeatMapsApi.md#getSeatmapFromFlightOffer) | **POST** /shopping/seatmaps | Returns all the seat maps of a given flightOffer.
[**getSeatmapFromOrder**](DisplaySeatMapsApi.md#getSeatmapFromOrder) | **GET** /shopping/seatmaps | Returns all the seat maps of a given order.



## getSeatmapFromFlightOffer

> SeatMapReply getSeatmapFromFlightOffer(xHTTPMethodOverride, body)

Returns all the seat maps of a given flightOffer.

### Example

```javascript
import SeatmapDisplay from 'seatmap_display';

let apiInstance = new SeatmapDisplay.DisplaySeatMapsApi();
let xHTTPMethodOverride = "'GET'"; // String | the HTTP method to apply
let body = new SeatmapDisplay.FlightOffers(); // FlightOffers | 
apiInstance.getSeatmapFromFlightOffer(xHTTPMethodOverride, body, (error, data, response) => {
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
 **xHTTPMethodOverride** | **String**| the HTTP method to apply | [default to &#39;GET&#39;]
 **body** | [**FlightOffers**](FlightOffers.md)|  | 

### Return type

[**SeatMapReply**](SeatMapReply.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.amadeus+json
- **Accept**: application/vnd.amadeus+json


## getSeatmapFromOrder

> SeatMapReply getSeatmapFromOrder(opts)

Returns all the seat maps of a given order.

### Example

```javascript
import SeatmapDisplay from 'seatmap_display';

let apiInstance = new SeatmapDisplay.DisplaySeatMapsApi();
let opts = {
  'flightOrderId': "flightOrderId_example", // String | identifier of the order
  'flightOrderId2': "flightOrderId_example" // String | DEPRECATED identifier of the order , kept for backward compatibility
};
apiInstance.getSeatmapFromOrder(opts, (error, data, response) => {
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
 **flightOrderId** | **String**| identifier of the order | [optional] 
 **flightOrderId2** | **String**| DEPRECATED identifier of the order , kept for backward compatibility | [optional] 

### Return type

[**SeatMapReply**](SeatMapReply.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

