# ServiceBusManagementClient.QueuesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queuesCreateOrUpdate**](QueuesApi.md#queuesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName} | 
[**queuesCreateOrUpdateAuthorizationRule**](QueuesApi.md#queuesCreateOrUpdateAuthorizationRule) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName}/authorizationRules/{authorizationRuleName} | 
[**queuesDelete**](QueuesApi.md#queuesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName} | 
[**queuesDeleteAuthorizationRule**](QueuesApi.md#queuesDeleteAuthorizationRule) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName}/authorizationRules/{authorizationRuleName} | 
[**queuesGet**](QueuesApi.md#queuesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName} | 
[**queuesGetAuthorizationRule**](QueuesApi.md#queuesGetAuthorizationRule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName}/authorizationRules/{authorizationRuleName} | 
[**queuesListAll**](QueuesApi.md#queuesListAll) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues | 
[**queuesListAuthorizationRules**](QueuesApi.md#queuesListAuthorizationRules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName}/authorizationRules | 
[**queuesListKeys**](QueuesApi.md#queuesListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName}/authorizationRules/{authorizationRuleName}/ListKeys | 
[**queuesPostAuthorizationRule**](QueuesApi.md#queuesPostAuthorizationRule) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName}/authorizationRules/{authorizationRuleName} | 
[**queuesRegenerateKeys**](QueuesApi.md#queuesRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName}/authorizationRules/{authorizationRuleName}/regenerateKeys | 



## queuesCreateOrUpdate

> QueueResource queuesCreateOrUpdate(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId, parameters)



Creates or updates a Service Bus queue. This operation is idempotent.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.QueuesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let queueName = "queueName_example"; // String | The queue name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ServiceBusManagementClient.QueueCreateOrUpdateParameters(); // QueueCreateOrUpdateParameters | Parameters supplied to create or update a queue resource.
apiInstance.queuesCreateOrUpdate(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **queueName** | **String**| The queue name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**QueueCreateOrUpdateParameters**](QueueCreateOrUpdateParameters.md)| Parameters supplied to create or update a queue resource. | 

### Return type

[**QueueResource**](QueueResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queuesCreateOrUpdateAuthorizationRule

> SharedAccessAuthorizationRuleResource queuesCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Creates an authorization rule for a queue.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.QueuesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let queueName = "queueName_example"; // String | The queue name.
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ServiceBusManagementClient.SharedAccessAuthorizationRuleCreateOrUpdateParameters(); // SharedAccessAuthorizationRuleCreateOrUpdateParameters | The shared access authorization rule.
apiInstance.queuesCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **queueName** | **String**| The queue name. | 
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


## queuesDelete

> queuesDelete(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId)



Deletes a queue from the specified namespace in a resource group.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.QueuesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let queueName = "queueName_example"; // String | The queue name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.queuesDelete(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId, (error, data, response) => {
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
 **queueName** | **String**| The queue name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## queuesDeleteAuthorizationRule

> queuesDeleteAuthorizationRule(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId)



Deletes a queue authorization rule.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.QueuesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let queueName = "queueName_example"; // String | The queue name.
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.queuesDeleteAuthorizationRule(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **queueName** | **String**| The queue name. | 
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


## queuesGet

> QueueResource queuesGet(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId)



Returns a description for the specified queue.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.QueuesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let queueName = "queueName_example"; // String | The queue name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.queuesGet(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId, (error, data, response) => {
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
 **queueName** | **String**| The queue name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**QueueResource**](QueueResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queuesGetAuthorizationRule

> SharedAccessAuthorizationRuleResource queuesGetAuthorizationRule(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId)



Gets an authorization rule for a queue by rule name.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.QueuesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let queueName = "queueName_example"; // String | The queue name.
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.queuesGetAuthorizationRule(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **queueName** | **String**| The queue name. | 
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


## queuesListAll

> QueueListResult queuesListAll(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Gets the queues within a namespace.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.QueuesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.queuesListAll(resourceGroupName, namespaceName, apiVersion, subscriptionId, (error, data, response) => {
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

[**QueueListResult**](QueueListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queuesListAuthorizationRules

> SharedAccessAuthorizationRuleListResult queuesListAuthorizationRules(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId)



Gets all authorization rules for a queue.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.QueuesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let queueName = "queueName_example"; // String | The queue name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.queuesListAuthorizationRules(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId, (error, data, response) => {
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
 **queueName** | **String**| The queue name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SharedAccessAuthorizationRuleListResult**](SharedAccessAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queuesListKeys

> ResourceListKeys queuesListKeys(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId)



Primary and secondary connection strings to the queue.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.QueuesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let queueName = "queueName_example"; // String | The queue name.
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.queuesListKeys(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **queueName** | **String**| The queue name. | 
 **authorizationRuleName** | **String**| The authorization rule name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ResourceListKeys**](ResourceListKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queuesPostAuthorizationRule

> SharedAccessAuthorizationRuleResource queuesPostAuthorizationRule(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId)



Gets an authorization rule for a queue by rule name.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.QueuesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let queueName = "queueName_example"; // String | The queue name.
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.queuesPostAuthorizationRule(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **queueName** | **String**| The queue name. | 
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


## queuesRegenerateKeys

> ResourceListKeys queuesRegenerateKeys(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Regenerates the primary or secondary connection strings to the queue.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.QueuesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let queueName = "queueName_example"; // String | The queue name.
let authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ServiceBusManagementClient.RegenerateKeysParameters(); // RegenerateKeysParameters | Parameters supplied to regenerate the authorization rule.
apiInstance.queuesRegenerateKeys(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **queueName** | **String**| The queue name. | 
 **authorizationRuleName** | **String**| The authorization rule name. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**RegenerateKeysParameters**](RegenerateKeysParameters.md)| Parameters supplied to regenerate the authorization rule. | 

### Return type

[**ResourceListKeys**](ResourceListKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

