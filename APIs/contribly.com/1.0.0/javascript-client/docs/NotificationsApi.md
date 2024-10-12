# Contribly.NotificationsApi

All URIs are relative to *https://api.contribly.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notificationsContributionsIdPreviewGet**](NotificationsApi.md#notificationsContributionsIdPreviewGet) | **GET** /notifications/contributions/{id}/preview | 



## notificationsContributionsIdPreviewGet

> NotificationPreview notificationsContributionsIdPreviewGet(id, message)



### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.NotificationsApi();
let id = "id_example"; // String | Id of the contribution to preview a notification for
let message = "message_example"; // String | Type of message to preview.
apiInstance.notificationsContributionsIdPreviewGet(id, message, (error, data, response) => {
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
 **id** | **String**| Id of the contribution to preview a notification for | 
 **message** | **String**| Type of message to preview. | 

### Return type

[**NotificationPreview**](NotificationPreview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

