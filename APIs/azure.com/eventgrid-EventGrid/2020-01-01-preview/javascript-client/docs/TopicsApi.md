# EventGridManagementClient.TopicsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**topicsCreateOrUpdate**](TopicsApi.md#topicsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName} | Create a topic
[**topicsDelete**](TopicsApi.md#topicsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName} | Delete a topic
[**topicsGet**](TopicsApi.md#topicsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName} | Get a topic
[**topicsListByResourceGroup**](TopicsApi.md#topicsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics | List topics under a resource group
[**topicsListBySubscription**](TopicsApi.md#topicsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EventGrid/topics | List topics under an Azure subscription
[**topicsListEventTypes**](TopicsApi.md#topicsListEventTypes) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{providerNamespace}/{resourceTypeName}/{resourceName}/providers/Microsoft.EventGrid/eventTypes | List topic event types
[**topicsListSharedAccessKeys**](TopicsApi.md#topicsListSharedAccessKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}/listKeys | List keys for a topic
[**topicsRegenerateKey**](TopicsApi.md#topicsRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}/regenerateKey | Regenerate key for a topic
[**topicsUpdate**](TopicsApi.md#topicsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName} | Update a topic



## topicsCreateOrUpdate

> Topic topicsCreateOrUpdate(subscriptionId, resourceGroupName, topicName, apiVersion, topicInfo)

Create a topic

Asynchronously creates a new topic with the specified parameters.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.TopicsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let topicName = "topicName_example"; // String | Name of the topic
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let topicInfo = new EventGridManagementClient.Topic(); // Topic | Topic information
apiInstance.topicsCreateOrUpdate(subscriptionId, resourceGroupName, topicName, apiVersion, topicInfo, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | 
 **topicName** | **String**| Name of the topic | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **topicInfo** | [**Topic**](Topic.md)| Topic information | 

### Return type

[**Topic**](Topic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## topicsDelete

> topicsDelete(subscriptionId, resourceGroupName, topicName, apiVersion)

Delete a topic

Delete existing topic

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.TopicsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let topicName = "topicName_example"; // String | Name of the topic
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.topicsDelete(subscriptionId, resourceGroupName, topicName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | 
 **topicName** | **String**| Name of the topic | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## topicsGet

> Topic topicsGet(subscriptionId, resourceGroupName, topicName, apiVersion)

Get a topic

Get properties of a topic

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.TopicsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let topicName = "topicName_example"; // String | Name of the topic
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.topicsGet(subscriptionId, resourceGroupName, topicName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | 
 **topicName** | **String**| Name of the topic | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**Topic**](Topic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topicsListByResourceGroup

> TopicsListResult topicsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)

List topics under a resource group

List all the topics under a resource group

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.TopicsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.
  'top': 56 // Number | The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
};
apiInstance.topicsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **filter** | **String**| The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;. | [optional] 
 **top** | **Number**| The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. | [optional] 

### Return type

[**TopicsListResult**](TopicsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topicsListBySubscription

> TopicsListResult topicsListBySubscription(subscriptionId, apiVersion, opts)

List topics under an Azure subscription

List all the topics under an Azure subscription

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.TopicsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.
  'top': 56 // Number | The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
};
apiInstance.topicsListBySubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **filter** | **String**| The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;. | [optional] 
 **top** | **Number**| The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. | [optional] 

### Return type

[**TopicsListResult**](TopicsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topicsListEventTypes

> EventTypesListResult topicsListEventTypes(subscriptionId, resourceGroupName, providerNamespace, resourceTypeName, resourceName, apiVersion)

List topic event types

List event types for a topic

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.TopicsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let providerNamespace = "providerNamespace_example"; // String | Namespace of the provider of the topic
let resourceTypeName = "resourceTypeName_example"; // String | Name of the topic type
let resourceName = "resourceName_example"; // String | Name of the topic
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.topicsListEventTypes(subscriptionId, resourceGroupName, providerNamespace, resourceTypeName, resourceName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | 
 **providerNamespace** | **String**| Namespace of the provider of the topic | 
 **resourceTypeName** | **String**| Name of the topic type | 
 **resourceName** | **String**| Name of the topic | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**EventTypesListResult**](EventTypesListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topicsListSharedAccessKeys

> TopicSharedAccessKeys topicsListSharedAccessKeys(subscriptionId, resourceGroupName, topicName, apiVersion)

List keys for a topic

List the two keys used to publish to a topic

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.TopicsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let topicName = "topicName_example"; // String | Name of the topic
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.topicsListSharedAccessKeys(subscriptionId, resourceGroupName, topicName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | 
 **topicName** | **String**| Name of the topic | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**TopicSharedAccessKeys**](TopicSharedAccessKeys.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topicsRegenerateKey

> TopicSharedAccessKeys topicsRegenerateKey(subscriptionId, resourceGroupName, topicName, apiVersion, regenerateKeyRequest)

Regenerate key for a topic

Regenerate a shared access key for a topic

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.TopicsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let topicName = "topicName_example"; // String | Name of the topic
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let regenerateKeyRequest = new EventGridManagementClient.TopicRegenerateKeyRequest(); // TopicRegenerateKeyRequest | Request body to regenerate key
apiInstance.topicsRegenerateKey(subscriptionId, resourceGroupName, topicName, apiVersion, regenerateKeyRequest, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | 
 **topicName** | **String**| Name of the topic | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **regenerateKeyRequest** | [**TopicRegenerateKeyRequest**](TopicRegenerateKeyRequest.md)| Request body to regenerate key | 

### Return type

[**TopicSharedAccessKeys**](TopicSharedAccessKeys.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## topicsUpdate

> Topic topicsUpdate(subscriptionId, resourceGroupName, topicName, apiVersion, topicUpdateParameters)

Update a topic

Asynchronously updates a topic with the specified parameters.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.TopicsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let topicName = "topicName_example"; // String | Name of the topic
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let topicUpdateParameters = new EventGridManagementClient.TopicUpdateParameters(); // TopicUpdateParameters | Topic update information
apiInstance.topicsUpdate(subscriptionId, resourceGroupName, topicName, apiVersion, topicUpdateParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | 
 **topicName** | **String**| Name of the topic | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **topicUpdateParameters** | [**TopicUpdateParameters**](TopicUpdateParameters.md)| Topic update information | 

### Return type

[**Topic**](Topic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

