# DiscourseApiDocumentation.NotificationsApi

All URIs are relative to *http://discourse.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNotifications**](NotificationsApi.md#getNotifications) | **GET** /notifications.json | Get the notifications that belong to the current user
[**markNotificationsAsRead**](NotificationsApi.md#markNotificationsAsRead) | **PUT** /notifications/mark-read.json | Mark notifications as read



## getNotifications

> GetNotifications200Response getNotifications()

Get the notifications that belong to the current user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.NotificationsApi();
apiInstance.getNotifications((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetNotifications200Response**](GetNotifications200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## markNotificationsAsRead

> UpdateGroup200Response markNotificationsAsRead(opts)

Mark notifications as read

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.NotificationsApi();
let opts = {
  'markNotificationsAsReadRequest': new DiscourseApiDocumentation.MarkNotificationsAsReadRequest() // MarkNotificationsAsReadRequest | 
};
apiInstance.markNotificationsAsRead(opts, (error, data, response) => {
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
 **markNotificationsAsReadRequest** | [**MarkNotificationsAsReadRequest**](MarkNotificationsAsReadRequest.md)|  | [optional] 

### Return type

[**UpdateGroup200Response**](UpdateGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

