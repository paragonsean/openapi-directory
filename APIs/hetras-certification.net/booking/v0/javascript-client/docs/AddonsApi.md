# HetrasBookingApiVersion0.AddonsApi

All URIs are relative to *https://api.hetras-certification.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addonsGet**](AddonsApi.md#addonsGet) | **GET** /api/booking/v0/addons | Get a list of offers for addon services for the specified guest stay details.



## addonsGet

> Addons addonsGet(appId, appKey, hotelId, arrivalDate, departureDate, channelCode, adults, rooms, roomType, ratePlanCode, opts)

Get a list of offers for addon services for the specified guest stay details.

With the addons request you can get a list of offers for addon services available for a specific rate, room type              and guest stay details.The channel code will define which rates will be returned based on the access control               configuration for related rates.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.AddonsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | Specifies the hotel id to request offers for.
let arrivalDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Date from when the addon service will be booked to the reservation in the ISO-8601 format \"YYYY-MM-DD\".
let departureDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Date until when the addon service will be booked to the reservation in the ISO-8601 format \"YYYY-MM-DD\".              This is usually the departure date of the reservation.
let channelCode = "channelCode_example"; // String | Channel Code the rate plan needs to be configured for.
let adults = null; // Blob | Number of adults per room.
let rooms = null; // Blob | Number of rooms.
let roomType = "roomType_example"; // String | Only return offers for the specified room type code.
let ratePlanCode = "ratePlanCode_example"; // String | Only return offers for the specified rate plan code.
let opts = {
  'expand': "expand_example" // String | Expand the rates breakdown if required.
};
apiInstance.addonsGet(appId, appKey, hotelId, arrivalDate, departureDate, channelCode, adults, rooms, roomType, ratePlanCode, opts, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **hotelId** | **Number**| Specifies the hotel id to request offers for. | 
 **arrivalDate** | **Date**| Date from when the addon service will be booked to the reservation in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;. | 
 **departureDate** | **Date**| Date until when the addon service will be booked to the reservation in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;.              This is usually the departure date of the reservation. | 
 **channelCode** | **String**| Channel Code the rate plan needs to be configured for. | 
 **adults** | **Blob**| Number of adults per room. | 
 **rooms** | **Blob**| Number of rooms. | 
 **roomType** | **String**| Only return offers for the specified room type code. | 
 **ratePlanCode** | **String**| Only return offers for the specified rate plan code. | 
 **expand** | **String**| Expand the rates breakdown if required. | [optional] 

### Return type

[**Addons**](Addons.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

