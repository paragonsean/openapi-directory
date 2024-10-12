# DeepArtEffects.DefaultApi

All URIs are relative to *https://api.deeparteffects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**noauthResultGet**](DefaultApi.md#noauthResultGet) | **GET** /noauth/result | 
[**noauthStylesGet**](DefaultApi.md#noauthStylesGet) | **GET** /noauth/styles | 
[**noauthUploadPost**](DefaultApi.md#noauthUploadPost) | **POST** /noauth/upload | 



## noauthResultGet

> Result noauthResultGet(opts)



### Example

```javascript
import DeepArtEffects from 'deep_art_effects';
let defaultClient = DeepArtEffects.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new DeepArtEffects.DefaultApi();
let opts = {
  'submissionId': "submissionId_example" // String | 
};
apiInstance.noauthResultGet(opts, (error, data, response) => {
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
 **submissionId** | **String**|  | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## noauthStylesGet

> Styles noauthStylesGet()



### Example

```javascript
import DeepArtEffects from 'deep_art_effects';
let defaultClient = DeepArtEffects.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new DeepArtEffects.DefaultApi();
apiInstance.noauthStylesGet((error, data, response) => {
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

[**Styles**](Styles.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## noauthUploadPost

> UploadResponse noauthUploadPost(uploadRequest)



### Example

```javascript
import DeepArtEffects from 'deep_art_effects';
let defaultClient = DeepArtEffects.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new DeepArtEffects.DefaultApi();
let uploadRequest = new DeepArtEffects.UploadRequest(); // UploadRequest | 
apiInstance.noauthUploadPost(uploadRequest, (error, data, response) => {
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
 **uploadRequest** | [**UploadRequest**](UploadRequest.md)|  | 

### Return type

[**UploadResponse**](UploadResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

