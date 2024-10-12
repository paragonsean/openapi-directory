# NetworkManagementClient.ServiceEndpointPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceEndpointPoliciesCreateOrUpdate**](ServiceEndpointPoliciesApi.md#serviceEndpointPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName} | 
[**serviceEndpointPoliciesDelete**](ServiceEndpointPoliciesApi.md#serviceEndpointPoliciesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName} | 
[**serviceEndpointPoliciesGet**](ServiceEndpointPoliciesApi.md#serviceEndpointPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName} | 
[**serviceEndpointPoliciesList**](ServiceEndpointPoliciesApi.md#serviceEndpointPoliciesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/ServiceEndpointPolicies | 
[**serviceEndpointPoliciesListByResourceGroup**](ServiceEndpointPoliciesApi.md#serviceEndpointPoliciesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies | 
[**serviceEndpointPoliciesUpdate**](ServiceEndpointPoliciesApi.md#serviceEndpointPoliciesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName} | 



## serviceEndpointPoliciesCreateOrUpdate

> ServiceEndpointPolicy serviceEndpointPoliciesCreateOrUpdate(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId, parameters)



Creates or updates a service Endpoint Policies.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ServiceEndpointPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the service endpoint policy.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.ServiceEndpointPolicy(); // ServiceEndpointPolicy | Parameters supplied to the create or update service endpoint policy operation.
apiInstance.serviceEndpointPoliciesCreateOrUpdate(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **serviceEndpointPolicyName** | **String**| The name of the service endpoint policy. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ServiceEndpointPolicy**](ServiceEndpointPolicy.md)| Parameters supplied to the create or update service endpoint policy operation. | 

### Return type

[**ServiceEndpointPolicy**](ServiceEndpointPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serviceEndpointPoliciesDelete

> serviceEndpointPoliciesDelete(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId)



Deletes the specified service endpoint policy.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ServiceEndpointPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the service endpoint policy.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serviceEndpointPoliciesDelete(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId, (error, data, response) => {
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
 **serviceEndpointPolicyName** | **String**| The name of the service endpoint policy. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## serviceEndpointPoliciesGet

> ServiceEndpointPolicy serviceEndpointPoliciesGet(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId, opts)



Gets the specified service Endpoint Policies in a specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ServiceEndpointPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the service endpoint policy.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'expand': "expand_example" // String | Expands referenced resources.
};
apiInstance.serviceEndpointPoliciesGet(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **serviceEndpointPolicyName** | **String**| The name of the service endpoint policy. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **expand** | **String**| Expands referenced resources. | [optional] 

### Return type

[**ServiceEndpointPolicy**](ServiceEndpointPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceEndpointPoliciesList

> ServiceEndpointPolicyListResult serviceEndpointPoliciesList(apiVersion, subscriptionId)



Gets all the service endpoint policies in a subscription.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ServiceEndpointPoliciesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serviceEndpointPoliciesList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ServiceEndpointPolicyListResult**](ServiceEndpointPolicyListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceEndpointPoliciesListByResourceGroup

> ServiceEndpointPolicyListResult serviceEndpointPoliciesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets all service endpoint Policies in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ServiceEndpointPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serviceEndpointPoliciesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ServiceEndpointPolicyListResult**](ServiceEndpointPolicyListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceEndpointPoliciesUpdate

> ServiceEndpointPolicy serviceEndpointPoliciesUpdate(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId, parameters)



Updates service Endpoint Policies.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ServiceEndpointPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the service endpoint policy.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.ServiceEndpointPoliciesUpdateRequest(); // ServiceEndpointPoliciesUpdateRequest | Parameters supplied to update service endpoint policy tags.
apiInstance.serviceEndpointPoliciesUpdate(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **serviceEndpointPolicyName** | **String**| The name of the service endpoint policy. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ServiceEndpointPoliciesUpdateRequest**](ServiceEndpointPoliciesUpdateRequest.md)| Parameters supplied to update service endpoint policy tags. | 

### Return type

[**ServiceEndpointPolicy**](ServiceEndpointPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

