# ServiceBusManagementClient.TopicsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**topicsCreateOrUpdate**](TopicsApi.md#topicsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName} | 
[**topicsCreateOrUpdateAuthorizationRule**](TopicsApi.md#topicsCreateOrUpdateAuthorizationRule) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName} | 
[**topicsDelete**](TopicsApi.md#topicsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName} | 
[**topicsDeleteAuthorizationRule**](TopicsApi.md#topicsDeleteAuthorizationRule) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName} | 
[**topicsGet**](TopicsApi.md#topicsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName} | 
[**topicsGetAuthorizationRule**](TopicsApi.md#topicsGetAuthorizationRule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName} | 
[**topicsListAll**](TopicsApi.md#topicsListAll) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics | 
[**topicsListAuthorizationRules**](TopicsApi.md#topicsListAuthorizationRules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules | 
[**topicsPostAuthorizationRule**](TopicsApi.md#topicsPostAuthorizationRule) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName} | 



## topicsCreateOrUpdate

> TopicResource topicsCreateOrUpdate(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId, parameters)



Creates a topic in the specified namespace.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.TopicsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let topicName = "topicName_example"; // String | The topic name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ServiceBusManagementClient.TopicCreateOrUpdateParameters(); // TopicCreateOrUpdateParameters | Parameters supplied to create a topic resource.
apiInstance.topicsCreateOrUpdate(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**TopicCreateOrUpdateParameters**](TopicCreateOrUpdateParameters.md)| Parameters supplied to create a topic resource. | 

### Return type

[**TopicResource**](TopicResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## topicsCreateOrUpdateAuthorizationRule

> SharedAccessAuthorizationRuleResource topicsCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Creates an authorization rule for the specified topic.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.TopicsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let topicName = "topicName_example"; // String | The topic name.
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ServiceBusManagementClient.SharedAccessAuthorizationRuleCreateOrUpdateParameters(); // SharedAccessAuthorizationRuleCreateOrUpdateParameters | The shared access authorization rule.
apiInstance.topicsCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **authorizationRuleName** | **String**| The authorization rule name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**SharedAccessAuthorizationRuleCreateOrUpdateParameters**](SharedAccessAuthorizationRuleCreateOrUpdateParameters.md)| The shared access authorization rule. | 

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## topicsDelete

> topicsDelete(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId)



Deletes a topic from the specified namespace and resource group.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.TopicsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let topicName = "topicName_example"; // String | The topic name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.topicsDelete(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## topicsDeleteAuthorizationRule

> topicsDeleteAuthorizationRule(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId)



Deletes a topic authorization rule.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.TopicsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let topicName = "topicName_example"; // String | The topic name.
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.topicsDeleteAuthorizationRule(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **authorizationRuleName** | **String**| The authorization rule name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## topicsGet

> TopicResource topicsGet(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId)



Returns a description for the specified topic.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.TopicsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let topicName = "topicName_example"; // String | The topic name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.topicsGet(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**TopicResource**](TopicResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topicsGetAuthorizationRule

> SharedAccessAuthorizationRuleGetResource topicsGetAuthorizationRule(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId)



Returns the specified authorization rule.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.TopicsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let topicName = "topicName_example"; // String | The topic name.
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.topicsGetAuthorizationRule(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **authorizationRuleName** | **String**| The authorization rule name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SharedAccessAuthorizationRuleGetResource**](SharedAccessAuthorizationRuleGetResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topicsListAll

> TopicListResult topicsListAll(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Gets all the topics in a namespace.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.TopicsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.topicsListAll(resourceGroupName, namespaceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**TopicListResult**](TopicListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topicsListAuthorizationRules

> SharedAccessAuthorizationRuleListResult topicsListAuthorizationRules(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId)



Gets authorization rules for a topic.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.TopicsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let topicName = "topicName_example"; // String | The topic name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.topicsListAuthorizationRules(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SharedAccessAuthorizationRuleListResult**](SharedAccessAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topicsPostAuthorizationRule

> SharedAccessAuthorizationRuleResource topicsPostAuthorizationRule(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId)



Returns the specified authorization rule.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.TopicsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let topicName = "topicName_example"; // String | The topic name.
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.topicsPostAuthorizationRule(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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

