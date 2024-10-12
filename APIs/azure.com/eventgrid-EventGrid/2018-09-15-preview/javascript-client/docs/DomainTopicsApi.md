# EventGridManagementClient.DomainTopicsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domainTopicsGet**](DomainTopicsApi.md#domainTopicsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/topics/{topicName} | Get a domain topic
[**domainTopicsListByDomain**](DomainTopicsApi.md#domainTopicsListByDomain) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/topics | List domain topics.



## domainTopicsGet

> DomainTopic domainTopicsGet(subscriptionId, resourceGroupName, domainName, topicName, apiVersion)

Get a domain topic

Get properties of a domain topic

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.DomainTopicsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
let domainName = "domainName_example"; // String | Name of the domain
let topicName = "topicName_example"; // String | Name of the topic
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.domainTopicsGet(subscriptionId, resourceGroupName, domainName, topicName, apiVersion, (error, data, response) => {
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
 **topicName** | **String**| Name of the topic | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**DomainTopic**](DomainTopic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainTopicsListByDomain

> DomainTopicsListResult domainTopicsListByDomain(subscriptionId, resourceGroupName, domainName, apiVersion)

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
apiInstance.domainTopicsListByDomain(subscriptionId, resourceGroupName, domainName, apiVersion, (error, data, response) => {
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

### Return type

[**DomainTopicsListResult**](DomainTopicsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

