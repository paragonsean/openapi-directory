# IllumiDesk.NotificationsApi

All URIs are relative to *https://api.illumidesk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notificationRead**](NotificationsApi.md#notificationRead) | **GET** /v1/{namespace}/notifications/{notification_id} | Retrieve a specific notification.
[**notificationSettingsCreate**](NotificationsApi.md#notificationSettingsCreate) | **POST** /v1/{namespace}/notifications/settings/ | Create global notification settings
[**notificationSettingsEntityCreate**](NotificationsApi.md#notificationSettingsEntityCreate) | **POST** /v1/{namespace}/notifications/settings/entity/{entity} | Create global notification settings
[**notificationSettingsEntityRead**](NotificationsApi.md#notificationSettingsEntityRead) | **GET** /v1/{namespace}/notifications/settings/entity/{entity} | Retrieve global notification settings for the authenticated user
[**notificationSettingsEntityUpdate**](NotificationsApi.md#notificationSettingsEntityUpdate) | **PATCH** /v1/{namespace}/notifications/settings/entity/{entity} | Modify global notification settings.
[**notificationSettingsRead**](NotificationsApi.md#notificationSettingsRead) | **GET** /v1/{namespace}/notifications/settings/ | Retrieve global notification settings for the authenticated user
[**notificationSettingsUpdate**](NotificationsApi.md#notificationSettingsUpdate) | **PATCH** /v1/{namespace}/notifications/settings/ | Modify global notification settings.
[**notificationUpdate**](NotificationsApi.md#notificationUpdate) | **PATCH** /v1/{namespace}/notifications/{notification_id} | Mark a specific notification as either read or unread.
[**notificationsList**](NotificationsApi.md#notificationsList) | **GET** /v1/{namespace}/notifications/ | Get notifications of all types and entities for the authenticated user.
[**notificationsListEntity**](NotificationsApi.md#notificationsListEntity) | **GET** /v1/{namespace}/notifications/entity/{entity} | Get notifications of all types and entities for the authenticated user.
[**notificationsUpdateEntityList**](NotificationsApi.md#notificationsUpdateEntityList) | **PATCH** /v1/{namespace}/notifications/entity/{entity} | Mark a list of notifications as either read or unread.
[**notificationsUpdateList**](NotificationsApi.md#notificationsUpdateList) | **PATCH** /v1/{namespace}/notifications/ | Mark a list of notifications as either read or unread.



## notificationRead

> Notification notificationRead(namespace, notificationId)

Retrieve a specific notification.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.NotificationsApi();
let namespace = "namespace_example"; // String | User or team data.
let notificationId = "notificationId_example"; // String | Notification UUID.
apiInstance.notificationRead(namespace, notificationId, (error, data, response) => {
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
 **namespace** | **String**| User or team data. | 
 **notificationId** | **String**| Notification UUID. | 

### Return type

[**Notification**](Notification.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## notificationSettingsCreate

> NotificationSettings notificationSettingsCreate(namespace, notificationSettingsData)

Create global notification settings

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.NotificationsApi();
let namespace = "namespace_example"; // String | User or team name.
let notificationSettingsData = new IllumiDesk.NotificationSettingsData(); // NotificationSettingsData | 
apiInstance.notificationSettingsCreate(namespace, notificationSettingsData, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **notificationSettingsData** | [**NotificationSettingsData**](NotificationSettingsData.md)|  | 

### Return type

[**NotificationSettings**](NotificationSettings.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## notificationSettingsEntityCreate

> NotificationSettings notificationSettingsEntityCreate(namespace, entity, opts)

Create global notification settings

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.NotificationsApi();
let namespace = "namespace_example"; // String | User or team name.
let entity = "entity_example"; // String | Entity whose settings should be retrieved.
let opts = {
  'notificationSettingsData': new IllumiDesk.NotificationSettingsData() // NotificationSettingsData | 
};
apiInstance.notificationSettingsEntityCreate(namespace, entity, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **entity** | **String**| Entity whose settings should be retrieved. | 
 **notificationSettingsData** | [**NotificationSettingsData**](NotificationSettingsData.md)|  | [optional] 

### Return type

[**NotificationSettings**](NotificationSettings.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## notificationSettingsEntityRead

> [NotificationSettings] notificationSettingsEntityRead(namespace, entity)

Retrieve global notification settings for the authenticated user

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.NotificationsApi();
let namespace = "namespace_example"; // String | User or team data.
let entity = "entity_example"; // String | Entity whose settings should be retrieved.
apiInstance.notificationSettingsEntityRead(namespace, entity, (error, data, response) => {
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
 **namespace** | **String**| User or team data. | 
 **entity** | **String**| Entity whose settings should be retrieved. | 

### Return type

[**[NotificationSettings]**](NotificationSettings.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## notificationSettingsEntityUpdate

> NotificationSettings notificationSettingsEntityUpdate(namespace, entity, opts)

Modify global notification settings.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.NotificationsApi();
let namespace = "namespace_example"; // String | User or team name.
let entity = "entity_example"; // String | Entity whose settings should be retrieved.
let opts = {
  'notificationSettingsData': new IllumiDesk.NotificationSettingsData() // NotificationSettingsData | 
};
apiInstance.notificationSettingsEntityUpdate(namespace, entity, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **entity** | **String**| Entity whose settings should be retrieved. | 
 **notificationSettingsData** | [**NotificationSettingsData**](NotificationSettingsData.md)|  | [optional] 

### Return type

[**NotificationSettings**](NotificationSettings.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## notificationSettingsRead

> [NotificationSettings] notificationSettingsRead(namespace)

Retrieve global notification settings for the authenticated user

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.NotificationsApi();
let namespace = "namespace_example"; // String | User or team data.
apiInstance.notificationSettingsRead(namespace, (error, data, response) => {
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
 **namespace** | **String**| User or team data. | 

### Return type

[**[NotificationSettings]**](NotificationSettings.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## notificationSettingsUpdate

> NotificationSettings notificationSettingsUpdate(namespace, opts)

Modify global notification settings.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.NotificationsApi();
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'notificationSettingsData': new IllumiDesk.NotificationSettingsData() // NotificationSettingsData | 
};
apiInstance.notificationSettingsUpdate(namespace, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **notificationSettingsData** | [**NotificationSettingsData**](NotificationSettingsData.md)|  | [optional] 

### Return type

[**NotificationSettings**](NotificationSettings.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## notificationUpdate

> Notification notificationUpdate(namespace, notificationId, opts)

Mark a specific notification as either read or unread.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.NotificationsApi();
let namespace = "namespace_example"; // String | User or team data.
let notificationId = "notificationId_example"; // String | Notification UUID.
let opts = {
  'notificationData': new IllumiDesk.NotificationUpdateData() // NotificationUpdateData | 
};
apiInstance.notificationUpdate(namespace, notificationId, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team data. | 
 **notificationId** | **String**| Notification UUID. | 
 **notificationData** | [**NotificationUpdateData**](NotificationUpdateData.md)|  | [optional] 

### Return type

[**Notification**](Notification.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## notificationsList

> [Notification] notificationsList(namespace, opts)

Get notifications of all types and entities for the authenticated user.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.NotificationsApi();
let namespace = "namespace_example"; // String | User or team data.
let opts = {
  'limit': "limit_example", // String | Limit when getting items.
  'offset': "offset_example", // String | Offset when getting items.
  'ordering': "ordering_example", // String | Ordering when getting items.
  'read': true // Boolean | When true, get only read notifications. When false, get only unread notifications. Default behavior is to return both read and unread.
};
apiInstance.notificationsList(namespace, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team data. | 
 **limit** | **String**| Limit when getting items. | [optional] 
 **offset** | **String**| Offset when getting items. | [optional] 
 **ordering** | **String**| Ordering when getting items. | [optional] 
 **read** | **Boolean**| When true, get only read notifications. When false, get only unread notifications. Default behavior is to return both read and unread. | [optional] 

### Return type

[**[Notification]**](Notification.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## notificationsListEntity

> [Notification] notificationsListEntity(namespace, entity, opts)

Get notifications of all types and entities for the authenticated user.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.NotificationsApi();
let namespace = "namespace_example"; // String | User or team data.
let entity = "entity_example"; // String | Entity to filter notifications by.
let opts = {
  'limit': "limit_example", // String | Limit when getting items.
  'offset': "offset_example", // String | Offset when getting items.
  'ordering': "ordering_example", // String | Ordering when getting items.
  'read': true // Boolean | When true, get only read notifications. When false, get only unread notifications. Default behavior is to return both read and unread.
};
apiInstance.notificationsListEntity(namespace, entity, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team data. | 
 **entity** | **String**| Entity to filter notifications by. | 
 **limit** | **String**| Limit when getting items. | [optional] 
 **offset** | **String**| Offset when getting items. | [optional] 
 **ordering** | **String**| Ordering when getting items. | [optional] 
 **read** | **Boolean**| When true, get only read notifications. When false, get only unread notifications. Default behavior is to return both read and unread. | [optional] 

### Return type

[**[Notification]**](Notification.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## notificationsUpdateEntityList

> Notification notificationsUpdateEntityList(namespace, entity, notificationData)

Mark a list of notifications as either read or unread.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.NotificationsApi();
let namespace = "namespace_example"; // String | User or team name.
let entity = "entity_example"; // String | Entity to filter notifications by.
let notificationData = new IllumiDesk.NotificationListUpdateData(); // NotificationListUpdateData | 
apiInstance.notificationsUpdateEntityList(namespace, entity, notificationData, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **entity** | **String**| Entity to filter notifications by. | 
 **notificationData** | [**NotificationListUpdateData**](NotificationListUpdateData.md)|  | 

### Return type

[**Notification**](Notification.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## notificationsUpdateList

> Notification notificationsUpdateList(namespace, notificationData)

Mark a list of notifications as either read or unread.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.NotificationsApi();
let namespace = "namespace_example"; // String | User or team name.
let notificationData = new IllumiDesk.NotificationListUpdateData(); // NotificationListUpdateData | 
apiInstance.notificationsUpdateList(namespace, notificationData, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **notificationData** | [**NotificationListUpdateData**](NotificationListUpdateData.md)|  | 

### Return type

[**Notification**](Notification.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html

