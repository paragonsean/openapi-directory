# InstagramApi.GeographiesApi

All URIs are relative to *https://api.instagram.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geographiesGeoIdMediaRecentGet**](GeographiesApi.md#geographiesGeoIdMediaRecentGet) | **GET** /geographies/{geo-id}/media/recent | Get recent media from a custom geo-id.



## geographiesGeoIdMediaRecentGet

> MediaListResponse geographiesGeoIdMediaRecentGet(geoId, opts)

Get recent media from a custom geo-id.

Get recent media from a geography subscription that you created.  **Note:** You can only access Geographies that were explicitly created by your OAuth client. Check the Geography Subscriptions section of the [real-time updates page](https://instagram.com/developer/realtime/). When you create a subscription to some geography that you define, you will be returned a unique &#x60;geo-id&#x60; that can be used in this query. To backfill photos from the location covered by this geography, use the [media search endpoint](https://instagram.com/developer/endpoints/media/).  **Warning:** [Deprecated](http://instagram.com/developer/changelog/) for Apps created **on or after** Nov 17, 2015 

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

let apiInstance = new InstagramApi.GeographiesApi();
let geoId = "geoId_example"; // String | The geography ID.
let opts = {
  'count': 56, // Number | Max number of media to return.
  'minId': "minId_example" // String | Return media before this `min_id`.
};
apiInstance.geographiesGeoIdMediaRecentGet(geoId, opts, (error, data, response) => {
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
 **geoId** | **String**| The geography ID. | 
 **count** | **Number**| Max number of media to return. | [optional] 
 **minId** | **String**| Return media before this &#x60;min_id&#x60;. | [optional] 

### Return type

[**MediaListResponse**](MediaListResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

