# Search.FiltersApi

All URIs are relative to *https://api.tomtom.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchVersionNumberGeometryFilterExtGet**](FiltersApi.md#searchVersionNumberGeometryFilterExtGet) | **GET** /search/{versionNumber}/geometryFilter.{ext} | Geometry Filter
[**searchVersionNumberGeometryFilterExtPost**](FiltersApi.md#searchVersionNumberGeometryFilterExtPost) | **POST** /search/{versionNumber}/geometryFilter.{ext} | Geometry Filter
[**searchVersionNumberRoutedFilterPositionHeadingExtGet**](FiltersApi.md#searchVersionNumberRoutedFilterPositionHeadingExtGet) | **GET** /search/{versionNumber}/routedFilter/{position}/{heading}.{ext} | Routed Filter
[**searchVersionNumberRoutedFilterPositionHeadingExtPost**](FiltersApi.md#searchVersionNumberRoutedFilterPositionHeadingExtPost) | **POST** /search/{versionNumber}/routedFilter/{position}/{heading}.{ext} | Routed Filter



## searchVersionNumberGeometryFilterExtGet

> searchVersionNumberGeometryFilterExtGet(versionNumber, ext, geometryList, poiList)

Geometry Filter

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.FiltersApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let ext = "xml"; // String | Expected response format.
let geometryList = "[{\"type\":\"CIRCLE\", \"position\":\"40.80558, -73.96548\", \"radius\":100}, {\"type\":\"POLYGON\", \"vertices\":[\"37.7524152343544, -122.43576049804686\", \"37.70660472542312, -122.43301391601562\", \"37.712059855877314, -122.36434936523438\", \"37.75350561243041, -122.37396240234374\"]}]"; // String | List of geometries to filter by. Available types are CIRCLE (with the radius expressed in meters) and POLYGON.
let poiList = "[{\"poi\":{\"name\":\"S Restaurant Toms\"},\"address\":{\"freeformAddress\":\"2880 Broadway, New York, NY 10025\"},\"position\":{\"lat\":40.80558,\"lon\":-73.96548}},{\"poi\":{\"name\":\"Yasha Raman Corporation\"},\"address\":{\"freeformAddress\":\"940 Amsterdam Ave, New York, NY 10025\"},\"position\":{\"lat\":40.80076,\"lon\":-73.96556}}]"; // String | List of POIs to filter. The only required attribute of a POI is position, everything else is optional and will be echoed back when passed in.
apiInstance.searchVersionNumberGeometryFilterExtGet(versionNumber, ext, geometryList, poiList, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionNumber** | **Number**| Service version number. The current value is 2. | 
 **ext** | **String**| Expected response format. | 
 **geometryList** | **String**| List of geometries to filter by. Available types are CIRCLE (with the radius expressed in meters) and POLYGON. | 
 **poiList** | **String**| List of POIs to filter. The only required attribute of a POI is position, everything else is optional and will be echoed back when passed in. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## searchVersionNumberGeometryFilterExtPost

> searchVersionNumberGeometryFilterExtPost(versionNumber, ext, opts)

Geometry Filter

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.FiltersApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let ext = "xml"; // String | Expected response format.
let opts = {
  'searchVersionNumberGeometryFilterExtPostRequest': new Search.SearchVersionNumberGeometryFilterExtPostRequest() // SearchVersionNumberGeometryFilterExtPostRequest | 
};
apiInstance.searchVersionNumberGeometryFilterExtPost(versionNumber, ext, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionNumber** | **Number**| Service version number. The current value is 2. | 
 **ext** | **String**| Expected response format. | 
 **searchVersionNumberGeometryFilterExtPostRequest** | [**SearchVersionNumberGeometryFilterExtPostRequest**](SearchVersionNumberGeometryFilterExtPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## searchVersionNumberRoutedFilterPositionHeadingExtGet

> searchVersionNumberRoutedFilterPositionHeadingExtGet(versionNumber, position, heading, ext, poiList, opts)

Routed Filter

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.FiltersApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let position = "37.8328,-122.27669"; // String | This is specified as a comma separated string composed of lat., lon.
let heading = -15.6; // Number | The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.)
let ext = "xml"; // String | Expected response format.
let poiList = "[{\"poi\":{\"name\":\"Cleaire Advanced Emission Controls\"},\"address\":{\"freeformAddress\":\"7220 Trade St, San Diego, CA 92121\"},\"position\":{\"lat\":\"37.83274\",\"lon\":\"-122.27631\"}}]"; // String | List of POIs to filter. The only required attribute of a POI is position, everything else is optional and will be echoed back when passed in.
let opts = {
  'routingTimeout': 4000 // Number | Only return results that arrive from routing engine within this time limit.
};
apiInstance.searchVersionNumberRoutedFilterPositionHeadingExtGet(versionNumber, position, heading, ext, poiList, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionNumber** | **Number**| Service version number. The current value is 2. | 
 **position** | **String**| This is specified as a comma separated string composed of lat., lon. | 
 **heading** | **Number**| The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.) | 
 **ext** | **String**| Expected response format. | 
 **poiList** | **String**| List of POIs to filter. The only required attribute of a POI is position, everything else is optional and will be echoed back when passed in. | 
 **routingTimeout** | **Number**| Only return results that arrive from routing engine within this time limit. | [optional] [default to 4000]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## searchVersionNumberRoutedFilterPositionHeadingExtPost

> searchVersionNumberRoutedFilterPositionHeadingExtPost(versionNumber, position, heading, ext, opts)

Routed Filter

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.FiltersApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let position = "37.8328,-122.27669"; // String | This is specified as a comma separated string composed of lat., lon.
let heading = 90; // Number | The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.)
let ext = "xml"; // String | Expected response format.
let opts = {
  'routingTimeout': 4000, // Number | Only return results that arrive from routing engine within this time limit.
  'searchVersionNumberRoutedFilterPositionHeadingExtPostRequest': new Search.SearchVersionNumberRoutedFilterPositionHeadingExtPostRequest() // SearchVersionNumberRoutedFilterPositionHeadingExtPostRequest | 
};
apiInstance.searchVersionNumberRoutedFilterPositionHeadingExtPost(versionNumber, position, heading, ext, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionNumber** | **Number**| Service version number. The current value is 2. | 
 **position** | **String**| This is specified as a comma separated string composed of lat., lon. | 
 **heading** | **Number**| The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.) | 
 **ext** | **String**| Expected response format. | 
 **routingTimeout** | **Number**| Only return results that arrive from routing engine within this time limit. | [optional] [default to 4000]
 **searchVersionNumberRoutedFilterPositionHeadingExtPostRequest** | [**SearchVersionNumberRoutedFilterPositionHeadingExtPostRequest**](SearchVersionNumberRoutedFilterPositionHeadingExtPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

