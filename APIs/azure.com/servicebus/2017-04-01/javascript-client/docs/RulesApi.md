# ServiceBusManagementClient.RulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rulesCreateOrUpdate**](RulesApi.md#rulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/subscriptions/{subscriptionName}/rules/{ruleName} | 
[**rulesDelete**](RulesApi.md#rulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/subscriptions/{subscriptionName}/rules/{ruleName} | 
[**rulesListBySubscriptions**](RulesApi.md#rulesListBySubscriptions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/subscriptions/{subscriptionName}/rules | 



## rulesCreateOrUpdate

> Rule rulesCreateOrUpdate(resourceGroupName, namespaceName, topicName, subscriptionName, ruleName, apiVersion, subscriptionId, parameters)



Creates a new rule and updates an existing rule

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.RulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let topicName = "topicName_example"; // String | The topic name.
let subscriptionName = "subscriptionName_example"; // String | The subscription name.
let ruleName = "ruleName_example"; // String | The rule name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ServiceBusManagementClient.Rule(); // Rule | Parameters supplied to create a rule.
apiInstance.rulesCreateOrUpdate(resourceGroupName, namespaceName, topicName, subscriptionName, ruleName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **topicName** | **String**| The topic name. | 
 **subscriptionName** | **String**| The subscription name. | 
 **ruleName** | **String**| The rule name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**Rule**](Rule.md)| Parameters supplied to create a rule. | 

### Return type

[**Rule**](Rule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rulesDelete

> rulesDelete(resourceGroupName, namespaceName, topicName, subscriptionName, ruleName, apiVersion, subscriptionId)



Deletes an existing rule.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.RulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let topicName = "topicName_example"; // String | The topic name.
let subscriptionName = "subscriptionName_example"; // String | The subscription name.
let ruleName = "ruleName_example"; // String | The rule name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.rulesDelete(resourceGroupName, namespaceName, topicName, subscriptionName, ruleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **namespaceName** | **String**| The namespace name | 
 **topicName** | **String**| The topic name. | 
 **subscriptionName** | **String**| The subscription name. | 
 **ruleName** | **String**| The rule name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rulesListBySubscriptions

> RuleListResult rulesListBySubscriptions(resourceGroupName, namespaceName, topicName, subscriptionName, apiVersion, subscriptionId, opts)



List all the rules within given topic-subscription

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.RulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let topicName = "topicName_example"; // String | The topic name.
let subscriptionName = "subscriptionName_example"; // String | The subscription name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'skip': 56, // Number | Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls.
  'top': 56 // Number | May be used to limit the number of results to the most recent N usageDetails.
};
apiInstance.rulesListBySubscriptions(resourceGroupName, namespaceName, topicName, subscriptionName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **topicName** | **String**| The topic name. | 
 **subscriptionName** | **String**| The subscription name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **skip** | **Number**| Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **top** | **Number**| May be used to limit the number of results to the most recent N usageDetails. | [optional] 

### Return type

[**RuleListResult**](RuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

