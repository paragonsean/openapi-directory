# Gitlab.ApplicationApi

All URIs are relative to *https://gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getV3ApplicationSettings**](ApplicationApi.md#getV3ApplicationSettings) | **GET** /v3/application/settings | Get the current application settings
[**putV3ApplicationSettings**](ApplicationApi.md#putV3ApplicationSettings) | **PUT** /v3/application/settings | Modify application settings



## getV3ApplicationSettings

> ApplicationSetting getV3ApplicationSettings()

Get the current application settings

Get the current application settings

### Example

```javascript
import Gitlab from 'gitlab';
let defaultClient = Gitlab.ApiClient.instance;
// Configure API key authorization: private_token_query
let private_token_query = defaultClient.authentications['private_token_query'];
private_token_query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_token_query.apiKeyPrefix = 'Token';
// Configure API key authorization: private_token_header
let private_token_header = defaultClient.authentications['private_token_header'];
private_token_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_token_header.apiKeyPrefix = 'Token';

let apiInstance = new Gitlab.ApplicationApi();
apiInstance.getV3ApplicationSettings((error, data, response) => {
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

[**ApplicationSetting**](ApplicationSetting.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putV3ApplicationSettings

> ApplicationSetting putV3ApplicationSettings(putV3ApplicationSettingsRequest)

Modify application settings

Modify application settings

### Example

```javascript
import Gitlab from 'gitlab';
let defaultClient = Gitlab.ApiClient.instance;
// Configure API key authorization: private_token_query
let private_token_query = defaultClient.authentications['private_token_query'];
private_token_query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_token_query.apiKeyPrefix = 'Token';
// Configure API key authorization: private_token_header
let private_token_header = defaultClient.authentications['private_token_header'];
private_token_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_token_header.apiKeyPrefix = 'Token';

let apiInstance = new Gitlab.ApplicationApi();
let putV3ApplicationSettingsRequest = new Gitlab.PutV3ApplicationSettingsRequest(); // PutV3ApplicationSettingsRequest | 
apiInstance.putV3ApplicationSettings(putV3ApplicationSettingsRequest, (error, data, response) => {
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
 **putV3ApplicationSettingsRequest** | [**PutV3ApplicationSettingsRequest**](PutV3ApplicationSettingsRequest.md)|  | 

### Return type

[**ApplicationSetting**](ApplicationSetting.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

