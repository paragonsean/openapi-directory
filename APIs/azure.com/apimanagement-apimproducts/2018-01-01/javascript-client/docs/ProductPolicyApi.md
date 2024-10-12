# ApiManagementClient.ProductPolicyApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productPolicyCreateOrUpdate**](ProductPolicyApi.md#productPolicyCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/policies/{policyId} | 
[**productPolicyDelete**](ProductPolicyApi.md#productPolicyDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/policies/{policyId} | 
[**productPolicyGet**](ProductPolicyApi.md#productPolicyGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/policies/{policyId} | 
[**productPolicyGetEntityTag**](ProductPolicyApi.md#productPolicyGetEntityTag) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/policies/{policyId} | 
[**productPolicyListByProduct**](ProductPolicyApi.md#productPolicyListByProduct) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/policies | 



## productPolicyCreateOrUpdate

> ProductPolicyGet200Response productPolicyCreateOrUpdate(resourceGroupName, serviceName, productId, policyId, apiVersion, subscriptionId, parameters, opts)



Creates or updates policy configuration for the Product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductPolicyApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let policyId = "policyId_example"; // String | The identifier of the Policy.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ApiManagementClient.ProductPolicyGet200Response(); // ProductPolicyGet200Response | The policy contents to apply.
let opts = {
  'ifMatch': "ifMatch_example" // String | ETag of the Entity. Not required when creating an entity, but required when updating an entity.
};
apiInstance.productPolicyCreateOrUpdate(resourceGroupName, serviceName, productId, policyId, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **policyId** | **String**| The identifier of the Policy. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ProductPolicyGet200Response**](ProductPolicyGet200Response.md)| The policy contents to apply. | 
 **ifMatch** | **String**| ETag of the Entity. Not required when creating an entity, but required when updating an entity. | [optional] 

### Return type

[**ProductPolicyGet200Response**](ProductPolicyGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productPolicyDelete

> productPolicyDelete(resourceGroupName, serviceName, productId, policyId, ifMatch, apiVersion, subscriptionId)



Deletes the policy configuration at the Product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductPolicyApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let policyId = "policyId_example"; // String | The identifier of the Policy.
let ifMatch = "ifMatch_example"; // String | ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.productPolicyDelete(resourceGroupName, serviceName, productId, policyId, ifMatch, apiVersion, subscriptionId, (error, data, response) => {
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
 **policyId** | **String**| The identifier of the Policy. | 
 **ifMatch** | **String**| ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productPolicyGet

> ProductPolicyGet200Response productPolicyGet(resourceGroupName, serviceName, apiVersion, subscriptionId, productId, policyId)



Get the policy configuration at the Product level.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductPolicyApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let policyId = "policyId_example"; // String | The identifier of the Policy.
apiInstance.productPolicyGet(resourceGroupName, serviceName, apiVersion, subscriptionId, productId, policyId, (error, data, response) => {
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
 **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | 
 **policyId** | **String**| The identifier of the Policy. | 

### Return type

[**ProductPolicyGet200Response**](ProductPolicyGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productPolicyGetEntityTag

> productPolicyGetEntityTag(resourceGroupName, serviceName, apiVersion, subscriptionId, productId, policyId)



Get the ETag of the policy configuration at the Product level.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductPolicyApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let policyId = "policyId_example"; // String | The identifier of the Policy.
apiInstance.productPolicyGetEntityTag(resourceGroupName, serviceName, apiVersion, subscriptionId, productId, policyId, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | 
 **policyId** | **String**| The identifier of the Policy. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productPolicyListByProduct

> ProductPolicyListByProduct200Response productPolicyListByProduct(resourceGroupName, serviceName, apiVersion, subscriptionId, productId)



Get the policy configuration at the Product level.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ProductPolicyApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
apiInstance.productPolicyListByProduct(resourceGroupName, serviceName, apiVersion, subscriptionId, productId, (error, data, response) => {
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
 **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | 

### Return type

[**ProductPolicyListByProduct200Response**](ProductPolicyListByProduct200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

