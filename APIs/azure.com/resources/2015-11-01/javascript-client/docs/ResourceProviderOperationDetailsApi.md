# ResourceManagementClient.ResourceProviderOperationDetailsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourceProviderOperationDetailsList**](ResourceProviderOperationDetailsApi.md#resourceProviderOperationDetailsList) | **GET** /providers/{resourceProviderNamespace}/operations | 



## resourceProviderOperationDetailsList

> ResourceProviderOperationDetailListResult resourceProviderOperationDetailsList(resourceProviderNamespace, apiVersion)



Gets a list of resource providers.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourceProviderOperationDetailsApi();
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | Resource identity.
let apiVersion = "apiVersion_example"; // String | 
apiInstance.resourceProviderOperationDetailsList(resourceProviderNamespace, apiVersion, (error, data, response) => {
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
 **resourceProviderNamespace** | **String**| Resource identity. | 
 **apiVersion** | **String**|  | 

### Return type

[**ResourceProviderOperationDetailListResult**](ResourceProviderOperationDetailListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

