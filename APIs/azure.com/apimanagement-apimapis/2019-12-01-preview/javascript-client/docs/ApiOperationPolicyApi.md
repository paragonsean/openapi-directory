# ApiManagementClient.ApiOperationPolicyApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiOperationPolicyCreateOrUpdate**](ApiOperationPolicyApi.md#apiOperationPolicyCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/policies/{policyId} | 
[**apiOperationPolicyDelete**](ApiOperationPolicyApi.md#apiOperationPolicyDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/policies/{policyId} | 
[**apiOperationPolicyGet**](ApiOperationPolicyApi.md#apiOperationPolicyGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/policies/{policyId} | 
[**apiOperationPolicyGetEntityTag**](ApiOperationPolicyApi.md#apiOperationPolicyGetEntityTag) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/policies/{policyId} | 
[**apiOperationPolicyListByOperation**](ApiOperationPolicyApi.md#apiOperationPolicyListByOperation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/policies | 



## apiOperationPolicyCreateOrUpdate

> ApiOperationPolicyGet200Response apiOperationPolicyCreateOrUpdate(resourceGroupName, serviceName, apiId, operationId, policyId, apiVersion, subscriptionId, parameters, opts)



Creates or updates policy configuration for the API Operation level.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiOperationPolicyApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
let operationId = "operationId_example"; // String | Operation identifier within an API. Must be unique in the current API Management service instance.
let policyId = "policyId_example"; // String | The identifier of the Policy.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ApiManagementClient.ApiOperationPolicyGet200Response(); // ApiOperationPolicyGet200Response | The policy contents to apply.
let opts = {
  'ifMatch': "ifMatch_example" // String | ETag of the Entity. Not required when creating an entity, but required when updating an entity.
};
apiInstance.apiOperationPolicyCreateOrUpdate(resourceGroupName, serviceName, apiId, operationId, policyId, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **apiId** | **String**| API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number. | 
 **operationId** | **String**| Operation identifier within an API. Must be unique in the current API Management service instance. | 
 **policyId** | **String**| The identifier of the Policy. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ApiOperationPolicyGet200Response**](ApiOperationPolicyGet200Response.md)| The policy contents to apply. | 
 **ifMatch** | **String**| ETag of the Entity. Not required when creating an entity, but required when updating an entity. | [optional] 

### Return type

[**ApiOperationPolicyGet200Response**](ApiOperationPolicyGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiOperationPolicyDelete

> apiOperationPolicyDelete(resourceGroupName, serviceName, apiId, operationId, policyId, ifMatch, apiVersion, subscriptionId)



Deletes the policy configuration at the Api Operation.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiOperationPolicyApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
let operationId = "operationId_example"; // String | Operation identifier within an API. Must be unique in the current API Management service instance.
let policyId = "policyId_example"; // String | The identifier of the Policy.
let ifMatch = "ifMatch_example"; // String | ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.apiOperationPolicyDelete(resourceGroupName, serviceName, apiId, operationId, policyId, ifMatch, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiId** | **String**| API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number. | 
 **operationId** | **String**| Operation identifier within an API. Must be unique in the current API Management service instance. | 
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


## apiOperationPolicyGet

> ApiOperationPolicyGet200Response apiOperationPolicyGet(resourceGroupName, serviceName, apiId, operationId, policyId, apiVersion, subscriptionId, opts)



Get the policy configuration at the API Operation level.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiOperationPolicyApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
let operationId = "operationId_example"; // String | Operation identifier within an API. Must be unique in the current API Management service instance.
let policyId = "policyId_example"; // String | The identifier of the Policy.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'format': "'xml'" // String | Policy Export Format.
};
apiInstance.apiOperationPolicyGet(resourceGroupName, serviceName, apiId, operationId, policyId, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiId** | **String**| API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number. | 
 **operationId** | **String**| Operation identifier within an API. Must be unique in the current API Management service instance. | 
 **policyId** | **String**| The identifier of the Policy. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **format** | **String**| Policy Export Format. | [optional] [default to &#39;xml&#39;]

### Return type

[**ApiOperationPolicyGet200Response**](ApiOperationPolicyGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiOperationPolicyGetEntityTag

> apiOperationPolicyGetEntityTag(resourceGroupName, serviceName, apiId, operationId, policyId, apiVersion, subscriptionId)



Gets the entity state (Etag) version of the API operation policy specified by its identifier.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiOperationPolicyApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
let operationId = "operationId_example"; // String | Operation identifier within an API. Must be unique in the current API Management service instance.
let policyId = "policyId_example"; // String | The identifier of the Policy.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.apiOperationPolicyGetEntityTag(resourceGroupName, serviceName, apiId, operationId, policyId, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiId** | **String**| API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number. | 
 **operationId** | **String**| Operation identifier within an API. Must be unique in the current API Management service instance. | 
 **policyId** | **String**| The identifier of the Policy. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiOperationPolicyListByOperation

> ApiOperationPolicyListByOperation200Response apiOperationPolicyListByOperation(resourceGroupName, serviceName, apiId, operationId, apiVersion, subscriptionId)



Get the list of policy configuration at the API Operation level.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiOperationPolicyApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiId = "apiId_example"; // String | API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
let operationId = "operationId_example"; // String | Operation identifier within an API. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.apiOperationPolicyListByOperation(resourceGroupName, serviceName, apiId, operationId, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiId** | **String**| API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number. | 
 **operationId** | **String**| Operation identifier within an API. Must be unique in the current API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ApiOperationPolicyListByOperation200Response**](ApiOperationPolicyListByOperation200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

