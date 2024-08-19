# ImpalaHotelBookingApi.RateCalendarApi

All URIs are relative to *https://sandbox.impala.travel/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listRatePlanForHotelForRatePlanId**](RateCalendarApi.md#listRatePlanForHotelForRatePlanId) | **GET** /hotels/{hotelId}/rate-plans/{ratePlanId} | List a rate plan (rate calendar) for a hotel (Beta endpoint).
[**listRatePlansForHotel**](RateCalendarApi.md#listRatePlansForHotel) | **GET** /hotels/{hotelId}/rate-plans | List all rate plans (rate calendar) for a hotel (Beta endpoint)



## listRatePlanForHotelForRatePlanId

> RatePlan listRatePlanForHotelForRatePlanId(hotelId, ratePlanId, opts)

List a rate plan (rate calendar) for a hotel (Beta endpoint).

Returns a single rate plan available for you for a hotel.  Rate plans are products the hotel is offering. They typically consist of a combination of restrictiveness in case of cancellations or changes, the time they&#39;re bookable, minimum or maximum length of stay restrictions (e.g. week-long bookings), included components like breakfast or dinner and/or the conditions under which the room can be sold (e.g. private rates that can only be offered and sold to a closed user group behind login).  Examples of rate plans:  * Non-refundable room rate that includes breakfast * Room-only rate with free cancellation up to 14 days before arrival  This endpoint returns a singular available rate plan.

### Example

```javascript
import ImpalaHotelBookingApi from 'impala_hotel_booking_api';
let defaultClient = ImpalaHotelBookingApi.ApiClient.instance;
// Configure API key authorization: API_Key_Authentication
let API_Key_Authentication = defaultClient.authentications['API_Key_Authentication'];
API_Key_Authentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key_Authentication.apiKeyPrefix = 'Token';

let apiInstance = new ImpalaHotelBookingApi.RateCalendarApi();
let hotelId = "40c0b330-186a-40bf-ae36-2c61fb322db0"; // String | The uuid of hotel for which rate plans are being fetched.
let ratePlanId = 112; // Number | The id of requested rateplan
let opts = {
  'updatedAt': {key: null}, // Object | Returns rate plans changed after the supplied date.
  'size': 40, // Number | Number of rate plans returned on a given page (pagination).
  'offset': 25, // Number | Offset from the first rate plan in the result (for pagination).
  'start': "2022-05-12", // String | Start date of the considered time window for the returned rate plan.
  'end': "2022-05-12", // String | Start date of the considered time window for the returned rate plan.
  'roomTypeId': "6d3a255d-3b22-48a4-8076-3ae3d0ade3d7" // String | The uuid of room for which rate plans are being fetched.
};
apiInstance.listRatePlanForHotelForRatePlanId(hotelId, ratePlanId, opts, (error, data, response) => {
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
 **hotelId** | **String**| The uuid of hotel for which rate plans are being fetched. | 
 **ratePlanId** | **Number**| The id of requested rateplan | 
 **updatedAt** | [**Object**](.md)| Returns rate plans changed after the supplied date. | [optional] 
 **size** | **Number**| Number of rate plans returned on a given page (pagination). | [optional] [default to 25]
 **offset** | **Number**| Offset from the first rate plan in the result (for pagination). | [optional] [default to 0]
 **start** | **String**| Start date of the considered time window for the returned rate plan. | [optional] 
 **end** | **String**| Start date of the considered time window for the returned rate plan. | [optional] 
 **roomTypeId** | **String**| The uuid of room for which rate plans are being fetched. | [optional] 

### Return type

[**RatePlan**](RatePlan.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRatePlansForHotel

> ListRatePlansForHotel200Response listRatePlansForHotel(hotelId, opts)

List all rate plans (rate calendar) for a hotel (Beta endpoint)

Returns a list of all rate plans available for you for a hotel.  Rate plans are products the hotel is offering. They typically consist of a combination of restrictiveness in case of cancellations or changes, the time they&#39;re bookable, minimum or maximum length of stay restrictions (e.g. week-long bookings), included components like breakfast or dinner and/or the conditions under which the room can be sold (e.g. private rates that can only be offered and sold to a closed user group behind login).  Examples of rate plans:  * Non-refundable room rate that includes breakfast * Room-only rate with free cancellation up to 14 days before arrival  For each such rate plan this endpoint returns the room types it&#39;s available for, alongside prices for each date and occupancy that can be sold – or the information that the room isn&#39;t available (closed) for a certain date.  For the vast majority of our customers, availability searches using the [List all hotels](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1hotels/get) endpoint are the best choice. It accepts the dates your guest is looking for and provides the rates to display.  This endpoint can help augment this for two additional use cases:  This endpoint allows you to query rate prices for all future dates in one go, making it a great choice to feed availability information and prices into your own system or displaying a rate calender to guide your guests to gain an overview of future availability and prices.

### Example

```javascript
import ImpalaHotelBookingApi from 'impala_hotel_booking_api';
let defaultClient = ImpalaHotelBookingApi.ApiClient.instance;
// Configure API key authorization: API_Key_Authentication
let API_Key_Authentication = defaultClient.authentications['API_Key_Authentication'];
API_Key_Authentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key_Authentication.apiKeyPrefix = 'Token';

let apiInstance = new ImpalaHotelBookingApi.RateCalendarApi();
let hotelId = "40c0b330-186a-40bf-ae36-2c61fb322db0"; // String | The uuid of hotel for which rate plans are being fetched.
let opts = {
  'updatedAt': {key: null}, // Object | Returns rate plans changed after the supplied date.
  'size': 40, // Number | Number of rate plans returned on a given page (pagination).
  'offset': 25, // Number | Offset from the first rate plan in the result (for pagination).
  'start': "2022-05-12", // String | Start date of the considered time window for the returned rate plan.
  'end': "2022-05-12", // String | Start date of the considered time window for the returned rate plan.
  'roomId': "6d3a255d-3b22-48a4-8076-3ae3d0ade3d7" // String | The UUID of room for which rate plans are being fetched.
};
apiInstance.listRatePlansForHotel(hotelId, opts, (error, data, response) => {
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
 **hotelId** | **String**| The uuid of hotel for which rate plans are being fetched. | 
 **updatedAt** | [**Object**](.md)| Returns rate plans changed after the supplied date. | [optional] 
 **size** | **Number**| Number of rate plans returned on a given page (pagination). | [optional] [default to 25]
 **offset** | **Number**| Offset from the first rate plan in the result (for pagination). | [optional] [default to 0]
 **start** | **String**| Start date of the considered time window for the returned rate plan. | [optional] 
 **end** | **String**| Start date of the considered time window for the returned rate plan. | [optional] 
 **roomId** | **String**| The UUID of room for which rate plans are being fetched. | [optional] 

### Return type

[**ListRatePlansForHotel200Response**](ListRatePlansForHotel200Response.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

