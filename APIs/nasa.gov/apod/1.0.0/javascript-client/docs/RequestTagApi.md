# Apod.RequestTagApi

All URIs are relative to *https://api.nasa.gov/planetary*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apodGet**](RequestTagApi.md#apodGet) | **GET** /apod | Returns images



## apodGet

> [Object] apodGet(opts)

Returns images

Returns the picture of the day

### Example

```javascript
import Apod from 'apod';
let defaultClient = Apod.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Apod.RequestTagApi();
let opts = {
  'date': "date_example", // String | The date of the APOD image to retrieve
  'hd': true // Boolean | Retrieve the URL for the high resolution image
};
apiInstance.apodGet(opts, (error, data, response) => {
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
 **date** | **String**| The date of the APOD image to retrieve | [optional] 
 **hd** | **Boolean**| Retrieve the URL for the high resolution image | [optional] 

### Return type

**[Object]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

