# Search.ReverseGeocodingApi

All URIs are relative to *https://api.tomtom.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchVersionNumberReverseGeocodeCrossStreetPositionExtGet**](ReverseGeocodingApi.md#searchVersionNumberReverseGeocodeCrossStreetPositionExtGet) | **GET** /search/{versionNumber}/reverseGeocode/crossStreet/{position}.{ext} | Cross Street lookup
[**searchVersionNumberReverseGeocodePositionExtGet**](ReverseGeocodingApi.md#searchVersionNumberReverseGeocodePositionExtGet) | **GET** /search/{versionNumber}/reverseGeocode/{position}.{ext} | Reverse Geocode



## searchVersionNumberReverseGeocodeCrossStreetPositionExtGet

> searchVersionNumberReverseGeocodeCrossStreetPositionExtGet(versionNumber, position, ext, opts)

Cross Street lookup

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.ReverseGeocodingApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let position = "37.8328,-122.27669"; // String | This is specified as a comma separated string composed of lat., lon.
let ext = "xml"; // String | Expected response format.
let opts = {
  'limit': 1, // Number | Maximum number of cross-streets to return.
  'spatialKeys': false, // Boolean | If the \"spatialKeys\" flag is set, the response will also contain a proprietary geospatial keys for a specified location.
  'heading': 3.4, // Number | The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.)
  'radius': 10000, // Number | The maximum distance in meters from the specified position for the reverse geocoder to consider.
  'language': "language_example" // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
};
apiInstance.searchVersionNumberReverseGeocodeCrossStreetPositionExtGet(versionNumber, position, ext, opts, (error, data, response) => {
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
 **ext** | **String**| Expected response format. | 
 **limit** | **Number**| Maximum number of cross-streets to return. | [optional] [default to 1]
 **spatialKeys** | **Boolean**| If the \&quot;spatialKeys\&quot; flag is set, the response will also contain a proprietary geospatial keys for a specified location. | [optional] [default to false]
 **heading** | **Number**| The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.) | [optional] 
 **radius** | **Number**| The maximum distance in meters from the specified position for the reverse geocoder to consider. | [optional] [default to 10000]
 **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## searchVersionNumberReverseGeocodePositionExtGet

> searchVersionNumberReverseGeocodePositionExtGet(versionNumber, position, ext, opts)

Reverse Geocode

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.ReverseGeocodingApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let position = "37.8328,-122.27669"; // String | This is specified as a comma separated string composed of lat., lon.
let ext = "xml"; // String | Expected response format.
let opts = {
  'spatialKeys': false, // Boolean | If the \"spatialKeys\" flag is set, the response will also contain a proprietary geospatial keys for a specified location.
  'returnSpeedLimit': false, // Boolean | To enable return of the posted speed limit (where available).
  'heading': 3.4, // Number | The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.)
  'radius': 10000, // Number | The maximum distance in meters from the specified position for the reverse geocoder to consider.
  'number': "number_example", // String | If a number is sent in along with the request, the response may include the side of the street (Left/Right) and an offset position for that number.
  'returnRoadUse': false, // Boolean | Enables return of the road use array for reverse geocodes at street level.
  'roadUse': "roadUse_example", // String | Restricts reverse geocodes to a certain type of road use. The road use array for reverse geocodes can be one or more of: [\"LimitedAccess\", \"Arterial\", \"Terminal\", \"Ramp\", \"Rotary\", \"LocalStreet\"].
  'callback': "'cb'" // String | Specifies the jsonp callback method.
};
apiInstance.searchVersionNumberReverseGeocodePositionExtGet(versionNumber, position, ext, opts, (error, data, response) => {
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
 **ext** | **String**| Expected response format. | 
 **spatialKeys** | **Boolean**| If the \&quot;spatialKeys\&quot; flag is set, the response will also contain a proprietary geospatial keys for a specified location. | [optional] [default to false]
 **returnSpeedLimit** | **Boolean**| To enable return of the posted speed limit (where available). | [optional] [default to false]
 **heading** | **Number**| The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.) | [optional] 
 **radius** | **Number**| The maximum distance in meters from the specified position for the reverse geocoder to consider. | [optional] [default to 10000]
 **number** | **String**| If a number is sent in along with the request, the response may include the side of the street (Left/Right) and an offset position for that number. | [optional] 
 **returnRoadUse** | **Boolean**| Enables return of the road use array for reverse geocodes at street level. | [optional] [default to false]
 **roadUse** | **String**| Restricts reverse geocodes to a certain type of road use. The road use array for reverse geocodes can be one or more of: [\&quot;LimitedAccess\&quot;, \&quot;Arterial\&quot;, \&quot;Terminal\&quot;, \&quot;Ramp\&quot;, \&quot;Rotary\&quot;, \&quot;LocalStreet\&quot;]. | [optional] 
 **callback** | **String**| Specifies the jsonp callback method. | [optional] [default to &#39;cb&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

