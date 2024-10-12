# FilesComApi.BundleNotificationsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteBundleNotificationsId**](BundleNotificationsApi.md#deleteBundleNotificationsId) | **DELETE** /bundle_notifications/{id} | Delete Bundle Notification
[**getBundleNotifications**](BundleNotificationsApi.md#getBundleNotifications) | **GET** /bundle_notifications | List Bundle Notifications
[**getBundleNotificationsId**](BundleNotificationsApi.md#getBundleNotificationsId) | **GET** /bundle_notifications/{id} | Show Bundle Notification
[**patchBundleNotificationsId**](BundleNotificationsApi.md#patchBundleNotificationsId) | **PATCH** /bundle_notifications/{id} | Update Bundle Notification
[**postBundleNotifications**](BundleNotificationsApi.md#postBundleNotifications) | **POST** /bundle_notifications | Create Bundle Notification



## deleteBundleNotificationsId

> deleteBundleNotificationsId(id)

Delete Bundle Notification

Delete Bundle Notification

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BundleNotificationsApi();
let id = 56; // Number | Bundle Notification ID.
apiInstance.deleteBundleNotificationsId(id, (error, data, response) => {
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
 **id** | **Number**| Bundle Notification ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBundleNotifications

> [BundleNotificationEntity] getBundleNotifications(opts)

List Bundle Notifications

List Bundle Notifications

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BundleNotificationsApi();
let opts = {
  'userId': 56, // Number | User ID.  Provide a value of `0` to operate the current session's user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[bundle_id]=desc`). Valid fields are `bundle_id`.
  'bundleId': "bundleId_example", // String | If set, return records where the specified field is equal to the supplied value.
  'filter': {key: null} // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `bundle_id`.
};
apiInstance.getBundleNotifications(opts, (error, data, response) => {
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
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[bundle_id]&#x3D;desc&#x60;). Valid fields are &#x60;bundle_id&#x60;. | [optional] 
 **bundleId** | **String**| If set, return records where the specified field is equal to the supplied value. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;bundle_id&#x60;. | [optional] 

### Return type

[**[BundleNotificationEntity]**](BundleNotificationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBundleNotificationsId

> BundleNotificationEntity getBundleNotificationsId(id)

Show Bundle Notification

Show Bundle Notification

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BundleNotificationsApi();
let id = 56; // Number | Bundle Notification ID.
apiInstance.getBundleNotificationsId(id, (error, data, response) => {
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
 **id** | **Number**| Bundle Notification ID. | 

### Return type

[**BundleNotificationEntity**](BundleNotificationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchBundleNotificationsId

> BundleNotificationEntity patchBundleNotificationsId(id, opts)

Update Bundle Notification

Update Bundle Notification

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BundleNotificationsApi();
let id = 56; // Number | Bundle Notification ID.
let opts = {
  'notifyOnRegistration': true, // Boolean | Triggers bundle notification when a registration action occurs for it.
  'notifyOnUpload': true // Boolean | Triggers bundle notification when a upload action occurs for it.
};
apiInstance.patchBundleNotificationsId(id, opts, (error, data, response) => {
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
 **id** | **Number**| Bundle Notification ID. | 
 **notifyOnRegistration** | **Boolean**| Triggers bundle notification when a registration action occurs for it. | [optional] 
 **notifyOnUpload** | **Boolean**| Triggers bundle notification when a upload action occurs for it. | [optional] 

### Return type

[**BundleNotificationEntity**](BundleNotificationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postBundleNotifications

> BundleNotificationEntity postBundleNotifications(bundleId, opts)

Create Bundle Notification

Create Bundle Notification

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BundleNotificationsApi();
let bundleId = 56; // Number | Bundle ID to notify on
let opts = {
  'notifyOnRegistration': true, // Boolean | Triggers bundle notification when a registration action occurs for it.
  'notifyOnUpload': true, // Boolean | Triggers bundle notification when a upload action occurs for it.
  'userId': 56 // Number | The id of the user to notify.
};
apiInstance.postBundleNotifications(bundleId, opts, (error, data, response) => {
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
 **bundleId** | **Number**| Bundle ID to notify on | 
 **notifyOnRegistration** | **Boolean**| Triggers bundle notification when a registration action occurs for it. | [optional] 
 **notifyOnUpload** | **Boolean**| Triggers bundle notification when a upload action occurs for it. | [optional] 
 **userId** | **Number**| The id of the user to notify. | [optional] 

### Return type

[**BundleNotificationEntity**](BundleNotificationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

