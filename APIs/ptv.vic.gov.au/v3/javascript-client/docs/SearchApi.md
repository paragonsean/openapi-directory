# PtvTimetableApiVersion3.SearchApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchSearch**](SearchApi.md#searchSearch) | **GET** /v3/search/{search_term} | View stops, routes and myki ticket outlets that match the search term



## searchSearch

> V3SearchResult searchSearch(searchTerm, opts)

View stops, routes and myki ticket outlets that match the search term

### Example

```javascript
import PtvTimetableApiVersion3 from 'ptv_timetable_api_version_3';

let apiInstance = new PtvTimetableApiVersion3.SearchApi();
let searchTerm = "searchTerm_example"; // String | Search text (note: if search text is numeric and/or less than 3 characters, the API will only return routes)
let opts = {
  'routeTypes': [null], // [Number] | Filter by route_type; values returned via RouteTypes API (note: stops and routes are ordered by route_types specified)
  'latitude': 3.4, // Number | Filter by geographic coordinate of latitude
  'longitude': 3.4, // Number | Filter by geographic coordinate of longitude
  'maxDistance': 3.4, // Number | Filter by maximum distance (in metres) from location specified via latitude and longitude parameters
  'includeAddresses': true, // Boolean | Placeholder for future development; currently unavailable
  'includeOutlets': true, // Boolean | Indicates if outlets will be returned in response (default = true)
  'matchStopBySuburb': true, // Boolean | Indicates whether to find stops by suburbs in the search term (default = true)
  'matchRouteBySuburb': true, // Boolean | Indicates whether to find routes by suburbs in the search term (default = true)
  'matchStopByGtfsStopId': true, // Boolean | Indicates whether to search for stops according to a metlink stop ID (default = false)
  'token': "token_example", // String | Please ignore
  'devid': "devid_example", // String | Your developer id
  'signature': "signature_example" // String | Authentication signature for request
};
apiInstance.searchSearch(searchTerm, opts, (error, data, response) => {
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
 **searchTerm** | **String**| Search text (note: if search text is numeric and/or less than 3 characters, the API will only return routes) | 
 **routeTypes** | [**[Number]**](Number.md)| Filter by route_type; values returned via RouteTypes API (note: stops and routes are ordered by route_types specified) | [optional] 
 **latitude** | **Number**| Filter by geographic coordinate of latitude | [optional] 
 **longitude** | **Number**| Filter by geographic coordinate of longitude | [optional] 
 **maxDistance** | **Number**| Filter by maximum distance (in metres) from location specified via latitude and longitude parameters | [optional] 
 **includeAddresses** | **Boolean**| Placeholder for future development; currently unavailable | [optional] 
 **includeOutlets** | **Boolean**| Indicates if outlets will be returned in response (default &#x3D; true) | [optional] 
 **matchStopBySuburb** | **Boolean**| Indicates whether to find stops by suburbs in the search term (default &#x3D; true) | [optional] 
 **matchRouteBySuburb** | **Boolean**| Indicates whether to find routes by suburbs in the search term (default &#x3D; true) | [optional] 
 **matchStopByGtfsStopId** | **Boolean**| Indicates whether to search for stops according to a metlink stop ID (default &#x3D; false) | [optional] 
 **token** | **String**| Please ignore | [optional] 
 **devid** | **String**| Your developer id | [optional] 
 **signature** | **String**| Authentication signature for request | [optional] 

### Return type

[**V3SearchResult**](V3SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/json

