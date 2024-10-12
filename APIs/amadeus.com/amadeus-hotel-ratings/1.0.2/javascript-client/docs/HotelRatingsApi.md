# HotelRatings.HotelRatingsApi

All URIs are relative to *https://test.api.amadeus.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSentimentsByHotelIds**](HotelRatingsApi.md#getSentimentsByHotelIds) | **GET** /e-reputation/hotel-sentiments | Get sentiments by Amadeus Hotel Ids



## getSentimentsByHotelIds

> SuccessSentiments getSentimentsByHotelIds(hotelIds)

Get sentiments by Amadeus Hotel Ids

### Example

```javascript
import HotelRatings from 'hotel_ratings';

let apiInstance = new HotelRatings.HotelRatingsApi();
let hotelIds = ["null"]; // [String] | Comma-separated list of Amadeus Hotel Ids (max. 3) . Amadeus Hotel Ids are found in the Hotel Search response (parameter name is 'hotelId').
apiInstance.getSentimentsByHotelIds(hotelIds, (error, data, response) => {
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
 **hotelIds** | [**[String]**](String.md)| Comma-separated list of Amadeus Hotel Ids (max. 3) . Amadeus Hotel Ids are found in the Hotel Search response (parameter name is &#39;hotelId&#39;). | 

### Return type

[**SuccessSentiments**](SuccessSentiments.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

