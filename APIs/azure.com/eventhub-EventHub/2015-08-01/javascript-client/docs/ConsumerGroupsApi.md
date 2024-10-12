# EventHubManagementClient.ConsumerGroupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consumerGroupsCreateOrUpdate**](ConsumerGroupsApi.md#consumerGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups/{consumerGroupName} | 
[**consumerGroupsDelete**](ConsumerGroupsApi.md#consumerGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups/{consumerGroupName} | 
[**consumerGroupsGet**](ConsumerGroupsApi.md#consumerGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups/{consumerGroupName} | 
[**consumerGroupsListAll**](ConsumerGroupsApi.md#consumerGroupsListAll) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups | 



## consumerGroupsCreateOrUpdate

> ConsumerGroupResource consumerGroupsCreateOrUpdate(resourceGroupName, namespaceName, eventHubName, consumerGroupName, apiVersion, subscriptionId, parameters)



Creates or updates an Event Hubs consumer group as a nested resource within a Namespace.

### Example

```javascript
import EventHubManagementClient from 'event_hub_management_client';
let defaultClient = EventHubManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EventHubManagementClient.ConsumerGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
let namespaceName = "namespaceName_example"; // String | The Namespace name
let eventHubName = "eventHubName_example"; // String | The Event Hub name
let consumerGroupName = "consumerGroupName_example"; // String | The consumer group name
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new EventHubManagementClient.ConsumerGroupCreateOrUpdateParameters(); // ConsumerGroupCreateOrUpdateParameters | Parameters supplied to create or update a consumer group resource.
apiInstance.consumerGroupsCreateOrUpdate(resourceGroupName, namespaceName, eventHubName, consumerGroupName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | 
 **namespaceName** | **String**| The Namespace name | 
 **eventHubName** | **String**| The Event Hub name | 
 **consumerGroupName** | **String**| The consumer group name | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ConsumerGroupCreateOrUpdateParameters**](ConsumerGroupCreateOrUpdateParameters.md)| Parameters supplied to create or update a consumer group resource. | 

### Return type

[**ConsumerGroupResource**](ConsumerGroupResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## consumerGroupsDelete

> consumerGroupsDelete(resourceGroupName, namespaceName, eventHubName, consumerGroupName, apiVersion, subscriptionId)



Deletes a consumer group from the specified Event Hub and resource group.

### Example

```javascript
import EventHubManagementClient from 'event_hub_management_client';
let defaultClient = EventHubManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EventHubManagementClient.ConsumerGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
let namespaceName = "namespaceName_example"; // String | The Namespace name
let eventHubName = "eventHubName_example"; // String | The Event Hub name
let consumerGroupName = "consumerGroupName_example"; // String | The consumer group name
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.consumerGroupsDelete(resourceGroupName, namespaceName, eventHubName, consumerGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | 
 **namespaceName** | **String**| The Namespace name | 
 **eventHubName** | **String**| The Event Hub name | 
 **consumerGroupName** | **String**| The consumer group name | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## consumerGroupsGet

> ConsumerGroupResource consumerGroupsGet(resourceGroupName, namespaceName, eventHubName, consumerGroupName, apiVersion, subscriptionId)



Gets a description for the specified consumer group.

### Example

```javascript
import EventHubManagementClient from 'event_hub_management_client';
let defaultClient = EventHubManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EventHubManagementClient.ConsumerGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
let namespaceName = "namespaceName_example"; // String | The Namespace name
let eventHubName = "eventHubName_example"; // String | The Event Hub name
let consumerGroupName = "consumerGroupName_example"; // String | The consumer group name
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.consumerGroupsGet(resourceGroupName, namespaceName, eventHubName, consumerGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | 
 **namespaceName** | **String**| The Namespace name | 
 **eventHubName** | **String**| The Event Hub name | 
 **consumerGroupName** | **String**| The consumer group name | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ConsumerGroupResource**](ConsumerGroupResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerGroupsListAll

> ConsumerGroupListResult consumerGroupsListAll(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId)



Gets all the consumer groups in a Namespace. An empty feed is returned if no consumer group exists in the Namespace.

### Example

```javascript
import EventHubManagementClient from 'event_hub_management_client';
let defaultClient = EventHubManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EventHubManagementClient.ConsumerGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
let namespaceName = "namespaceName_example"; // String | The Namespace name
let eventHubName = "eventHubName_example"; // String | The Event Hub name
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.consumerGroupsListAll(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | 
 **namespaceName** | **String**| The Namespace name | 
 **eventHubName** | **String**| The Event Hub name | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ConsumerGroupListResult**](ConsumerGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

