# FilesComApi.ActionNotificationExportsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getActionNotificationExportsId**](ActionNotificationExportsApi.md#getActionNotificationExportsId) | **GET** /action_notification_exports/{id} | Show Action Notification Export
[**postActionNotificationExports**](ActionNotificationExportsApi.md#postActionNotificationExports) | **POST** /action_notification_exports | Create Action Notification Export



## getActionNotificationExportsId

> ActionNotificationExportEntity getActionNotificationExportsId(id)

Show Action Notification Export

Show Action Notification Export

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ActionNotificationExportsApi();
let id = 56; // Number | Action Notification Export ID.
apiInstance.getActionNotificationExportsId(id, (error, data, response) => {
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
 **id** | **Number**| Action Notification Export ID. | 

### Return type

[**ActionNotificationExportEntity**](ActionNotificationExportEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postActionNotificationExports

> ActionNotificationExportEntity postActionNotificationExports(opts)

Create Action Notification Export

Create Action Notification Export

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ActionNotificationExportsApi();
let opts = {
  'endAt': new Date("2013-10-20T19:20:30+01:00"), // Date | End date/time of export range.
  'queryFolder': "queryFolder_example", // String | Return notifications that were triggered by actions in this folder.
  'queryMessage': "queryMessage_example", // String | Error message associated with the request, if any.
  'queryPath': "queryPath_example", // String | Return notifications that were triggered by actions on this specific path.
  'queryRequestMethod': "queryRequestMethod_example", // String | The HTTP request method used by the webhook.
  'queryRequestUrl': "queryRequestUrl_example", // String | The target webhook URL.
  'queryStatus': "queryStatus_example", // String | The HTTP status returned from the server in response to the webhook request.
  'querySuccess': true, // Boolean | true if the webhook request succeeded (i.e. returned a 200 or 204 response status). false otherwise.
  'startAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Start date/time of export range.
  'userId': 56 // Number | User ID.  Provide a value of `0` to operate the current session's user.
};
apiInstance.postActionNotificationExports(opts, (error, data, response) => {
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
 **endAt** | **Date**| End date/time of export range. | [optional] 
 **queryFolder** | **String**| Return notifications that were triggered by actions in this folder. | [optional] 
 **queryMessage** | **String**| Error message associated with the request, if any. | [optional] 
 **queryPath** | **String**| Return notifications that were triggered by actions on this specific path. | [optional] 
 **queryRequestMethod** | **String**| The HTTP request method used by the webhook. | [optional] 
 **queryRequestUrl** | **String**| The target webhook URL. | [optional] 
 **queryStatus** | **String**| The HTTP status returned from the server in response to the webhook request. | [optional] 
 **querySuccess** | **Boolean**| true if the webhook request succeeded (i.e. returned a 200 or 204 response status). false otherwise. | [optional] 
 **startAt** | **Date**| Start date/time of export range. | [optional] 
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 

### Return type

[**ActionNotificationExportEntity**](ActionNotificationExportEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

