# WebApplicationFirewallManagement.CreateOrUpdateWebApplicationFirewallPolicyApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policiesCreateOrUpdate**](CreateOrUpdateWebApplicationFirewallPolicyApi.md#policiesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies/{policyName} | 



## policiesCreateOrUpdate

> WebApplicationFirewallPolicy policiesCreateOrUpdate(resourceGroupName, policyName, subscriptionId, apiVersion, parameters)



Creates or update policy with specified rule set name within a resource group.

### Example

```javascript
import WebApplicationFirewallManagement from 'web_application_firewall_management';
let defaultClient = WebApplicationFirewallManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebApplicationFirewallManagement.CreateOrUpdateWebApplicationFirewallPolicyApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let policyName = "policyName_example"; // String | The name of the resource group.
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **policyName** | **String**| The name of the resource group. | 
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

