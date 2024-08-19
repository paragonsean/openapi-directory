# InstagramApi.LocationsApi

All URIs are relative to *https://api.instagram.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locationsLocationIdGet**](LocationsApi.md#locationsLocationIdGet) | **GET** /locations/{location-id} | Get information about a location.
[**locationsLocationIdMediaRecentGet**](LocationsApi.md#locationsLocationIdMediaRecentGet) | **GET** /locations/{location-id}/media/recent | Get a list of recent media objects from a given location.
[**locationsSearchGet**](LocationsApi.md#locationsSearchGet) | **GET** /locations/search | Search for a location by geographic coordinate.



## locationsLocationIdGet

> LocationInfoResponse locationsLocationIdGet(locationId)

Get information about a location.

Get information about a location.

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.LocationsApi();
let locationId = "locationId_example"; // String | The location ID.
apiInstance.locationsLocationIdGet(locationId, (error, data, response) => {
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
 **locationId** | **String**| The location ID. | 

### Return type

[**LocationInfoResponse**](LocationInfoResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locationsLocationIdMediaRecentGet

> MediaListResponse locationsLocationIdMediaRecentGet(locationId, opts)

Get a list of recent media objects from a given location.

Get a list of recent media objects from a given location.

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.LocationsApi();
let locationId = "locationId_example"; // String | The location ID.
let opts = {
  'minTimestamp': 789, // Number | Return media after this UNIX timestamp.
  'maxTimestamp': 789, // Number | Return media before this UNIX timestamp.
  'minId': "minId_example", // String | Return media before this `min_id`.
  'maxId': "maxId_example" // String | Return media after this `max_id`.
};
apiInstance.locationsLocationIdMediaRecentGet(locationId, opts, (error, data, response) => {
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
 **locationId** | **String**| The location ID. | 
 **minTimestamp** | **Number**| Return media after this UNIX timestamp. | [optional] 
 **maxTimestamp** | **Number**| Return media before this UNIX timestamp. | [optional] 
 **minId** | **String**| Return media before this &#x60;min_id&#x60;. | [optional] 
 **maxId** | **String**| Return media after this &#x60;max_id&#x60;. | [optional] 

### Return type

[**MediaListResponse**](MediaListResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locationsSearchGet

> LocationSearchResponse locationsSearchGet(opts)

Search for a location by geographic coordinate.

Search for a location by geographic coordinate.

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.LocationsApi();
let opts = {
  'distance': 56, // Number | Default is 1000m (distance=1000), max distance is 5000.
  'facebookPlacesId': "facebookPlacesId_example", // String | Returns a location mapped off of a Facebook places id. If used, a Foursquare id and `lat`, `lng` are not required.
  'foursquareId': "foursquareId_example", // String | Returns a location mapped off of a foursquare v1 api location id. If used, you are not required to use `lat` and `lng`. Note that this method is deprecated; you should use the new foursquare IDs with V2 of their API. 
  'lat': 3.4, // Number | Latitude of the center search coordinate. If used, `lng` is required.
  'lng': 3.4, // Number | Longitude of the center search coordinate. If used, `lat` is required.
  'foursquareV2Id': "foursquareV2Id_example" // String | Returns a location mapped off of a foursquare v2 api location id. If used, you are not required to use `lat` and `lng`. 
};
apiInstance.locationsSearchGet(opts, (error, data, response) => {
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
 **distance** | **Number**| Default is 1000m (distance&#x3D;1000), max distance is 5000. | [optional] 
 **facebookPlacesId** | **String**| Returns a location mapped off of a Facebook places id. If used, a Foursquare id and &#x60;lat&#x60;, &#x60;lng&#x60; are not required. | [optional] 
 **foursquareId** | **String**| Returns a location mapped off of a foursquare v1 api location id. If used, you are not required to use &#x60;lat&#x60; and &#x60;lng&#x60;. Note that this method is deprecated; you should use the new foursquare IDs with V2 of their API.  | [optional] 
 **lat** | **Number**| Latitude of the center search coordinate. If used, &#x60;lng&#x60; is required. | [optional] 
 **lng** | **Number**| Longitude of the center search coordinate. If used, &#x60;lat&#x60; is required. | [optional] 
 **foursquareV2Id** | **String**| Returns a location mapped off of a foursquare v2 api location id. If used, you are not required to use &#x60;lat&#x60; and &#x60;lng&#x60;.  | [optional] 

### Return type

[**LocationSearchResponse**](LocationSearchResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

