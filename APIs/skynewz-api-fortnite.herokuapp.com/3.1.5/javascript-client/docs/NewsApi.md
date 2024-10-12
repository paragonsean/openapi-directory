# FortniteRestApi.NewsApi

All URIs are relative to *https://skynewz-api-fortnite.herokuapp.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**newsGet**](NewsApi.md#newsGet) | **GET** /news | Get Fortnite News



## newsGet

> NewsGet200Response newsGet()

Get Fortnite News

### Example

```javascript
import FortniteRestApi from 'fortnite_rest_api';
let defaultClient = FortniteRestApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new FortniteRestApi.NewsApi();
apiInstance.newsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**NewsGet200Response**](NewsGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

