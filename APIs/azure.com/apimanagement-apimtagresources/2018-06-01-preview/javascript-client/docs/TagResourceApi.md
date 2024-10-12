# ApiManagementClient.TagResourceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tagResourceListByService**](TagResourceApi.md#tagResourceListByService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tagResources | 



## tagResourceListByService

> TagResourceListByService200Response tagResourceListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, opts)



Lists a collection of resources associated with tags.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.TagResourceApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |aid | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |displayName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |apiName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |apiRevision | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |path | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |serviceUrl | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |method | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |urlTemplate | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |terms | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |state | eq |    | |isCurrent | eq |    | 
  'top': 56, // Number | Number of records to return.
  'skip': 56 // Number | Number of records to skip.
};
apiInstance.tagResourceListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |aid | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |displayName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |apiName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |apiRevision | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |path | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |serviceUrl | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |method | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |urlTemplate | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |terms | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |state | eq |    | |isCurrent | eq |    |  | [optional] 
 **top** | **Number**| Number of records to return. | [optional] 
 **skip** | **Number**| Number of records to skip. | [optional] 

### Return type

[**TagResourceListByService200Response**](TagResourceListByService200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

