# AgcoApi.NotificationsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notificationsPostMail**](NotificationsApi.md#notificationsPostMail) | **POST** /api/v2/Notifications | Sends an email message.



## notificationsPostMail

> notificationsPostMail(aPIModelsNotification)

Sends an email message.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.NotificationsApi();
let aPIModelsNotification = new AgcoApi.APIModelsNotification(); // APIModelsNotification | The Notification Object.
apiInstance.notificationsPostMail(aPIModelsNotification, (error, data, response) => {
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
 **aPIModelsNotification** | [**APIModelsNotification**](APIModelsNotification.md)| The Notification Object. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

