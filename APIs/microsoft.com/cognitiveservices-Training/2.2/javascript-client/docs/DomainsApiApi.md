# CustomVisionTrainingClient.DomainsApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v2.2/Training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDomain**](DomainsApiApi.md#getDomain) | **GET** /domains/{domainId} | Get information about a specific domain.
[**getDomains**](DomainsApiApi.md#getDomains) | **GET** /domains | Get a list of the available domains.



## getDomain

> Domain getDomain(domainId, trainingKey)

Get information about a specific domain.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';

let apiInstance = new CustomVisionTrainingClient.DomainsApiApi();
let domainId = "b30a91ae-e3c1-4f73-a81e-c270bff27c39"; // String | The id of the domain to get information about.
let trainingKey = "{API Key}"; // String | 
apiInstance.getDomain(domainId, trainingKey, (error, data, response) => {
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
 **trainingKey** | **String**|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getDomains

> [Domain] getDomains(trainingKey)

Get a list of the available domains.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';

let apiInstance = new CustomVisionTrainingClient.DomainsApiApi();
let trainingKey = "{API Key}"; // String | 
apiInstance.getDomains(trainingKey, (error, data, response) => {
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
 **trainingKey** | **String**|  | 

### Return type

[**[Domain]**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

