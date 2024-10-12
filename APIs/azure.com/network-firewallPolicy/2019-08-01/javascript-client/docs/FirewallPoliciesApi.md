# NetworkManagementClient.FirewallPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firewallPoliciesCreateOrUpdate**](FirewallPoliciesApi.md#firewallPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName} | 
[**firewallPoliciesDelete**](FirewallPoliciesApi.md#firewallPoliciesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName} | 
[**firewallPoliciesGet**](FirewallPoliciesApi.md#firewallPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName} | 
[**firewallPoliciesList**](FirewallPoliciesApi.md#firewallPoliciesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies | 
[**firewallPoliciesListAll**](FirewallPoliciesApi.md#firewallPoliciesListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/firewallPolicies | 
[**firewallPoliciesUpdateTags**](FirewallPoliciesApi.md#firewallPoliciesUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName} | 



## firewallPoliciesCreateOrUpdate

> FirewallPolicy firewallPoliciesCreateOrUpdate(resourceGroupName, firewallPolicyName, apiVersion, subscriptionId, parameters)



Creates or updates the specified Firewall Policy.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.FirewallPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let firewallPolicyName = "firewallPolicyName_example"; // String | The name of the Firewall Policy.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.FirewallPolicy(); // FirewallPolicy | Parameters supplied to the create or update Firewall Policy operation.
apiInstance.firewallPoliciesCreateOrUpdate(resourceGroupName, firewallPolicyName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **firewallPolicyName** | **String**| The name of the Firewall Policy. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**FirewallPolicy**](FirewallPolicy.md)| Parameters supplied to the create or update Firewall Policy operation. | 

### Return type

[**FirewallPolicy**](FirewallPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firewallPoliciesDelete

> firewallPoliciesDelete(resourceGroupName, firewallPolicyName, apiVersion, subscriptionId)



Deletes the specified Firewall Policy.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.FirewallPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let firewallPolicyName = "firewallPolicyName_example"; // String | The name of the Firewall Policy.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.firewallPoliciesDelete(resourceGroupName, firewallPolicyName, apiVersion, subscriptionId, (error, data, response) => {
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
 **firewallPolicyName** | **String**| The name of the Firewall Policy. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## firewallPoliciesGet

> FirewallPolicy firewallPoliciesGet(resourceGroupName, firewallPolicyName, apiVersion, subscriptionId, opts)



Gets the specified Firewall Policy.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.FirewallPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let firewallPolicyName = "firewallPolicyName_example"; // String | The name of the Firewall Policy.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'expand': "expand_example" // String | Expands referenced resources.
};
apiInstance.firewallPoliciesGet(resourceGroupName, firewallPolicyName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **firewallPolicyName** | **String**| The name of the Firewall Policy. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **expand** | **String**| Expands referenced resources. | [optional] 

### Return type

[**FirewallPolicy**](FirewallPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firewallPoliciesList

> FirewallPolicyListResult firewallPoliciesList(resourceGroupName, apiVersion, subscriptionId)



Lists all Firewall Policies in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.FirewallPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.firewallPoliciesList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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

[**FirewallPolicyListResult**](FirewallPolicyListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firewallPoliciesListAll

> FirewallPolicyListResult firewallPoliciesListAll(apiVersion, subscriptionId)



Gets all the Firewall Policies in a subscription.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.FirewallPoliciesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.firewallPoliciesListAll(apiVersion, subscriptionId, (error, data, response) => {
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

[**FirewallPolicyListResult**](FirewallPolicyListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firewallPoliciesUpdateTags

> FirewallPolicy firewallPoliciesUpdateTags(subscriptionId, resourceGroupName, firewallPolicyName, apiVersion, firewallPolicyParameters)



Updates a Firewall Policy Tags.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.FirewallPoliciesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the Firewall Policy.
let firewallPolicyName = "firewallPolicyName_example"; // String | The name of the Firewall Policy being updated.
let apiVersion = "apiVersion_example"; // String | Client API version.
let firewallPolicyParameters = new NetworkManagementClient.FirewallPoliciesUpdateTagsRequest(); // FirewallPoliciesUpdateTagsRequest | Parameters supplied to Update Firewall Policy tags.
apiInstance.firewallPoliciesUpdateTags(subscriptionId, resourceGroupName, firewallPolicyName, apiVersion, firewallPolicyParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group name of the Firewall Policy. | 
 **firewallPolicyName** | **String**| The name of the Firewall Policy being updated. | 
 **apiVersion** | **String**| Client API version. | 
 **firewallPolicyParameters** | [**FirewallPoliciesUpdateTagsRequest**](FirewallPoliciesUpdateTagsRequest.md)| Parameters supplied to Update Firewall Policy tags. | 

### Return type

[**FirewallPolicy**](FirewallPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

