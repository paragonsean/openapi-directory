# EventGridManagementClient.DomainTopicsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domainTopicsCreateOrUpdate**](DomainTopicsApi.md#domainTopicsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/topics/{domainTopicName} | Create or update a domain topic
[**domainTopicsDelete**](DomainTopicsApi.md#domainTopicsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/topics/{domainTopicName} | Delete a domain topic
[**domainTopicsGet**](DomainTopicsApi.md#domainTopicsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/topics/{domainTopicName} | Get a domain topic
[**domainTopicsListByDomain**](DomainTopicsApi.md#domainTopicsListByDomain) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/topics | List domain topics.



## domainTopicsCreateOrUpdate

> DomainTopic domainTopicsCreateOrUpdate(subscriptionId, resourceGroupName, domainName, domainTopicName, apiVersion)

Create or update a domain topic

Asynchronously creates or updates a new domain topic with the specified parameters.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.DomainTopicsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let domainName = "domainName_example"; // String | Name of the domain
let domainTopicName = "domainTopicName_example"; // String | Name of the domain topic
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.domainTopicsCreateOrUpdate(subscriptionId, resourceGroupName, domainName, domainTopicName, apiVersion, (error, data, response) => {
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
 **domainName** | **String**| Name of the domain | 
 **domainTopicName** | **String**| Name of the domain topic | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**DomainTopic**](DomainTopic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainTopicsDelete

> domainTopicsDelete(subscriptionId, resourceGroupName, domainName, domainTopicName, apiVersion)

Delete a domain topic

Delete existing domain topic

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.DomainTopicsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let domainName = "domainName_example"; // String | Name of the domain
let domainTopicName = "domainTopicName_example"; // String | Name of the domain topic
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.domainTopicsDelete(subscriptionId, resourceGroupName, domainName, domainTopicName, apiVersion, (error, data, response) => {
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
 **domainName** | **String**| Name of the domain | 
 **domainTopicName** | **String**| Name of the domain topic | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## domainTopicsGet

> DomainTopic domainTopicsGet(subscriptionId, resourceGroupName, domainName, domainTopicName, apiVersion)

Get a domain topic

Get properties of a domain topic

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.DomainTopicsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let domainName = "domainName_example"; // String | Name of the domain
let domainTopicName = "domainTopicName_example"; // String | Name of the topic
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.domainTopicsGet(subscriptionId, resourceGroupName, domainName, domainTopicName, apiVersion, (error, data, response) => {
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
 **domainName** | **String**| Name of the domain | 
 **domainTopicName** | **String**| Name of the topic | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**DomainTopic**](DomainTopic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainTopicsListByDomain

> DomainTopicsListResult domainTopicsListByDomain(subscriptionId, resourceGroupName, domainName, apiVersion, opts)

List domain topics.

List all the topics in a domain.

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.DomainTopicsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let domainName = "domainName_example"; // String | Domain name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | Filter the results using OData syntax.
  'top': 56 // Number | The number of results to return.
};
apiInstance.domainTopicsListByDomain(subscriptionId, resourceGroupName, domainName, apiVersion, opts, (error, data, response) => {
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
 **domainName** | **String**| Domain name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **filter** | **String**| Filter the results using OData syntax. | [optional] 
 **top** | **Number**| The number of results to return. | [optional] 

### Return type

[**DomainTopicsListResult**](DomainTopicsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

