# HetrasBookingApiVersion0.AvailabilityApi

All URIs are relative to *https://api.hetras-certification.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**availabilityGet**](AvailabilityApi.md#availabilityGet) | **GET** /api/booking/v0/availability | Gets the availability and occupancy for a specific hotel and timespan.



## availabilityGet

> AvailabilityResponse availabilityGet(appId, appKey, hotelId, from, to, opts)

Gets the availability and occupancy for a specific hotel and timespan.

Read past occupancy and future availability for a specific hotel. You can also request the breakdown per room type.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.AvailabilityApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | Specifies the hotel id to request the availability for.
let from = new Date("2013-10-20T19:20:30+01:00"); // Date | Defines the first business day you would like to get availability numbers for.
let to = new Date("2013-10-20T19:20:30+01:00"); // Date | Defines the last business day you would like to get availability numbers for. The maximum time span between <i>from</i>´and <i>to</i>              is limited to 365 days.
let opts = {
  'expand': "expand_example", // String | You can expand the room types breakdown per business day for the availibility numbers if need be.
  'skip': 56, // Number | Amount of items to skip.
  'top': 56, // Number | Amount of items to select.
  'inlinecount': "inlinecount_example" // String | Return total number of items for a given filter criteria.
};
apiInstance.availabilityGet(appId, appKey, hotelId, from, to, opts, (error, data, response) => {
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
 **hotelId** | **Number**| Specifies the hotel id to request the availability for. | 
 **from** | **Date**| Defines the first business day you would like to get availability numbers for. | 
 **to** | **Date**| Defines the last business day you would like to get availability numbers for. The maximum time span between &lt;i&gt;from&lt;/i&gt;´and &lt;i&gt;to&lt;/i&gt;              is limited to 365 days. | 
 **expand** | **String**| You can expand the room types breakdown per business day for the availibility numbers if need be. | [optional] 
 **skip** | **Number**| Amount of items to skip. | [optional] 
 **top** | **Number**| Amount of items to select. | [optional] 
 **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] 

### Return type

[**AvailabilityResponse**](AvailabilityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

