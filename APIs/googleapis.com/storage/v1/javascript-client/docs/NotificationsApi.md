# CloudStorageJsonApi.NotificationsApi

All URIs are relative to *https://storage.googleapis.com/storage/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageNotificationsDelete**](NotificationsApi.md#storageNotificationsDelete) | **DELETE** /b/{bucket}/notificationConfigs/{notification} | 
[**storageNotificationsGet**](NotificationsApi.md#storageNotificationsGet) | **GET** /b/{bucket}/notificationConfigs/{notification} | 
[**storageNotificationsInsert**](NotificationsApi.md#storageNotificationsInsert) | **POST** /b/{bucket}/notificationConfigs | 
[**storageNotificationsList**](NotificationsApi.md#storageNotificationsList) | **GET** /b/{bucket}/notificationConfigs | 



## storageNotificationsDelete

> storageNotificationsDelete(bucket, notification, opts)



Permanently deletes a notification subscription.

### Example

```javascript
import CloudStorageJsonApi from 'cloud_storage_json_api';
let defaultClient = CloudStorageJsonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudStorageJsonApi.NotificationsApi();
let bucket = "bucket_example"; // String | The parent bucket of the notification.
let notification = "notification_example"; // String | ID of the notification to delete.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'userProject': "userProject_example" // String | The project to be billed for this request. Required for Requester Pays buckets.
};
apiInstance.storageNotificationsDelete(bucket, notification, opts, (error, data, response) => {
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
 **bucket** | **String**| The parent bucket of the notification. | 
 **notification** | **String**| ID of the notification to delete. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## storageNotificationsGet

> Notification storageNotificationsGet(bucket, notification, opts)



View a notification configuration.

### Example

```javascript
import CloudStorageJsonApi from 'cloud_storage_json_api';
let defaultClient = CloudStorageJsonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudStorageJsonApi.NotificationsApi();
let bucket = "bucket_example"; // String | The parent bucket of the notification.
let notification = "notification_example"; // String | Notification ID
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'userProject': "userProject_example" // String | The project to be billed for this request. Required for Requester Pays buckets.
};
apiInstance.storageNotificationsGet(bucket, notification, opts, (error, data, response) => {
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
 **bucket** | **String**| The parent bucket of the notification. | 
 **notification** | **String**| Notification ID | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 

### Return type

[**Notification**](Notification.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageNotificationsInsert

> Notification storageNotificationsInsert(bucket, opts)



Creates a notification subscription for a given bucket.

### Example

```javascript
import CloudStorageJsonApi from 'cloud_storage_json_api';
let defaultClient = CloudStorageJsonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudStorageJsonApi.NotificationsApi();
let bucket = "bucket_example"; // String | The parent bucket of the notification.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'userProject': "userProject_example", // String | The project to be billed for this request. Required for Requester Pays buckets.
  'notification': new CloudStorageJsonApi.Notification() // Notification | 
};
apiInstance.storageNotificationsInsert(bucket, opts, (error, data, response) => {
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
 **bucket** | **String**| The parent bucket of the notification. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 
 **notification** | [**Notification**](Notification.md)|  | [optional] 

### Return type

[**Notification**](Notification.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageNotificationsList

> Notifications storageNotificationsList(bucket, opts)



Retrieves a list of notification subscriptions for a given bucket.

### Example

```javascript
import CloudStorageJsonApi from 'cloud_storage_json_api';
let defaultClient = CloudStorageJsonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudStorageJsonApi.NotificationsApi();
let bucket = "bucket_example"; // String | Name of a Google Cloud Storage bucket.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'userProject': "userProject_example" // String | The project to be billed for this request. Required for Requester Pays buckets.
};
apiInstance.storageNotificationsList(bucket, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of a Google Cloud Storage bucket. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 

### Return type

[**Notifications**](Notifications.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

