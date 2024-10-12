# QnAMakerClient.EndpointKeysApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpointKeysRefreshKeys**](EndpointKeysApi.md#endpointKeysRefreshKeys) | **PATCH** /endpointkeys/{keyType} | Re-generates an endpoint key.
[**endpointSettingsUpdateSettings**](EndpointKeysApi.md#endpointSettingsUpdateSettings) | **PATCH** /endpointSettings | Updates endpoint settings for an endpoint.



## endpointKeysRefreshKeys

> EndpointKeysDTO endpointKeysRefreshKeys(keyType)

Re-generates an endpoint key.

### Example

```javascript
import QnAMakerClient from 'qn_a_maker_client';
let defaultClient = QnAMakerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerClient.EndpointKeysApi();
let keyType = "keyType_example"; // String | Type of Key
apiInstance.endpointKeysRefreshKeys(keyType, (error, data, response) => {
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
 **keyType** | **String**| Type of Key | 

### Return type

[**EndpointKeysDTO**](EndpointKeysDTO.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## endpointSettingsUpdateSettings

> String endpointSettingsUpdateSettings(endpointSettingsPayload)

Updates endpoint settings for an endpoint.

### Example

```javascript
import QnAMakerClient from 'qn_a_maker_client';
let defaultClient = QnAMakerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerClient.EndpointKeysApi();
let endpointSettingsPayload = new QnAMakerClient.EndpointSettingsDTO(); // EndpointSettingsDTO | Post body of the request.
apiInstance.endpointSettingsUpdateSettings(endpointSettingsPayload, (error, data, response) => {
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
 **endpointSettingsPayload** | [**EndpointSettingsDTO**](EndpointSettingsDTO.md)| Post body of the request. | 

### Return type

**String**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

