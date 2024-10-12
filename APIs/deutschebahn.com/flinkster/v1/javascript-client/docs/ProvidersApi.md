# FlinksterApiNg.ProvidersApi

All URIs are relative to *https://api.deutschebahn.com/flinkster-api-ng/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProvider**](ProvidersApi.md#getProvider) | **GET** /providers/{uid} | Get information about the ProviderResourceImpl.



## getProvider

> RentalObjectJO getProvider(uid)

Get information about the ProviderResourceImpl.

Get information about the ProviderResourcesCtrl. 

### Example

```javascript
import FlinksterApiNg from 'flinkster_api_ng';

let apiInstance = new FlinksterApiNg.ProvidersApi();
let uid = "uid_example"; // String | 
apiInstance.getProvider(uid, (error, data, response) => {
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

