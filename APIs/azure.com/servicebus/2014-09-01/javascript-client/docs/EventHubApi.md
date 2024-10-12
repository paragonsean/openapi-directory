# ServiceBusManagementClient.EventHubApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventHubGetAuthorizationRule**](EventHubApi.md#eventHubGetAuthorizationRule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/eventhubs/{eventhubName}/authorizationRules/{authorizationRuleName} | 
[**eventHubListAuthorizationRules**](EventHubApi.md#eventHubListAuthorizationRules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/eventhubs/{eventhubName}/authorizationRules | 



## eventHubGetAuthorizationRule

> SharedAccessAuthorizationRuleResource eventHubGetAuthorizationRule(resourceGroupName, namespaceName, eventhubName, authorizationRuleName, apiVersion, subscriptionId)



Returns the specified authorization rule.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.EventHubApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let eventhubName = "eventhubName_example"; // String | The eventhub name.
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.eventHubGetAuthorizationRule(resourceGroupName, namespaceName, eventhubName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **namespaceName** | **String**| The namespace name | 
 **eventhubName** | **String**| The eventhub name. | 
 **authorizationRuleName** | **String**| The authorization rule name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventHubListAuthorizationRules

> SharedAccessAuthorizationRuleListResult eventHubListAuthorizationRules(resourceGroupName, namespaceName, eventhubName, apiVersion, subscriptionId)



Gets authorization rules for a eventhub.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.EventHubApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let eventhubName = "eventhubName_example"; // String | The eventhub name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.eventHubListAuthorizationRules(resourceGroupName, namespaceName, eventhubName, apiVersion, subscriptionId, (error, data, response) => {
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
 **namespaceName** | **String**| The namespace name | 
 **eventhubName** | **String**| The eventhub name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SharedAccessAuthorizationRuleListResult**](SharedAccessAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

