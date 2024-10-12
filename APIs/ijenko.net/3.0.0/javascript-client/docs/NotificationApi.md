# IoEIoTApiToCreateEndUserApplications.NotificationApi

All URIs are relative to *https://ioe2api.ijenko.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notificationDelete**](NotificationApi.md#notificationDelete) | **DELETE** /notifications/{notificationId} | Delete a Notification
[**notificationGetMetadata**](NotificationApi.md#notificationGetMetadata) | **GET** /notifications/{notificationId}/metadata | List metadata
[**notificationPatch**](NotificationApi.md#notificationPatch) | **PATCH** /notifications/{notificationId} | Modify a Notification
[**notificationPatchMetadata**](NotificationApi.md#notificationPatchMetadata) | **PATCH** /notifications/{notificationId}/metadata | Modify metadata of a Notification
[**notificationsGet**](NotificationApi.md#notificationsGet) | **GET** /notifications/{notificationId} | Information about a Notification
[**placeNewNotification**](NotificationApi.md#placeNewNotification) | **POST** /places/{placeId}/notifications | Create a Notification
[**placeNotifications**](NotificationApi.md#placeNotifications) | **GET** /places/{placeId}/notifications | List Notifications



## notificationDelete

> notificationDelete(notificationId)

Delete a Notification

Delete a *Notification*. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.NotificationApi();
let notificationId = "notificationId_example"; // String | Unique identifier of a *Notification*.
apiInstance.notificationDelete(notificationId, (error, data, response) => {
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
 **notificationId** | **String**| Unique identifier of a *Notification*. | 

### Return type

null (empty response body)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## notificationGetMetadata

> {String: Object} notificationGetMetadata(notificationId)

List metadata

Get the metadata of the *Notification*.

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.NotificationApi();
let notificationId = "notificationId_example"; // String | Unique identifier of a *Notification*.
apiInstance.notificationGetMetadata(notificationId, (error, data, response) => {
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
 **notificationId** | **String**| Unique identifier of a *Notification*. | 

### Return type

**{String: Object}**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## notificationPatch

> notificationPatch(notificationId, notificationPatch)

Modify a Notification

Modify a *Notification*. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.NotificationApi();
let notificationId = "notificationId_example"; // String | Unique identifier of a *Notification*.
let notificationPatch = new IoEIoTApiToCreateEndUserApplications.NotificationPatch(); // NotificationPatch | 
apiInstance.notificationPatch(notificationId, notificationPatch, (error, data, response) => {
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
 **notificationId** | **String**| Unique identifier of a *Notification*. | 
 **notificationPatch** | [**NotificationPatch**](NotificationPatch.md)|  | 

### Return type

null (empty response body)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## notificationPatchMetadata

> {String: Object} notificationPatchMetadata(notificationId, metadataPatch)

Modify metadata of a Notification

Modify the metadata of a *Notification*. Keys are limited to the same format as tags (up to 21 characters, [a-z0-9], starting with [a-z]). Values can be any JSON value. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.NotificationApi();
let notificationId = "notificationId_example"; // String | Unique identifier of a *Notification*.
let metadataPatch = new IoEIoTApiToCreateEndUserApplications.MetadataPatch(); // MetadataPatch | Modifications to apply to the metadata of the resource. 
apiInstance.notificationPatchMetadata(notificationId, metadataPatch, (error, data, response) => {
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
 **notificationId** | **String**| Unique identifier of a *Notification*. | 
 **metadataPatch** | [**MetadataPatch**](MetadataPatch.md)| Modifications to apply to the metadata of the resource.  | 

### Return type

**{String: Object}**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## notificationsGet

> Notification notificationsGet(notificationId)

Information about a Notification

Get information about a *Notification*. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.NotificationApi();
let notificationId = "notificationId_example"; // String | Unique identifier of a *Notification*.
apiInstance.notificationsGet(notificationId, (error, data, response) => {
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
 **notificationId** | **String**| Unique identifier of a *Notification*. | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## placeNewNotification

> NotificationCreated placeNewNotification(placeId, notification)

Create a Notification

Create a new *Notification*.

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.NotificationApi();
let placeId = "placeId_example"; // String | Unique identifier of a *Place*.
let notification = new IoEIoTApiToCreateEndUserApplications.NotificationNew(); // NotificationNew | 
apiInstance.placeNewNotification(placeId, notification, (error, data, response) => {
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
 **placeId** | **String**| Unique identifier of a *Place*. | 
 **notification** | [**NotificationNew**](NotificationNew.md)|  | 

### Return type

[**NotificationCreated**](NotificationCreated.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## placeNotifications

> [NotificationItem] placeNotifications(placeId, opts)

List Notifications

Get the list of *Notifications* available in this *Place*.

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.NotificationApi();
let placeId = "placeId_example"; // String | Unique identifier of a *Place*.
let opts = {
  'embedMetadata': ["null"] // [String] | Request to include the given keys of metadata in the response. If a key doesn't exist on the resource it is ignored. **Note:** This only applies to the top level resources. 
};
apiInstance.placeNotifications(placeId, opts, (error, data, response) => {
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
 **placeId** | **String**| Unique identifier of a *Place*. | 
 **embedMetadata** | [**[String]**](String.md)| Request to include the given keys of metadata in the response. If a key doesn&#39;t exist on the resource it is ignored. **Note:** This only applies to the top level resources.  | [optional] 

### Return type

[**[NotificationItem]**](NotificationItem.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

