# PtvTimetableApiVersion3.FareEstimateApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fareEstimateGetFareEstimateByZone**](FareEstimateApi.md#fareEstimateGetFareEstimateByZone) | **GET** /v3/fare_estimate/min_zone/{minZone}/max_zone/{maxZone} | Estimate a fare by zone



## fareEstimateGetFareEstimateByZone

> Object fareEstimateGetFareEstimateByZone(minZone, maxZone, opts)

Estimate a fare by zone

### Example

```javascript
import PtvTimetableApiVersion3 from 'ptv_timetable_api_version_3';

let apiInstance = new PtvTimetableApiVersion3.FareEstimateApi();
let minZone = 56; // Number | Minimum Zone travelled through ie. 1
let maxZone = 56; // Number | Maximum Zone travelled through id. 6
let opts = {
  'journeyTouchOnUtc': new Date("2013-10-20T19:20:30+01:00"), // Date | JourneyTouchOnUtc in format yyyy-M-d h:m (e.g 2016-5-31 16:53).
  'journeyTouchOffUtc': new Date("2013-10-20T19:20:30+01:00"), // Date | JourneyTouchOffUtc in format yyyy-M-d h:m (e.g 2016-5-31 16:53).
  'isJourneyInFreeTramZone': true, // Boolean | 
  'travelledRouteTypes': [null], // [Number] | 
  'token': "token_example", // String | Please ignore
  'devid': "devid_example", // String | Your developer id
  'signature': "signature_example" // String | Authentication signature for request
};
apiInstance.fareEstimateGetFareEstimateByZone(minZone, maxZone, opts, (error, data, response) => {
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
 **minZone** | **Number**| Minimum Zone travelled through ie. 1 | 
 **maxZone** | **Number**| Maximum Zone travelled through id. 6 | 
 **journeyTouchOnUtc** | **Date**| JourneyTouchOnUtc in format yyyy-M-d h:m (e.g 2016-5-31 16:53). | [optional] 
 **journeyTouchOffUtc** | **Date**| JourneyTouchOffUtc in format yyyy-M-d h:m (e.g 2016-5-31 16:53). | [optional] 
 **isJourneyInFreeTramZone** | **Boolean**|  | [optional] 
 **travelledRouteTypes** | [**[Number]**](Number.md)|  | [optional] 
 **token** | **String**| Please ignore | [optional] 
 **devid** | **String**| Your developer id | [optional] 
 **signature** | **String**| Authentication signature for request | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/json

