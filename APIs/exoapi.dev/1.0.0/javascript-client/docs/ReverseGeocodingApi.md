# ExoApi.ReverseGeocodingApi

All URIs are relative to *https://api.exoapi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reverseGeocodingGet**](ReverseGeocodingApi.md#reverseGeocodingGet) | **GET** /reverse-geocoding | 



## reverseGeocodingGet

> ReverseGeocodingGet200Response reverseGeocodingGet(lat, lon, opts)



Quickly convert GPS coordinates to human-readable addresses

### Example

```javascript
import ExoApi from 'exo_api';
let defaultClient = ExoApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ExoApi.ReverseGeocodingApi();
let lat = 3.4; // Number | 
let lon = 3.4; // Number | 
let opts = {
  'locale': "locale_example" // String | 
};
apiInstance.reverseGeocodingGet(lat, lon, opts, (error, data, response) => {
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
 **lat** | **Number**|  | 
 **lon** | **Number**|  | 
 **locale** | **String**|  | [optional] 

### Return type

[**ReverseGeocodingGet200Response**](ReverseGeocodingGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

