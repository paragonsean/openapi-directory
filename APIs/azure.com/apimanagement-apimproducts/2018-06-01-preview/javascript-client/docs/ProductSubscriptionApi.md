# ApiManagementClient.ProductSubscriptionApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productSubscriptionsList**](ProductSubscriptionApi.md#productSubscriptionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/subscriptions | 



## productSubscriptionsList

> ProductSubscriptionsList200Response productSubscriptionsList(resourceGroupName, serviceName, productId, apiVersion, subscriptionId, opts)



Lists the collection of subscriptions to the specified product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductSubscriptionApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |displayName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |stateComment | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |ownerId | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |scope | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |userId | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |productId | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |state | eq |    | |user |     |    | 
  'top': 56, // Number | Number of records to return.
  'skip': 56 // Number | Number of records to skip.
};
apiInstance.productSubscriptionsList(resourceGroupName, serviceName, productId, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |displayName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |stateComment | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |ownerId | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |scope | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |userId | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |productId | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |state | eq |    | |user |     |    |  | [optional] 
 **top** | **Number**| Number of records to return. | [optional] 
 **skip** | **Number**| Number of records to skip. | [optional] 

### Return type

[**ProductSubscriptionsList200Response**](ProductSubscriptionsList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

