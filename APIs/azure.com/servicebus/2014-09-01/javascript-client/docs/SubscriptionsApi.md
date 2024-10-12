# ServiceBusManagementClient.SubscriptionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptionsCreateOrUpdate**](SubscriptionsApi.md#subscriptionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/subscriptions/{subscriptionName} | 
[**subscriptionsDelete**](SubscriptionsApi.md#subscriptionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/subscriptions/{subscriptionName} | 
[**subscriptionsGet**](SubscriptionsApi.md#subscriptionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/subscriptions/{subscriptionName} | 
[**subscriptionsListAll**](SubscriptionsApi.md#subscriptionsListAll) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/subscriptions | 



## subscriptionsCreateOrUpdate

> SubscriptionResource subscriptionsCreateOrUpdate(resourceGroupName, namespaceName, topicName, subscriptionName, apiVersion, subscriptionId, parameters)



Creates a topic subscription.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.SubscriptionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let topicName = "topicName_example"; // String | The topic name.
let subscriptionName = "subscriptionName_example"; // String | The subscription name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ServiceBusManagementClient.SubscriptionCreateOrUpdateParameters(); // SubscriptionCreateOrUpdateParameters | Parameters supplied to create a subscription resource.
apiInstance.subscriptionsCreateOrUpdate(resourceGroupName, namespaceName, topicName, subscriptionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **parameters** | [**SubscriptionCreateOrUpdateParameters**](SubscriptionCreateOrUpdateParameters.md)| Parameters supplied to create a subscription resource. | 

### Return type

[**SubscriptionResource**](SubscriptionResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscriptionsDelete

> subscriptionsDelete(resourceGroupName, namespaceName, topicName, subscriptionName, apiVersion, subscriptionId)



Deletes a subscription from the specified topic.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.SubscriptionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let topicName = "topicName_example"; // String | The topic name.
let subscriptionName = "subscriptionName_example"; // String | The subscription name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.subscriptionsDelete(resourceGroupName, namespaceName, topicName, subscriptionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## subscriptionsGet

> SubscriptionResource subscriptionsGet(resourceGroupName, namespaceName, topicName, subscriptionName, apiVersion, subscriptionId)



Returns a subscription description for the specified topic.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.SubscriptionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let topicName = "topicName_example"; // String | The topic name.
let subscriptionName = "subscriptionName_example"; // String | The subscription name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.subscriptionsGet(resourceGroupName, namespaceName, topicName, subscriptionName, apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**SubscriptionResource**](SubscriptionResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionsListAll

> SubscriptionListResult subscriptionsListAll(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId)



List all the subscriptions under a specified topic.

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.SubscriptionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let namespaceName = "namespaceName_example"; // String | The namespace name
let topicName = "topicName_example"; // String | The topic name.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.subscriptionsListAll(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId, (error, data, response) => {
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

[**SubscriptionListResult**](SubscriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

