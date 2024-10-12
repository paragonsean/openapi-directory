# ApiManagementClient.ProductsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsCreateOrUpdate**](ProductsApi.md#productsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId} | 
[**productsDelete**](ProductsApi.md#productsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId} | 
[**productsGet**](ProductsApi.md#productsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId} | 
[**productsListByService**](ProductsApi.md#productsListByService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products | 
[**productsUpdate**](ProductsApi.md#productsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId} | 



## productsCreateOrUpdate

> productsCreateOrUpdate(resourceGroupName, serviceName, productId, apiVersion, subscriptionId, parameters)



Creates or Updates a product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ApiManagementClient.ProductContract(); // ProductContract | Create or update parameters.
apiInstance.productsCreateOrUpdate(resourceGroupName, serviceName, productId, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ProductContract**](ProductContract.md)| Create or update parameters. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsDelete

> productsDelete(resourceGroupName, serviceName, productId, ifMatch, apiVersion, subscriptionId, opts)



Delete product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let ifMatch = "ifMatch_example"; // String | ETag of the Product Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'deleteSubscriptions': true // Boolean | Delete existing subscriptions to the product or not.
};
apiInstance.productsDelete(resourceGroupName, serviceName, productId, ifMatch, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **ifMatch** | **String**| ETag of the Product Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **deleteSubscriptions** | **Boolean**| Delete existing subscriptions to the product or not. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsGet

> ProductContract productsGet(resourceGroupName, serviceName, productId, apiVersion, subscriptionId)



Gets the details of the product specified by its identifier.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.productsGet(resourceGroupName, serviceName, productId, apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**ProductContract**](ProductContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsListByService

> ProductCollection productsListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, opts)



Lists a collection of products in the specified service instance.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | terms       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state       | eq                     |                                             |
  'top': 56, // Number | Number of records to return.
  'skip': 56, // Number | Number of records to skip.
  'expandGroups': true // Boolean | When set to true, the response contains an array of groups that have visibility to the product. The default is false.
};
apiInstance.productsListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **filter** | **String**| | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | terms       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state       | eq                     |                                             | | [optional] 
 **top** | **Number**| Number of records to return. | [optional] 
 **skip** | **Number**| Number of records to skip. | [optional] 
 **expandGroups** | **Boolean**| When set to true, the response contains an array of groups that have visibility to the product. The default is false. | [optional] 

### Return type

[**ProductCollection**](ProductCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsUpdate

> productsUpdate(resourceGroupName, serviceName, productId, ifMatch, apiVersion, subscriptionId, parameters)



Update product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let ifMatch = "ifMatch_example"; // String | ETag of the Product Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ApiManagementClient.ProductUpdateParameters(); // ProductUpdateParameters | Update parameters.
apiInstance.productsUpdate(resourceGroupName, serviceName, productId, ifMatch, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **ifMatch** | **String**| ETag of the Product Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ProductUpdateParameters**](ProductUpdateParameters.md)| Update parameters. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

