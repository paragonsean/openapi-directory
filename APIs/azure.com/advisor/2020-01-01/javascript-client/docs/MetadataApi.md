# AdvisorManagementClient.MetadataApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recommendationMetadataGet**](MetadataApi.md#recommendationMetadataGet) | **GET** /providers/Microsoft.Advisor/metadata/{name} | Gets the metadata entity.
[**recommendationMetadataList**](MetadataApi.md#recommendationMetadataList) | **GET** /providers/Microsoft.Advisor/metadata | Gets the list of metadata entities.



## recommendationMetadataGet

> MetadataEntity recommendationMetadataGet(name, apiVersion)

Gets the metadata entity.

### Example

```javascript
import AdvisorManagementClient from 'advisor_management_client';
let defaultClient = AdvisorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdvisorManagementClient.MetadataApi();
let name = "name_example"; // String | Name of metadata entity.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.recommendationMetadataGet(name, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of metadata entity. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**MetadataEntity**](MetadataEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationMetadataList

> MetadataEntityListResult recommendationMetadataList(apiVersion)

Gets the list of metadata entities.

### Example

```javascript
import AdvisorManagementClient from 'advisor_management_client';
let defaultClient = AdvisorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdvisorManagementClient.MetadataApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.recommendationMetadataList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**MetadataEntityListResult**](MetadataEntityListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

