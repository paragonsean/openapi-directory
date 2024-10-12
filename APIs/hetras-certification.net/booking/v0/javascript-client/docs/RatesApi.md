# HetrasBookingApiVersion0.RatesApi

All URIs are relative to *https://api.hetras-certification.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ratesGet**](RatesApi.md#ratesGet) | **GET** /api/booking/v0/rates | Get a list of room offers for the specified guest stay details.



## ratesGet

> Rates ratesGet(appId, appKey, hotelId, arrivalDate, departureDate, channelCode, adults, opts)

Get a list of room offers for the specified guest stay details.

With the rates request you can get a list of different rate offers per room type. You will have to at least               specify the hotel, the arrival and departure date, number of adults per room and the channel code. The channel code              will define which rates will be returned based on the access control configuration for the rates.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.RatesApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | Specifies the hotel id to request offers for.
let arrivalDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Date of arrival for the guest in the ISO-8601 format \"YYYY-MM-DD\".
let departureDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Date of departure for the guest in the ISO-8601 format \"YYYY-MM-DD\".
let channelCode = "channelCode_example"; // String | Channel Code the rate plan needs to be configured for.
let adults = null; // Blob | Number of adults per room.
let opts = {
  'rooms': null, // Blob | Number of rooms (default is 1).
  'roomType': "roomType_example", // String | Only return offers with rates for the specified room type code.
  'ratePlanCode': "ratePlanCode_example", // String | Only return offers for the specified room type code.
  'groupCode': "groupCode_example", // String | Only return offers for the specified group code.
  'expand': "expand_example" // String | Expand the rates breakdown if required.
};
apiInstance.ratesGet(appId, appKey, hotelId, arrivalDate, departureDate, channelCode, adults, opts, (error, data, response) => {
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
 **arrivalDate** | **Date**| Date of arrival for the guest in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;. | 
 **departureDate** | **Date**| Date of departure for the guest in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;. | 
 **channelCode** | **String**| Channel Code the rate plan needs to be configured for. | 
 **adults** | **Blob**| Number of adults per room. | 
 **rooms** | **Blob**| Number of rooms (default is 1). | [optional] 
 **roomType** | **String**| Only return offers with rates for the specified room type code. | [optional] 
 **ratePlanCode** | **String**| Only return offers for the specified room type code. | [optional] 
 **groupCode** | **String**| Only return offers for the specified group code. | [optional] 
 **expand** | **String**| Expand the rates breakdown if required. | [optional] 

### Return type

[**Rates**](Rates.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

