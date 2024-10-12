# WebApplicationFirewallManagement.WebApplicationFirewallPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policiesCreateOrUpdate**](WebApplicationFirewallPoliciesApi.md#policiesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies/{policyName} | 
[**policiesDelete**](WebApplicationFirewallPoliciesApi.md#policiesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies/{policyName} | 
[**policiesGet**](WebApplicationFirewallPoliciesApi.md#policiesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies/{policyName} | 
[**policiesList**](WebApplicationFirewallPoliciesApi.md#policiesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies | 



## policiesCreateOrUpdate

> WebApplicationFirewallPolicy policiesCreateOrUpdate(resourceGroupName, policyName, subscriptionId, apiVersion, parameters)



Create or update policy with specified rule set name within a resource group.

### Example

```javascript
import WebApplicationFirewallManagement from 'web_application_firewall_management';
let defaultClient = WebApplicationFirewallManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebApplicationFirewallManagement.WebApplicationFirewallPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let policyName = "policyName_example"; // String | The name of the Web Application Firewall Policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new WebApplicationFirewallManagement.WebApplicationFirewallPolicy(); // WebApplicationFirewallPolicy | Policy to be created.
apiInstance.policiesCreateOrUpdate(resourceGroupName, policyName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **policyName** | **String**| The name of the Web Application Firewall Policy. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **parameters** | [**WebApplicationFirewallPolicy**](WebApplicationFirewallPolicy.md)| Policy to be created. | 

### Return type

[**WebApplicationFirewallPolicy**](WebApplicationFirewallPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## policiesDelete

> policiesDelete(resourceGroupName, policyName, subscriptionId, apiVersion)



Deletes Policy

### Example

```javascript
import WebApplicationFirewallManagement from 'web_application_firewall_management';
let defaultClient = WebApplicationFirewallManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebApplicationFirewallManagement.WebApplicationFirewallPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let policyName = "policyName_example"; // String | The name of the Web Application Firewall Policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.policiesDelete(resourceGroupName, policyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **policyName** | **String**| The name of the Web Application Firewall Policy. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## policiesGet

> WebApplicationFirewallPolicy policiesGet(resourceGroupName, policyName, subscriptionId, apiVersion)



Retrieve protection policy with specified name within a resource group.

### Example

```javascript
import WebApplicationFirewallManagement from 'web_application_firewall_management';
let defaultClient = WebApplicationFirewallManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebApplicationFirewallManagement.WebApplicationFirewallPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let policyName = "policyName_example"; // String | The name of the Web Application Firewall Policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.policiesGet(resourceGroupName, policyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **policyName** | **String**| The name of the Web Application Firewall Policy. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**WebApplicationFirewallPolicy**](WebApplicationFirewallPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policiesList

> WebApplicationFirewallPolicyList policiesList(resourceGroupName, subscriptionId, apiVersion)



Lists all of the protection policies within a resource group.

### Example

```javascript
import WebApplicationFirewallManagement from 'web_application_firewall_management';
let defaultClient = WebApplicationFirewallManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebApplicationFirewallManagement.WebApplicationFirewallPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.policiesList(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**WebApplicationFirewallPolicyList**](WebApplicationFirewallPolicyList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

