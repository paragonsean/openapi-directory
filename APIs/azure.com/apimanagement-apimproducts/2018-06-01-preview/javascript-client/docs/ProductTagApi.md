# ApiManagementClient.ProductTagApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tagAssignToProduct**](ProductTagApi.md#tagAssignToProduct) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/tags/{tagId} | 
[**tagDetachFromProduct**](ProductTagApi.md#tagDetachFromProduct) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/tags/{tagId} | 
[**tagGetByProduct**](ProductTagApi.md#tagGetByProduct) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/tags/{tagId} | 
[**tagGetEntityStateByProduct**](ProductTagApi.md#tagGetEntityStateByProduct) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/tags/{tagId} | 
[**tagListByProduct**](ProductTagApi.md#tagListByProduct) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/tags | 



## tagAssignToProduct

> TagGetByProduct200Response tagAssignToProduct(resourceGroupName, serviceName, productId, tagId, apiVersion, subscriptionId)



Assign tag to the Product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductTagApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let tagId = "tagId_example"; // String | Tag identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.tagAssignToProduct(resourceGroupName, serviceName, productId, tagId, apiVersion, subscriptionId, (error, data, response) => {
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
 **tagId** | **String**| Tag identifier. Must be unique in the current API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**TagGetByProduct200Response**](TagGetByProduct200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagDetachFromProduct

> tagDetachFromProduct(resourceGroupName, serviceName, productId, tagId, apiVersion, subscriptionId)



Detach the tag from the Product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductTagApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let tagId = "tagId_example"; // String | Tag identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.tagDetachFromProduct(resourceGroupName, serviceName, productId, tagId, apiVersion, subscriptionId, (error, data, response) => {
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
 **tagId** | **String**| Tag identifier. Must be unique in the current API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagGetByProduct

> TagGetByProduct200Response tagGetByProduct(resourceGroupName, serviceName, productId, tagId, apiVersion, subscriptionId)



Get tag associated with the Product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductTagApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let tagId = "tagId_example"; // String | Tag identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.tagGetByProduct(resourceGroupName, serviceName, productId, tagId, apiVersion, subscriptionId, (error, data, response) => {
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
 **tagId** | **String**| Tag identifier. Must be unique in the current API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**TagGetByProduct200Response**](TagGetByProduct200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagGetEntityStateByProduct

> tagGetEntityStateByProduct(resourceGroupName, serviceName, productId, tagId, apiVersion, subscriptionId)



Gets the entity state version of the tag specified by its identifier.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductTagApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let tagId = "tagId_example"; // String | Tag identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.tagGetEntityStateByProduct(resourceGroupName, serviceName, productId, tagId, apiVersion, subscriptionId, (error, data, response) => {
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
 **tagId** | **String**| Tag identifier. Must be unique in the current API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagListByProduct

> TagListByProduct200Response tagListByProduct(resourceGroupName, serviceName, productId, apiVersion, subscriptionId, opts)



Lists all Tags associated with the Product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductTagApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |displayName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| 
  'top': 56, // Number | Number of records to return.
  'skip': 56 // Number | Number of records to skip.
};
apiInstance.tagListByProduct(resourceGroupName, serviceName, productId, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **filter** | **String**| | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |displayName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith|  | [optional] 
 **top** | **Number**| Number of records to return. | [optional] 
 **skip** | **Number**| Number of records to skip. | [optional] 

### Return type

[**TagListByProduct200Response**](TagListByProduct200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

