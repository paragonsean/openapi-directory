# QuickStartTelematicsSdk.Class22UserTripsOptionalApi

All URIs are relative to *https://api.telematicssdk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tripsTripDetails_0**](Class22UserTripsOptionalApi.md#tripsTripDetails_0) | **GET** /mobilesdk/stage/track/get_track/v1 | Trips - trip details



## tripsTripDetails_0

> TripsTripDetails200Response tripsTripDetails_0(opts)

Trips - trip details

Trips - trip details

### Example

```javascript
import QuickStartTelematicsSdk from 'quick_start_telematics_sdk';

let apiInstance = new QuickStartTelematicsSdk.Class22UserTripsOptionalApi();
let opts = {
  'trackToken': "" // String | 
};
apiInstance.tripsTripDetails_0(opts, (error, data, response) => {
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
 **trackToken** | **String**|  | [optional] 

### Return type

[**TripsTripDetails200Response**](TripsTripDetails200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

