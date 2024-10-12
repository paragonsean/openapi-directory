# PtvTimetableApiVersion3.RouteTypesApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**routeTypesGetRouteTypes**](RouteTypesApi.md#routeTypesGetRouteTypes) | **GET** /v3/route_types | View all route types and their names



## routeTypesGetRouteTypes

> V3RouteTypesResponse routeTypesGetRouteTypes(opts)

View all route types and their names

### Example

```javascript
import PtvTimetableApiVersion3 from 'ptv_timetable_api_version_3';

let apiInstance = new PtvTimetableApiVersion3.RouteTypesApi();
let opts = {
  'token': "token_example", // String | Please ignore
  'devid': "devid_example", // String | Your developer id
  'signature': "signature_example" // String | Authentication signature for request
};
apiInstance.routeTypesGetRouteTypes(opts, (error, data, response) => {
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
 **token** | **String**| Please ignore | [optional] 
 **devid** | **String**| Your developer id | [optional] 
 **signature** | **String**| Authentication signature for request | [optional] 

### Return type

[**V3RouteTypesResponse**](V3RouteTypesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/json

