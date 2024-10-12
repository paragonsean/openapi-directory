# ApiManagementClient.ApiOperationsPolicyApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiOperationsPolicyCreateOrUpdate**](ApiOperationsPolicyApi.md#apiOperationsPolicyCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/policy | 
[**apiOperationsPolicyDelete**](ApiOperationsPolicyApi.md#apiOperationsPolicyDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/policy | 
[**apiOperationsPolicyGet**](ApiOperationsPolicyApi.md#apiOperationsPolicyGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/policy | 



## apiOperationsPolicyCreateOrUpdate

> apiOperationsPolicyCreateOrUpdate(resourceGroupName, serviceName, apiId, operationId, ifMatch, apiVersion, subscriptionId, parameters)



Creates or updates policy configuration for the API Operation level.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiOperationsPolicyApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
let operationId = "operationId_example"; // String | Operation identifier within an API. Must be unique in the current API Management service instance.
let ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the Api Operation policy to update. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = {key: null}; // Object | The policy contents to apply.
apiInstance.apiOperationsPolicyCreateOrUpdate(resourceGroupName, serviceName, apiId, operationId, ifMatch, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | 
 **operationId** | **String**| Operation identifier within an API. Must be unique in the current API Management service instance. | 
 **ifMatch** | **String**| The entity state (Etag) version of the Api Operation policy to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | **Object**| The policy contents to apply. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/vnd.ms-azure-apim.policy+xml
- **Accept**: application/json


## apiOperationsPolicyDelete

> apiOperationsPolicyDelete(resourceGroupName, serviceName, apiId, operationId, ifMatch, apiVersion, subscriptionId)



Deletes the policy configuration at the Api Operation.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiOperationsPolicyApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
let operationId = "operationId_example"; // String | Operation identifier within an API. Must be unique in the current API Management service instance.
let ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the Api operation policy to update. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.apiOperationsPolicyDelete(resourceGroupName, serviceName, apiId, operationId, ifMatch, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | 
 **operationId** | **String**| Operation identifier within an API. Must be unique in the current API Management service instance. | 
 **ifMatch** | **String**| The entity state (Etag) version of the Api operation policy to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiOperationsPolicyGet

> File apiOperationsPolicyGet(resourceGroupName, serviceName, apiId, operationId, apiVersion, subscriptionId)



Get the policy configuration at the API Operation level.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiOperationsPolicyApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
let operationId = "operationId_example"; // String | Operation identifier within an API. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.apiOperationsPolicyGet(resourceGroupName, serviceName, apiId, operationId, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | 
 **operationId** | **String**| Operation identifier within an API. Must be unique in the current API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.ms-azure-apim.policy+xml

