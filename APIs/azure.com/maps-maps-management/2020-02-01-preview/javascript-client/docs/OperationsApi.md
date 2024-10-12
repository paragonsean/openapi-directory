# AzureMapsResourceProvider.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mapsListOperations**](OperationsApi.md#mapsListOperations) | **GET** /providers/Microsoft.Maps/operations | 



## mapsListOperations

> MapsOperations mapsListOperations(apiVersion)



List operations available for the Maps Resource Provider

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.OperationsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.mapsListOperations(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**MapsOperations**](MapsOperations.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

