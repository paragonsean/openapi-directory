# ApiManagementClient.RevisionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiRevisionsList**](RevisionsApi.md#apiRevisionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/revisions | 



## apiRevisionsList

> ApiRevisionCollection apiRevisionsList(resourceGroupName, serviceName, apiVersion, subscriptionId, apiId, opts)



Lists all revisions of an API.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.RevisionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
let opts = {
  'filter': "filter_example", // String | | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |apiRevision | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| 
  'top': 56, // Number | Number of records to return.
  'skip': 56 // Number | Number of records to skip.
};
apiInstance.apiRevisionsList(resourceGroupName, serviceName, apiVersion, subscriptionId, apiId, opts, (error, data, response) => {
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
 **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | 
 **filter** | **String**| | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |apiRevision | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith|  | [optional] 
 **top** | **Number**| Number of records to return. | [optional] 
 **skip** | **Number**| Number of records to skip. | [optional] 

### Return type

[**ApiRevisionCollection**](ApiRevisionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

