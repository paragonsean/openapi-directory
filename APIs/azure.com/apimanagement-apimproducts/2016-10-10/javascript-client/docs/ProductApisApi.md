# ApiManagementClient.ProductApisApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productApisCreate**](ProductApisApi.md#productApisCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/apis/{apiId} | 
[**productApisDelete**](ProductApisApi.md#productApisDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/apis/{apiId} | 
[**productApisListByProducts**](ProductApisApi.md#productApisListByProducts) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/apis | 



## productApisCreate

> productApisCreate(resourceGroupName, serviceName, productId, apiId, apiVersion, subscriptionId)



Adds an API to the specified product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductApisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.productApisCreate(resourceGroupName, serviceName, productId, apiId, apiVersion, subscriptionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | 
 **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productApisDelete

> productApisDelete(resourceGroupName, serviceName, productId, apiId, apiVersion, subscriptionId)



Deletes the specified API from the specified product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductApisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.productApisDelete(resourceGroupName, serviceName, productId, apiId, apiVersion, subscriptionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | 
 **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productApisListByProducts

> ProductApisListByProducts200Response productApisListByProducts(resourceGroupName, serviceName, productId, apiVersion, subscriptionId, opts)



Lists a collection of the APIs associated with a product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductApisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | serviceUrl  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | path        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | 
  'top': 56, // Number | Number of records to return.
  'skip': 56 // Number | Number of records to skip.
};
apiInstance.productApisListByProducts(resourceGroupName, serviceName, productId, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **filter** | **String**| | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | serviceUrl  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | path        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |  | [optional] 
 **top** | **Number**| Number of records to return. | [optional] 
 **skip** | **Number**| Number of records to skip. | [optional] 

### Return type

[**ProductApisListByProducts200Response**](ProductApisListByProducts200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

