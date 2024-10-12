# WebApplicationFirewallManagement.ListWebApplicationFirewallPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policiesList**](ListWebApplicationFirewallPoliciesApi.md#policiesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies | 



## policiesList

> WebApplicationFirewallPolicyListResult policiesList(resourceGroupName, subscriptionId, apiVersion)



Lists all of the protection policies within a resource group.

### Example

```javascript
import WebApplicationFirewallManagement from 'web_application_firewall_management';
let defaultClient = WebApplicationFirewallManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebApplicationFirewallManagement.ListWebApplicationFirewallPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**WebApplicationFirewallPolicyListResult**](WebApplicationFirewallPolicyListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

