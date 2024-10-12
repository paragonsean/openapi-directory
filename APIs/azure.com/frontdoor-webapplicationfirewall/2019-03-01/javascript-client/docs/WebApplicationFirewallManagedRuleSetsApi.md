# WebApplicationFirewallManagement.WebApplicationFirewallManagedRuleSetsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managedRuleSetsList**](WebApplicationFirewallManagedRuleSetsApi.md#managedRuleSetsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallManagedRuleSets | 



## managedRuleSetsList

> ManagedRuleSetDefinitionList managedRuleSetsList(subscriptionId, apiVersion)



Lists all available managed rule sets.

### Example

```javascript
import WebApplicationFirewallManagement from 'web_application_firewall_management';
let defaultClient = WebApplicationFirewallManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebApplicationFirewallManagement.WebApplicationFirewallManagedRuleSetsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.managedRuleSetsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 

### Return type

[**ManagedRuleSetDefinitionList**](ManagedRuleSetDefinitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

