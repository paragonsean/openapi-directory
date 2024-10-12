# FlinksterApiNg.ProvidernetworksApi

All URIs are relative to *https://api.deutschebahn.com/flinkster-api-ng/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProviderNetwork**](ProvidernetworksApi.md#getProviderNetwork) | **GET** /providernetworks/{uid} | Get information about the ProviderNetworkResources.



## getProviderNetwork

> RentalObjectJO getProviderNetwork(uid)

Get information about the ProviderNetworkResources.

Get information about the ProviderNetworkResources. 

### Example

```javascript
import FlinksterApiNg from 'flinkster_api_ng';

let apiInstance = new FlinksterApiNg.ProvidernetworksApi();
let uid = "uid_example"; // String | 
apiInstance.getProviderNetwork(uid, (error, data, response) => {
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
 **uid** | **String**|  | 

### Return type

[**RentalObjectJO**](RentalObjectJO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

