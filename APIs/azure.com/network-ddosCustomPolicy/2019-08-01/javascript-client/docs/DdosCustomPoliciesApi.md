# NetworkManagementClient.DdosCustomPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ddosCustomPoliciesCreateOrUpdate**](DdosCustomPoliciesApi.md#ddosCustomPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ddosCustomPolicies/{ddosCustomPolicyName} | 
[**ddosCustomPoliciesDelete**](DdosCustomPoliciesApi.md#ddosCustomPoliciesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ddosCustomPolicies/{ddosCustomPolicyName} | 
[**ddosCustomPoliciesGet**](DdosCustomPoliciesApi.md#ddosCustomPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ddosCustomPolicies/{ddosCustomPolicyName} | 
[**ddosCustomPoliciesUpdateTags**](DdosCustomPoliciesApi.md#ddosCustomPoliciesUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ddosCustomPolicies/{ddosCustomPolicyName} | 



## ddosCustomPoliciesCreateOrUpdate

> DdosCustomPolicy ddosCustomPoliciesCreateOrUpdate(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId, parameters)



Creates or updates a DDoS custom policy.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.DdosCustomPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ddosCustomPolicyName = "ddosCustomPolicyName_example"; // String | The name of the DDoS custom policy.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.DdosCustomPolicy(); // DdosCustomPolicy | Parameters supplied to the create or update operation.
apiInstance.ddosCustomPoliciesCreateOrUpdate(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **ddosCustomPolicyName** | **String**| The name of the DDoS custom policy. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**DdosCustomPolicy**](DdosCustomPolicy.md)| Parameters supplied to the create or update operation. | 

### Return type

[**DdosCustomPolicy**](DdosCustomPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ddosCustomPoliciesDelete

> ddosCustomPoliciesDelete(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId)



Deletes the specified DDoS custom policy.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.DdosCustomPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ddosCustomPolicyName = "ddosCustomPolicyName_example"; // String | The name of the DDoS custom policy.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.ddosCustomPoliciesDelete(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId, (error, data, response) => {
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
 **ddosCustomPolicyName** | **String**| The name of the DDoS custom policy. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ddosCustomPoliciesGet

> DdosCustomPolicy ddosCustomPoliciesGet(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId)



Gets information about the specified DDoS custom policy.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.DdosCustomPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ddosCustomPolicyName = "ddosCustomPolicyName_example"; // String | The name of the DDoS custom policy.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.ddosCustomPoliciesGet(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId, (error, data, response) => {
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
 **ddosCustomPolicyName** | **String**| The name of the DDoS custom policy. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DdosCustomPolicy**](DdosCustomPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ddosCustomPoliciesUpdateTags

> DdosCustomPolicy ddosCustomPoliciesUpdateTags(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId, parameters)



Update a DDoS custom policy tags.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.DdosCustomPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let ddosCustomPolicyName = "ddosCustomPolicyName_example"; // String | The name of the DDoS custom policy.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.DdosCustomPoliciesUpdateTagsRequest(); // DdosCustomPoliciesUpdateTagsRequest | Parameters supplied to the update DDoS custom policy resource tags.
apiInstance.ddosCustomPoliciesUpdateTags(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **ddosCustomPolicyName** | **String**| The name of the DDoS custom policy. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**DdosCustomPoliciesUpdateTagsRequest**](DdosCustomPoliciesUpdateTagsRequest.md)| Parameters supplied to the update DDoS custom policy resource tags. | 

### Return type

[**DdosCustomPolicy**](DdosCustomPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

