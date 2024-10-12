# CustomVisionTrainingClient.DomainsApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDomain**](DomainsApiApi.md#getDomain) | **GET** /domains/{domainId} | Get information about a specific domain.
[**getDomains**](DomainsApiApi.md#getDomains) | **GET** /domains | Get a list of the available domains.



## getDomain

> Domain getDomain(domainId)

Get information about a specific domain.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.DomainsApiApi();
let domainId = "b30a91ae-e3c1-4f73-a81e-c270bff27c39"; // String | The id of the domain to get information about.
apiInstance.getDomain(domainId, (error, data, response) => {
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
 **domainId** | **String**| The id of the domain to get information about. | 

### Return type

[**Domain**](Domain.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getDomains

> [Domain] getDomains()

Get a list of the available domains.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.DomainsApiApi();
apiInstance.getDomains((error, data, response) => {
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

[**[Domain]**](Domain.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml

