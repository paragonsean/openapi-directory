# NetworkManagementClient.AzureFirewallFqdnTagsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**azureFirewallFqdnTagsListAll**](AzureFirewallFqdnTagsApi.md#azureFirewallFqdnTagsListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/azureFirewallFqdnTags | 



## azureFirewallFqdnTagsListAll

> AzureFirewallFqdnTagListResult azureFirewallFqdnTagsListAll(apiVersion, subscriptionId)



Gets all the Azure Firewall FQDN Tags in a subscription.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.AzureFirewallFqdnTagsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.azureFirewallFqdnTagsListAll(apiVersion, subscriptionId, (error, data, response) => {
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

[**AzureFirewallFqdnTagListResult**](AzureFirewallFqdnTagListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

