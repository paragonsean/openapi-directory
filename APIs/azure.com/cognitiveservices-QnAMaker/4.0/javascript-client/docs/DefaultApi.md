# QnAMakerClient.DefaultApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpointKeysGetKeys**](DefaultApi.md#endpointKeysGetKeys) | **GET** /endpointkeys | Gets endpoint keys for an endpoint
[**endpointSettingsGetSettings**](DefaultApi.md#endpointSettingsGetSettings) | **GET** /endpointSettings | Gets endpoint settings for an endpoint.



## endpointKeysGetKeys

> EndpointKeysDTO endpointKeysGetKeys()

Gets endpoint keys for an endpoint

### Example

```javascript
import QnAMakerClient from 'qn_a_maker_client';
let defaultClient = QnAMakerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerClient.DefaultApi();
apiInstance.endpointKeysGetKeys((error, data, response) => {
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

[**EndpointKeysDTO**](EndpointKeysDTO.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## endpointSettingsGetSettings

> EndpointSettingsDTO endpointSettingsGetSettings()

Gets endpoint settings for an endpoint.

### Example

```javascript
import QnAMakerClient from 'qn_a_maker_client';
let defaultClient = QnAMakerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerClient.DefaultApi();
apiInstance.endpointSettingsGetSettings((error, data, response) => {
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

[**EndpointSettingsDTO**](EndpointSettingsDTO.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

