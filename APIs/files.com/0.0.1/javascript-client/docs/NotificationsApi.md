# FilesComApi.NotificationsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteNotificationsId**](NotificationsApi.md#deleteNotificationsId) | **DELETE** /notifications/{id} | Delete Notification
[**getNotifications**](NotificationsApi.md#getNotifications) | **GET** /notifications | List Notifications
[**getNotificationsId**](NotificationsApi.md#getNotificationsId) | **GET** /notifications/{id} | Show Notification
[**patchNotificationsId**](NotificationsApi.md#patchNotificationsId) | **PATCH** /notifications/{id} | Update Notification
[**postNotifications**](NotificationsApi.md#postNotifications) | **POST** /notifications | Create Notification



## deleteNotificationsId

> deleteNotificationsId(id)

Delete Notification

Delete Notification

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.NotificationsApi();
let id = 56; // Number | Notification ID.
apiInstance.deleteNotificationsId(id, (error, data, response) => {
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
 **id** | **Number**| Notification ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotifications

> [NotificationEntity] getNotifications(opts)

List Notifications

List Notifications

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.NotificationsApi();
let opts = {
  'userId': 56, // Number | DEPRECATED: Show notifications for this User ID. Use `filter[user_id]` instead.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[path]=desc`). Valid fields are `path`, `user_id` or `group_id`.
  'groupId': "groupId_example", // String | If set, return records where the specified field is equal to the supplied value.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `path`, `user_id` or `group_id`.
  'filterPrefix': {key: null}, // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `path`.
  'path': "path_example", // String | Show notifications for this Path.
  'includeAncestors': true // Boolean | If `include_ancestors` is `true` and `path` is specified, include notifications for any parent paths. Ignored if `path` is not specified.
};
apiInstance.getNotifications(opts, (error, data, response) => {
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
 **userId** | **Number**| DEPRECATED: Show notifications for this User ID. Use &#x60;filter[user_id]&#x60; instead. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[path]&#x3D;desc&#x60;). Valid fields are &#x60;path&#x60;, &#x60;user_id&#x60; or &#x60;group_id&#x60;. | [optional] 
 **groupId** | **String**| If set, return records where the specified field is equal to the supplied value. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;path&#x60;, &#x60;user_id&#x60; or &#x60;group_id&#x60;. | [optional] 
 **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;path&#x60;. | [optional] 
 **path** | **String**| Show notifications for this Path. | [optional] 
 **includeAncestors** | **Boolean**| If &#x60;include_ancestors&#x60; is &#x60;true&#x60; and &#x60;path&#x60; is specified, include notifications for any parent paths. Ignored if &#x60;path&#x60; is not specified. | [optional] 

### Return type

[**[NotificationEntity]**](NotificationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNotificationsId

> NotificationEntity getNotificationsId(id)

Show Notification

Show Notification

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.NotificationsApi();
let id = 56; // Number | Notification ID.
apiInstance.getNotificationsId(id, (error, data, response) => {
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
 **id** | **Number**| Notification ID. | 

### Return type

[**NotificationEntity**](NotificationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchNotificationsId

> NotificationEntity patchNotificationsId(id, opts)

Update Notification

Update Notification

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.NotificationsApi();
let id = 56; // Number | Notification ID.
let opts = {
  'message': "message_example", // String | Custom message to include in notification emails.
  'notifyOnCopy': true, // Boolean | If `true`, copying or moving resources into this path will trigger a notification, in addition to just uploads.
  'notifyOnDelete': true, // Boolean | Triggers notification when deleting files from this path
  'notifyOnDownload': true, // Boolean | Triggers notification when downloading files from this path
  'notifyOnMove': true, // Boolean | Triggers notification when moving files to this path
  'notifyOnUpload': true, // Boolean | Triggers notification when uploading new files to this path
  'notifyUserActions': true, // Boolean | If `true` actions initiated by the user will still result in a notification
  'recursive': true, // Boolean | If `true`, enable notifications for each subfolder in this path
  'sendInterval': "sendInterval_example", // String | The time interval that notifications are aggregated by.  Can be `five_minutes`, `fifteen_minutes`, `hourly`, or `daily`.
  'triggerByShareRecipients': true, // Boolean | Notify when actions are performed by a share recipient?
  'triggeringFilenames': ["null"], // [String] | Array of filenames (possibly with wildcards) to match for action path
  'triggeringGroupIds': [null], // [Number] | Only notify on actions made by a member of one of the specified groups
  'triggeringUserIds': [null] // [Number] | Only notify on actions made one of the specified users
};
apiInstance.patchNotificationsId(id, opts, (error, data, response) => {
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
 **id** | **Number**| Notification ID. | 
 **message** | **String**| Custom message to include in notification emails. | [optional] 
 **notifyOnCopy** | **Boolean**| If &#x60;true&#x60;, copying or moving resources into this path will trigger a notification, in addition to just uploads. | [optional] 
 **notifyOnDelete** | **Boolean**| Triggers notification when deleting files from this path | [optional] 
 **notifyOnDownload** | **Boolean**| Triggers notification when downloading files from this path | [optional] 
 **notifyOnMove** | **Boolean**| Triggers notification when moving files to this path | [optional] 
 **notifyOnUpload** | **Boolean**| Triggers notification when uploading new files to this path | [optional] 
 **notifyUserActions** | **Boolean**| If &#x60;true&#x60; actions initiated by the user will still result in a notification | [optional] 
 **recursive** | **Boolean**| If &#x60;true&#x60;, enable notifications for each subfolder in this path | [optional] 
 **sendInterval** | **String**| The time interval that notifications are aggregated by.  Can be &#x60;five_minutes&#x60;, &#x60;fifteen_minutes&#x60;, &#x60;hourly&#x60;, or &#x60;daily&#x60;. | [optional] 
 **triggerByShareRecipients** | **Boolean**| Notify when actions are performed by a share recipient? | [optional] 
 **triggeringFilenames** | [**[String]**](String.md)| Array of filenames (possibly with wildcards) to match for action path | [optional] 
 **triggeringGroupIds** | [**[Number]**](Number.md)| Only notify on actions made by a member of one of the specified groups | [optional] 
 **triggeringUserIds** | [**[Number]**](Number.md)| Only notify on actions made one of the specified users | [optional] 

### Return type

[**NotificationEntity**](NotificationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postNotifications

> NotificationEntity postNotifications(opts)

Create Notification

Create Notification

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.NotificationsApi();
let opts = {
  'groupId': 56, // Number | The ID of the group to notify.  Provide `user_id`, `username` or `group_id`.
  'message': "message_example", // String | Custom message to include in notification emails.
  'notifyOnCopy': true, // Boolean | If `true`, copying or moving resources into this path will trigger a notification, in addition to just uploads.
  'notifyOnDelete': true, // Boolean | Triggers notification when deleting files from this path
  'notifyOnDownload': true, // Boolean | Triggers notification when downloading files from this path
  'notifyOnMove': true, // Boolean | Triggers notification when moving files to this path
  'notifyOnUpload': true, // Boolean | Triggers notification when uploading new files to this path
  'notifyUserActions': true, // Boolean | If `true` actions initiated by the user will still result in a notification
  'path': "path_example", // String | Path
  'recursive': true, // Boolean | If `true`, enable notifications for each subfolder in this path
  'sendInterval': "sendInterval_example", // String | The time interval that notifications are aggregated by.  Can be `five_minutes`, `fifteen_minutes`, `hourly`, or `daily`.
  'triggerByShareRecipients': true, // Boolean | Notify when actions are performed by a share recipient?
  'triggeringFilenames': ["null"], // [String] | Array of filenames (possibly with wildcards) to match for action path
  'triggeringGroupIds': [null], // [Number] | Only notify on actions made by a member of one of the specified groups
  'triggeringUserIds': [null], // [Number] | Only notify on actions made one of the specified users
  'userId': 56, // Number | The id of the user to notify. Provide `user_id`, `username` or `group_id`.
  'username': "username_example" // String | The username of the user to notify.  Provide `user_id`, `username` or `group_id`.
};
apiInstance.postNotifications(opts, (error, data, response) => {
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
 **groupId** | **Number**| The ID of the group to notify.  Provide &#x60;user_id&#x60;, &#x60;username&#x60; or &#x60;group_id&#x60;. | [optional] 
 **message** | **String**| Custom message to include in notification emails. | [optional] 
 **notifyOnCopy** | **Boolean**| If &#x60;true&#x60;, copying or moving resources into this path will trigger a notification, in addition to just uploads. | [optional] 
 **notifyOnDelete** | **Boolean**| Triggers notification when deleting files from this path | [optional] 
 **notifyOnDownload** | **Boolean**| Triggers notification when downloading files from this path | [optional] 
 **notifyOnMove** | **Boolean**| Triggers notification when moving files to this path | [optional] 
 **notifyOnUpload** | **Boolean**| Triggers notification when uploading new files to this path | [optional] 
 **notifyUserActions** | **Boolean**| If &#x60;true&#x60; actions initiated by the user will still result in a notification | [optional] 
 **path** | **String**| Path | [optional] 
 **recursive** | **Boolean**| If &#x60;true&#x60;, enable notifications for each subfolder in this path | [optional] 
 **sendInterval** | **String**| The time interval that notifications are aggregated by.  Can be &#x60;five_minutes&#x60;, &#x60;fifteen_minutes&#x60;, &#x60;hourly&#x60;, or &#x60;daily&#x60;. | [optional] 
 **triggerByShareRecipients** | **Boolean**| Notify when actions are performed by a share recipient? | [optional] 
 **triggeringFilenames** | [**[String]**](String.md)| Array of filenames (possibly with wildcards) to match for action path | [optional] 
 **triggeringGroupIds** | [**[Number]**](Number.md)| Only notify on actions made by a member of one of the specified groups | [optional] 
 **triggeringUserIds** | [**[Number]**](Number.md)| Only notify on actions made one of the specified users | [optional] 
 **userId** | **Number**| The id of the user to notify. Provide &#x60;user_id&#x60;, &#x60;username&#x60; or &#x60;group_id&#x60;. | [optional] 
 **username** | **String**| The username of the user to notify.  Provide &#x60;user_id&#x60;, &#x60;username&#x60; or &#x60;group_id&#x60;. | [optional] 

### Return type

[**NotificationEntity**](NotificationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

