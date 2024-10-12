# AirbyteConfigurationApi.NotificationsApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tryNotificationConfig**](NotificationsApi.md#tryNotificationConfig) | **POST** /v1/notifications/try | Try sending a notifications



## tryNotificationConfig

> NotificationRead tryNotificationConfig(notification)

Try sending a notifications

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.NotificationsApi();
let notification = new AirbyteConfigurationApi.Notification(); // Notification | 
apiInstance.tryNotificationConfig(notification, (error, data, response) => {
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
 **notification** | [**Notification**](Notification.md)|  | 

### Return type

[**NotificationRead**](NotificationRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

