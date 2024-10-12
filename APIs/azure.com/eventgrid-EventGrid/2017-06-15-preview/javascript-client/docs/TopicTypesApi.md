# EventGridManagementClient.TopicTypesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**topicTypesGet**](TopicTypesApi.md#topicTypesGet) | **GET** /providers/Microsoft.EventGrid/topicTypes/{topicTypeName} | Get a topic type
[**topicTypesList**](TopicTypesApi.md#topicTypesList) | **GET** /providers/Microsoft.EventGrid/topicTypes | List topic types
[**topicTypesListEventTypes**](TopicTypesApi.md#topicTypesListEventTypes) | **GET** /providers/Microsoft.EventGrid/topicTypes/{topicTypeName}/eventTypes | List event types



## topicTypesGet

> TopicTypeInfo topicTypesGet(topicTypeName, apiVersion)

Get a topic type

Get information about a topic type

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.TopicTypesApi();
let topicTypeName = "topicTypeName_example"; // String | Name of the topic type
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.topicTypesGet(topicTypeName, apiVersion, (error, data, response) => {
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
 **topicTypeName** | **String**| Name of the topic type | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**TopicTypeInfo**](TopicTypeInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topicTypesList

> TopicTypesListResult topicTypesList(apiVersion)

List topic types

List all registered topic types

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.TopicTypesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.topicTypesList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**TopicTypesListResult**](TopicTypesListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topicTypesListEventTypes

> EventTypesListResult topicTypesListEventTypes(topicTypeName, apiVersion)

List event types

List event types for a topic type

### Example

```javascript
import EventGridManagementClient from 'event_grid_management_client';

let apiInstance = new EventGridManagementClient.TopicTypesApi();
let topicTypeName = "topicTypeName_example"; // String | Name of the topic type
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.topicTypesListEventTypes(topicTypeName, apiVersion, (error, data, response) => {
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
 **topicTypeName** | **String**| Name of the topic type | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**EventTypesListResult**](EventTypesListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

