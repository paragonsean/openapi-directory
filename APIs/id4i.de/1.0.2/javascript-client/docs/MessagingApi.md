# Id4iApi.MessagingApi

All URIs are relative to *http://backend.id4i.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enqueueCustomMessage**](MessagingApi.md#enqueueCustomMessage) | **POST** /api/v1/organizations/{organizationId}/messaging/enqueueCustomMessage | Enqueue a custom message
[**getDefaultQueue**](MessagingApi.md#getDefaultQueue) | **GET** /api/v1/organizations/{organizationId}/messaging | 
[**patchDefaultQueue**](MessagingApi.md#patchDefaultQueue) | **PATCH** /api/v1/organizations/{organizationId}/messaging | 



## enqueueCustomMessage

> enqueueCustomMessage(organizationId, sendCustomMessage)

Enqueue a custom message

Enqueue a custom organisation message with custom data.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.MessagingApi();
let organizationId = "organizationId_example"; // String | The organisation namespace
let sendCustomMessage = new Id4iApi.SendCustomMessage(); // SendCustomMessage | request
apiInstance.enqueueCustomMessage(organizationId, sendCustomMessage, (error, data, response) => {
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
 **organizationId** | **String**| The organisation namespace | 
 **sendCustomMessage** | [**SendCustomMessage**](SendCustomMessage.md)| request | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## getDefaultQueue

> QueuePresentation getDefaultQueue(organizationId)



### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.MessagingApi();
let organizationId = "organizationId_example"; // String | organizationId
apiInstance.getDefaultQueue(organizationId, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 

### Return type

[**QueuePresentation**](QueuePresentation.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## patchDefaultQueue

> patchDefaultQueue(organizationId, queueUpdateRequest)



### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.MessagingApi();
let organizationId = "organizationId_example"; // String | organizationId
let queueUpdateRequest = new Id4iApi.QueueUpdateRequest(); // QueueUpdateRequest | request
apiInstance.patchDefaultQueue(organizationId, queueUpdateRequest, (error, data, response) => {
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
 **organizationId** | **String**| organizationId | 
 **queueUpdateRequest** | [**QueueUpdateRequest**](QueueUpdateRequest.md)| request | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: Not defined

