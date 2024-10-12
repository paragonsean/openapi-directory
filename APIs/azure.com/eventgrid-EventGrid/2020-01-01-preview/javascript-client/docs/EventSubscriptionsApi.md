# EventGridManagementClient.EventSubscriptionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventSubscriptionsCreateOrUpdate**](EventSubscriptionsApi.md#eventSubscriptionsCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{eventSubscriptionName} | Create or update an event subscription
[**eventSubscriptionsDelete**](EventSubscriptionsApi.md#eventSubscriptionsDelete) | **DELETE** /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{eventSubscriptionName} | Delete an event subscription
[**eventSubscriptionsGet**](EventSubscriptionsApi.md#eventSubscriptionsGet) | **GET** /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{eventSubscriptionName} | Get an event subscription
[**eventSubscriptionsGetFullUrl**](EventSubscriptionsApi.md#eventSubscriptionsGetFullUrl) | **POST** /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{eventSubscriptionName}/getFullUrl | Get full URL of an event subscription
[**eventSubscriptionsListByDomainTopic**](EventSubscriptionsApi.md#eventSubscriptionsListByDomainTopic) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/topics/{topicName}/providers/Microsoft.EventGrid/eventSubscriptions | List all event subscriptions for a specific domain topic
[**eventSubscriptionsListByResource**](EventSubscriptionsApi.md#eventSubscriptionsListByResource) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{providerNamespace}/{resourceTypeName}/{resourceName}/providers/Microsoft.EventGrid/eventSubscriptions | List all event subscriptions for a specific topic
[**eventSubscriptionsListGlobalByResourceGroup**](EventSubscriptionsApi.md#eventSubscriptionsListGlobalByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/eventSubscriptions | List all global event subscriptions under an Azure subscription and resource group
[**eventSubscriptionsListGlobalByResourceGroupForTopicType**](EventSubscriptionsApi.md#eventSubscriptionsListGlobalByResourceGroupForTopicType) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topicTypes/{topicTypeName}/eventSubscriptions | List all global event subscriptions under a resource group for a topic type
[**eventSubscriptionsListGlobalBySubscription**](EventSubscriptionsApi.md#eventSubscriptionsListGlobalBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EventGrid/eventSubscriptions | Get an aggregated list of all global event subscriptions under an Azure subscription
[**eventSubscriptionsListGlobalBySubscriptionForTopicType**](EventSubscriptionsApi.md#eventSubscriptionsListGlobalBySubscriptionForTopicType) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EventGrid/topicTypes/{topicTypeName}/eventSubscriptions | List all global event subscriptions for a topic type
[**eventSubscriptionsListRegionalByResourceGroup**](EventSubscriptionsApi.md#eventSubscriptionsListRegionalByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/locations/{location}/eventSubscriptions | List all regional event subscriptions under an Azure subscription and resource group
[**eventSubscriptionsListRegionalByResourceGroupForTopicType**](EventSubscriptionsApi.md#eventSubscriptionsListRegionalByResourceGroupForTopicType) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/locations/{location}/topicTypes/{topicTypeName}/eventSubscriptions | List all regional event subscriptions under an Azure subscription and resource group for a topic type
[**eventSubscriptionsListRegionalBySubscription**](EventSubscriptionsApi.md#eventSubscriptionsListRegionalBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EventGrid/locations/{location}/eventSubscriptions | List all regional event subscriptions under an Azure subscription
[**eventSubscriptionsListRegionalBySubscriptionForTopicType**](EventSubscriptionsApi.md#eventSubscriptionsListRegionalBySubscriptionForTopicType) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EventGrid/locations/{location}/topicTypes/{topicTypeName}/eventSubscriptions | List all regional event subscriptions under an Azure subscription for a topic type
[**eventSubscriptionsUpdate**](EventSubscriptionsApi.md#eventSubscriptionsUpdate) | **PATCH** /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{eventSubscriptionName} | Update an event subscription



## eventSubscriptionsCreateOrUpdate

> EventSubscription eventSubscriptionsCreateOrUpdate(scope, eventSubscriptionName, apiVersion, eventSubscriptionInfo)

Create or update an event subscription

Asynchronously creates a new event subscription or updates an existing event subscription based on the specified scope.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.EventSubscriptionsApi();
let scope = "scope_example"; // String | The identifier of the resource to which the event subscription needs to be created or updated. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use '/subscriptions/{subscriptionId}/' for a subscription, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for a resource group, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}' for a resource, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}' for an EventGrid topic.
let eventSubscriptionName = "eventSubscriptionName_example"; // String | Name of the event subscription. Event subscription names must be between 3 and 64 characters in length and should use alphanumeric letters only.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let eventSubscriptionInfo = new EventGridManagementClient.EventSubscription(); // EventSubscription | Event subscription properties containing the destination and filter information
apiInstance.eventSubscriptionsCreateOrUpdate(scope, eventSubscriptionName, apiVersion, eventSubscriptionInfo, (error, data, response) => {
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
 **scope** | **String**| The identifier of the resource to which the event subscription needs to be created or updated. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic. | 
 **eventSubscriptionName** | **String**| Name of the event subscription. Event subscription names must be between 3 and 64 characters in length and should use alphanumeric letters only. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **eventSubscriptionInfo** | [**EventSubscription**](EventSubscription.md)| Event subscription properties containing the destination and filter information | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## eventSubscriptionsDelete

> eventSubscriptionsDelete(scope, eventSubscriptionName, apiVersion)

Delete an event subscription

Delete an existing event subscription

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.EventSubscriptionsApi();
let scope = "scope_example"; // String | The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use '/subscriptions/{subscriptionId}/' for a subscription, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for a resource group, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}' for a resource, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}' for an EventGrid topic.
let eventSubscriptionName = "eventSubscriptionName_example"; // String | Name of the event subscription
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.eventSubscriptionsDelete(scope, eventSubscriptionName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic. | 
 **eventSubscriptionName** | **String**| Name of the event subscription | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## eventSubscriptionsGet

> EventSubscription eventSubscriptionsGet(scope, eventSubscriptionName, apiVersion)

Get an event subscription

Get properties of an event subscription

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.EventSubscriptionsApi();
let scope = "scope_example"; // String | The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use '/subscriptions/{subscriptionId}/' for a subscription, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for a resource group, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}' for a resource, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}' for an EventGrid topic.
let eventSubscriptionName = "eventSubscriptionName_example"; // String | Name of the event subscription
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.eventSubscriptionsGet(scope, eventSubscriptionName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic. | 
 **eventSubscriptionName** | **String**| Name of the event subscription | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSubscriptionsGetFullUrl

> EventSubscriptionFullUrl eventSubscriptionsGetFullUrl(scope, eventSubscriptionName, apiVersion)

Get full URL of an event subscription

Get the full endpoint URL for an event subscription

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.EventSubscriptionsApi();
let scope = "scope_example"; // String | The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use '/subscriptions/{subscriptionId}/' for a subscription, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for a resource group, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}' for a resource, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}' for an EventGrid topic.
let eventSubscriptionName = "eventSubscriptionName_example"; // String | Name of the event subscription
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.eventSubscriptionsGetFullUrl(scope, eventSubscriptionName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic. | 
 **eventSubscriptionName** | **String**| Name of the event subscription | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**EventSubscriptionFullUrl**](EventSubscriptionFullUrl.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSubscriptionsListByDomainTopic

> EventSubscriptionsListResult eventSubscriptionsListByDomainTopic(subscriptionId, resourceGroupName, domainName, topicName, apiVersion, opts)

List all event subscriptions for a specific domain topic

List all event subscriptions that have been created for a specific domain topic

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.EventSubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let domainName = "domainName_example"; // String | Name of the top level domain
let topicName = "topicName_example"; // String | Name of the domain topic
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.
  'top': 56 // Number | The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
};
apiInstance.eventSubscriptionsListByDomainTopic(subscriptionId, resourceGroupName, domainName, topicName, apiVersion, opts, (error, data, response) => {
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
 **domainName** | **String**| Name of the top level domain | 
 **topicName** | **String**| Name of the domain topic | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **filter** | **String**| The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;. | [optional] 
 **top** | **Number**| The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. | [optional] 

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSubscriptionsListByResource

> EventSubscriptionsListResult eventSubscriptionsListByResource(subscriptionId, resourceGroupName, providerNamespace, resourceTypeName, resourceName, apiVersion, opts)

List all event subscriptions for a specific topic

List all event subscriptions that have been created for a specific topic

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.EventSubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let providerNamespace = "providerNamespace_example"; // String | Namespace of the provider of the topic
let resourceTypeName = "resourceTypeName_example"; // String | Name of the resource type
let resourceName = "resourceName_example"; // String | Name of the resource
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.
  'top': 56 // Number | The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
};
apiInstance.eventSubscriptionsListByResource(subscriptionId, resourceGroupName, providerNamespace, resourceTypeName, resourceName, apiVersion, opts, (error, data, response) => {
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
 **resourceTypeName** | **String**| Name of the resource type | 
 **resourceName** | **String**| Name of the resource | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **filter** | **String**| The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;. | [optional] 
 **top** | **Number**| The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. | [optional] 

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSubscriptionsListGlobalByResourceGroup

> EventSubscriptionsListResult eventSubscriptionsListGlobalByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)

List all global event subscriptions under an Azure subscription and resource group

List all global event subscriptions under a specific Azure subscription and resource group

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.EventSubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.
  'top': 56 // Number | The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
};
apiInstance.eventSubscriptionsListGlobalByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSubscriptionsListGlobalByResourceGroupForTopicType

> EventSubscriptionsListResult eventSubscriptionsListGlobalByResourceGroupForTopicType(subscriptionId, resourceGroupName, topicTypeName, apiVersion, opts)

List all global event subscriptions under a resource group for a topic type

List all global event subscriptions under a resource group for a specific topic type.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.EventSubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let topicTypeName = "topicTypeName_example"; // String | Name of the topic type
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.
  'top': 56 // Number | The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
};
apiInstance.eventSubscriptionsListGlobalByResourceGroupForTopicType(subscriptionId, resourceGroupName, topicTypeName, apiVersion, opts, (error, data, response) => {
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
 **topicTypeName** | **String**| Name of the topic type | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **filter** | **String**| The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;. | [optional] 
 **top** | **Number**| The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. | [optional] 

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSubscriptionsListGlobalBySubscription

> EventSubscriptionsListResult eventSubscriptionsListGlobalBySubscription(subscriptionId, apiVersion, opts)

Get an aggregated list of all global event subscriptions under an Azure subscription

List all aggregated global event subscriptions under a specific Azure subscription

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.EventSubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.
  'top': 56 // Number | The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
};
apiInstance.eventSubscriptionsListGlobalBySubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSubscriptionsListGlobalBySubscriptionForTopicType

> EventSubscriptionsListResult eventSubscriptionsListGlobalBySubscriptionForTopicType(subscriptionId, topicTypeName, apiVersion, opts)

List all global event subscriptions for a topic type

List all global event subscriptions under an Azure subscription for a topic type.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.EventSubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let topicTypeName = "topicTypeName_example"; // String | Name of the topic type
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.
  'top': 56 // Number | The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
};
apiInstance.eventSubscriptionsListGlobalBySubscriptionForTopicType(subscriptionId, topicTypeName, apiVersion, opts, (error, data, response) => {
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
 **topicTypeName** | **String**| Name of the topic type | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **filter** | **String**| The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;. | [optional] 
 **top** | **Number**| The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. | [optional] 

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSubscriptionsListRegionalByResourceGroup

> EventSubscriptionsListResult eventSubscriptionsListRegionalByResourceGroup(subscriptionId, resourceGroupName, location, apiVersion, opts)

List all regional event subscriptions under an Azure subscription and resource group

List all event subscriptions from the given location under a specific Azure subscription and resource group

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.EventSubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let location = "location_example"; // String | Name of the location
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.
  'top': 56 // Number | The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
};
apiInstance.eventSubscriptionsListRegionalByResourceGroup(subscriptionId, resourceGroupName, location, apiVersion, opts, (error, data, response) => {
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
 **location** | **String**| Name of the location | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **filter** | **String**| The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;. | [optional] 
 **top** | **Number**| The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. | [optional] 

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSubscriptionsListRegionalByResourceGroupForTopicType

> EventSubscriptionsListResult eventSubscriptionsListRegionalByResourceGroupForTopicType(subscriptionId, resourceGroupName, location, topicTypeName, apiVersion, opts)

List all regional event subscriptions under an Azure subscription and resource group for a topic type

List all event subscriptions from the given location under a specific Azure subscription and resource group and topic type

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.EventSubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let location = "location_example"; // String | Name of the location
let topicTypeName = "topicTypeName_example"; // String | Name of the topic type
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.
  'top': 56 // Number | The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
};
apiInstance.eventSubscriptionsListRegionalByResourceGroupForTopicType(subscriptionId, resourceGroupName, location, topicTypeName, apiVersion, opts, (error, data, response) => {
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
 **location** | **String**| Name of the location | 
 **topicTypeName** | **String**| Name of the topic type | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **filter** | **String**| The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;. | [optional] 
 **top** | **Number**| The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. | [optional] 

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSubscriptionsListRegionalBySubscription

> EventSubscriptionsListResult eventSubscriptionsListRegionalBySubscription(subscriptionId, location, apiVersion, opts)

List all regional event subscriptions under an Azure subscription

List all event subscriptions from the given location under a specific Azure subscription

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.EventSubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Name of the location
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.
  'top': 56 // Number | The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
};
apiInstance.eventSubscriptionsListRegionalBySubscription(subscriptionId, location, apiVersion, opts, (error, data, response) => {
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
 **location** | **String**| Name of the location | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **filter** | **String**| The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;. | [optional] 
 **top** | **Number**| The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. | [optional] 

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSubscriptionsListRegionalBySubscriptionForTopicType

> EventSubscriptionsListResult eventSubscriptionsListRegionalBySubscriptionForTopicType(subscriptionId, location, topicTypeName, apiVersion, opts)

List all regional event subscriptions under an Azure subscription for a topic type

List all event subscriptions from the given location under a specific Azure subscription and topic type.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.EventSubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Name of the location
let topicTypeName = "topicTypeName_example"; // String | Name of the topic type
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.
  'top': 56 // Number | The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
};
apiInstance.eventSubscriptionsListRegionalBySubscriptionForTopicType(subscriptionId, location, topicTypeName, apiVersion, opts, (error, data, response) => {
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
 **location** | **String**| Name of the location | 
 **topicTypeName** | **String**| Name of the topic type | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **filter** | **String**| The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;. | [optional] 
 **top** | **Number**| The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. | [optional] 

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSubscriptionsUpdate

> EventSubscription eventSubscriptionsUpdate(scope, eventSubscriptionName, apiVersion, eventSubscriptionUpdateParameters)

Update an event subscription

Asynchronously updates an existing event subscription.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.EventSubscriptionsApi();
let scope = "scope_example"; // String | The scope of existing event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use '/subscriptions/{subscriptionId}/' for a subscription, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for a resource group, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}' for a resource, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}' for an EventGrid topic.
let eventSubscriptionName = "eventSubscriptionName_example"; // String | Name of the event subscription to be updated
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let eventSubscriptionUpdateParameters = new EventGridManagementClient.EventSubscriptionUpdateParameters(); // EventSubscriptionUpdateParameters | Updated event subscription information
apiInstance.eventSubscriptionsUpdate(scope, eventSubscriptionName, apiVersion, eventSubscriptionUpdateParameters, (error, data, response) => {
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
 **scope** | **String**| The scope of existing event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic. | 
 **eventSubscriptionName** | **String**| Name of the event subscription to be updated | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **eventSubscriptionUpdateParameters** | [**EventSubscriptionUpdateParameters**](EventSubscriptionUpdateParameters.md)| Updated event subscription information | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

