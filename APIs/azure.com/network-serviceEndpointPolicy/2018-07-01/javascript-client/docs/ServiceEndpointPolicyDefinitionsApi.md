# NetworkManagementClient.ServiceEndpointPolicyDefinitionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceEndpointPolicyDefinitionsCreateOrUpdate**](ServiceEndpointPolicyDefinitionsApi.md#serviceEndpointPolicyDefinitionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName}/serviceEndpointPolicyDefinitions/{serviceEndpointPolicyDefinitionName} | 
[**serviceEndpointPolicyDefinitionsDelete**](ServiceEndpointPolicyDefinitionsApi.md#serviceEndpointPolicyDefinitionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName}/serviceEndpointPolicyDefinitions/{serviceEndpointPolicyDefinitionName} | 
[**serviceEndpointPolicyDefinitionsGet**](ServiceEndpointPolicyDefinitionsApi.md#serviceEndpointPolicyDefinitionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName}/serviceEndpointPolicyDefinitions/{serviceEndpointPolicyDefinitionName} | 
[**serviceEndpointPolicyDefinitionsListByResourceGroup**](ServiceEndpointPolicyDefinitionsApi.md#serviceEndpointPolicyDefinitionsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName}/serviceEndpointPolicyDefinitions | 



## serviceEndpointPolicyDefinitionsCreateOrUpdate

> ServiceEndpointPolicyDefinition serviceEndpointPolicyDefinitionsCreateOrUpdate(resourceGroupName, serviceEndpointPolicyName, serviceEndpointPolicyDefinitionName, apiVersion, subscriptionId, serviceEndpointPolicyDefinitions)



Creates or updates a service endpoint policy definition in the specified service endpoint policy.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ServiceEndpointPolicyDefinitionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the service endpoint policy.
let serviceEndpointPolicyDefinitionName = "serviceEndpointPolicyDefinitionName_example"; // String | The name of the service endpoint policy definition name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let serviceEndpointPolicyDefinitions = new NetworkManagementClient.ServiceEndpointPolicyDefinition(); // ServiceEndpointPolicyDefinition | Parameters supplied to the create or update service endpoint policy operation.
apiInstance.serviceEndpointPolicyDefinitionsCreateOrUpdate(resourceGroupName, serviceEndpointPolicyName, serviceEndpointPolicyDefinitionName, apiVersion, subscriptionId, serviceEndpointPolicyDefinitions, (error, data, response) => {
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
 **serviceEndpointPolicyDefinitionName** | **String**| The name of the service endpoint policy definition name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **serviceEndpointPolicyDefinitions** | [**ServiceEndpointPolicyDefinition**](ServiceEndpointPolicyDefinition.md)| Parameters supplied to the create or update service endpoint policy operation. | 

### Return type

[**ServiceEndpointPolicyDefinition**](ServiceEndpointPolicyDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serviceEndpointPolicyDefinitionsDelete

> serviceEndpointPolicyDefinitionsDelete(resourceGroupName, serviceEndpointPolicyName, serviceEndpointPolicyDefinitionName, apiVersion, subscriptionId)



Deletes the specified ServiceEndpoint policy definitions.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ServiceEndpointPolicyDefinitionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the Service Endpoint Policy.
let serviceEndpointPolicyDefinitionName = "serviceEndpointPolicyDefinitionName_example"; // String | The name of the service endpoint policy definition.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serviceEndpointPolicyDefinitionsDelete(resourceGroupName, serviceEndpointPolicyName, serviceEndpointPolicyDefinitionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **serviceEndpointPolicyName** | **String**| The name of the Service Endpoint Policy. | 
 **serviceEndpointPolicyDefinitionName** | **String**| The name of the service endpoint policy definition. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## serviceEndpointPolicyDefinitionsGet

> ServiceEndpointPolicyDefinition serviceEndpointPolicyDefinitionsGet(resourceGroupName, serviceEndpointPolicyName, serviceEndpointPolicyDefinitionName, apiVersion, subscriptionId)



Get the specified service endpoint policy definitions from service endpoint policy.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ServiceEndpointPolicyDefinitionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the service endpoint policy name.
let serviceEndpointPolicyDefinitionName = "serviceEndpointPolicyDefinitionName_example"; // String | The name of the service endpoint policy definition name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serviceEndpointPolicyDefinitionsGet(resourceGroupName, serviceEndpointPolicyName, serviceEndpointPolicyDefinitionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **serviceEndpointPolicyName** | **String**| The name of the service endpoint policy name. | 
 **serviceEndpointPolicyDefinitionName** | **String**| The name of the service endpoint policy definition name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ServiceEndpointPolicyDefinition**](ServiceEndpointPolicyDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceEndpointPolicyDefinitionsListByResourceGroup

> ServiceEndpointPolicyDefinitionListResult serviceEndpointPolicyDefinitionsListByResourceGroup(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId)



Gets all service endpoint policy definitions in a service end point policy.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ServiceEndpointPolicyDefinitionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the service endpoint policy name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serviceEndpointPolicyDefinitionsListByResourceGroup(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId, (error, data, response) => {
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
 **serviceEndpointPolicyName** | **String**| The name of the service endpoint policy name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ServiceEndpointPolicyDefinitionListResult**](ServiceEndpointPolicyDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

